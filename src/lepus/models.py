# encoding=utf-8
import pickle
import hashlib
import time
import datetime
from django.utils.timezone import utc
import base64
from django.conf import settings
from django.db import models
from django.contrib.auth.models import UserManager as DjangoUserManager
from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.contrib.auth.hashers import make_password, check_password
from os.path import normpath, join
from lepus.settings import BASE_DIR

class Templete(models.Model):
    """全てのモデルで共通のフィールドを含んだAbstract Model"""
    class Meta:
        abstract = True
    created_at = models.DateTimeField("作成日時", auto_now_add=True)
    updated_at = models.DateTimeField("最終更新日時", auto_now=True)

class Category(Templete):
    """問題のカテゴリ"""
    class Meta:
        ordering = ('ordering', 'id',)

    name = models.CharField("カテゴリ名", max_length=50, unique=True)
    ordering = models.IntegerField("表示順序", default=100)

    def __str__(self):
        return self.name


class QuestionManager(models.Manager):
    def public(self):
        return self.get_queryset().filter(is_public=True)

class Question(Templete):
    """問題"""
    class Meta:
        ordering = ('category', 'ordering', 'id',)

    category = models.ForeignKey(Category, verbose_name="カテゴリ")
    ordering = models.IntegerField("表示順序", default=100)
    title = models.CharField("タイトル", max_length=50)
    sentence = models.TextField("問題文")
    max_answers = models.IntegerField("最大回答者数", blank=True, null=True)
    max_failure = models.IntegerField("最大回答数", blank=True, null=True)
    is_public = models.BooleanField("公開にするか", blank=True, default=False)

    objects = QuestionManager()

    @property
    def points(self):
        return sum([o.point for o in self.flag_set.all()])

    def __str__(self):
        return self.title

    @property
    def files(self):
        return filter(lambda f:f.is_public, self.file_set.all())


class Flag(Templete):
    """正解のフラグと得点"""
    flag = models.CharField("Flag", max_length=200, unique=True)
    question = models.ForeignKey(Question, verbose_name="問題")
    point = models.IntegerField("得点")

    def __str__(self):
        return self.flag

    @property
    def teams(self):
        return [a["team_id"] for a in Answer.objects.filter(flag=self).values("team_id")]

class FileManager(models.Manager):
    def public(self):
        return self.get_queryset().filter(is_public=True, question__is_public=True)

class File(Templete):
    """問題に添付するファイル"""
    question = models.ForeignKey(Question, verbose_name="問題")
    name = models.CharField("ファイル名", max_length=256)
    file = models.FileField(upload_to='question/', max_length=256, verbose_name="ファイル")
    is_public = models.BooleanField("公開するか", blank=True, default=True)

    objects = FileManager()

    @property
    def url(self):
        return reverse("download_file", args=(self.id, self.name))

    @property
    def size(self):
        return self.file.size

    def __str__(self):
        return self.name

class Team(Templete):
    """チーム"""
    name = models.CharField("チーム名", max_length=32, unique=True)
    password = models.CharField("チームパスワード", max_length=128)
    last_score_time = models.DateTimeField("最終得点日時", blank=True, null=True)

    def __str__(self):
        return self.name

    def set_password(self, password):
        self.password = make_password(password)

    def check_password(self, raw_password):
        """
        Return a boolean of whether the raw_password was correct. Handles
        hashing formats behind the scenes.
        """
        def setter(raw_password):
            self.set_password(raw_password)
            # Password hash upgrades shouldn't be considered password changes.
            self._password = None
            self.save(update_fields=["password"])
        return check_password(raw_password, self.password, setter)

    @property
    def token(self):
        sha1 = hashlib.sha1()
        sha1.update("{0}_{1}_{2}".format(
                                         settings.TEAM_TOKEN_SECRET_KEY,
                                         self.id,
                                         int(time.time() / settings.TEAM_TOKEN_INTERVAL
                                             )).encode("utf-8"))
        return sha1.hexdigest()

    @property
    def points(self):
        answers = filter(lambda a:a.flag_id, self.answer_set.all())
        points = 0
        for answer in answers:
            points += answer.flag.point

        for attack_point in self.attackpoint_set.all():
            points += attack_point.point

        return points

    @property
    def questions(self):
        data = {}
        answers = filter(lambda a:a.flag_id, self.answer_set.all())

        for answer in answers:
            question = answer.flag.question
            if not question.id in data:
                data[question.id] = {
                    "id": question.id,
                    "cat": question.category.id,
                    "flags":0,
                    "points":0
                }
            data[question.id]["flags"] += 1
            data[question.id]["points"] += answer.flag.point
            
        return data.values()


class UserManager(DjangoUserManager):
    def by_ip(self, ip):
        try:
            user_connection = UserConnection.objects.filter(ip=ip).order_by("-updated_at")[0]
        except IndexError:
            return User.objects.none()
        return self.get_queryset().filter(id=user_connection.user.id)


class User(AbstractUser, Templete):
    """チームに属するユーザ"""
    team = models.ForeignKey(Team, verbose_name="チーム", blank=True, null=True)
    seat = models.CharField("座席", max_length=32, blank=True)
    last_score_time = models.DateTimeField("最終得点日時", blank=True, null=True)
    
    objects = UserManager()

    def __str__(self):
        return self.username

    @property
    def points(self):
        answers = Answer.objects.filter(user=self).exclude(flag=None)
        points = 0
        for answer in answers:
            points += answer.flag.point

        for attack_point in AttackPoint.objects.filter(user=self):
            points += attack_point.point

        return points

    @property
    def ip(self):
        try:
            user_connection = self.userconnection_set.order_by("-updated_at")[0]
        except IndexError:
            return None
        return user_connection.ip

class UserConnection(Templete):
    """ユーザの接続元を管理するモデル"""
    class Meta:
        unique_together = (('user', 'ip'),)
        ordering = ("-updated_at",)

    user = models.ForeignKey(User, verbose_name="ユーザー")
    ip = models.GenericIPAddressField("IPアドレス")

    @classmethod
    def update(cls, user, ip):
        """アクセス元IPの更新"""
        user_connection, created = cls.objects.get_or_create(user=user, ip=ip)
        if not created:
            user_connection.updated_at = datetime.datetime.utcnow().replace(tzinfo=utc)
            user_connection.save()
        return user_connection

class Answer(Templete):
    """回答履歴"""
    class Meta:
        unique_together = (('team', 'flag'),)
    user = models.ForeignKey(User, verbose_name="ユーザー")
    team = models.ForeignKey(Team, verbose_name="チーム")
    question = models.ForeignKey(Question, verbose_name="問題")
    flag = models.ForeignKey(Flag, blank=True, null=True)
    answer = models.CharField("解答", max_length=256)

    @property
    def is_correct(self):
        return self.flag is not None

class AttackPoint(Templete):
    """攻撃点記録"""
    user = models.ForeignKey(User, verbose_name="ユーザー")
    team = models.ForeignKey(Team, verbose_name="チーム")
    question = models.ForeignKey(Question, verbose_name="問題")
    token = models.CharField("トークン", max_length=256, unique=True)
    point = models.IntegerField("得点")

class Config(Templete):
    """設定用モデル"""
    key = models.CharField("設定項目", max_length=256, unique=True)
    value_str = models.TextField("シリアライズされた値")

    def __str__(self):
        return self.key

    def get_value(self):
        return pickle.loads(base64.b64decode(self.value_str))
    def set_value(self, value):
        self.value_str = base64.b64encode(pickle.dumps(value))
    value = property(get_value, set_value)

    @classmethod
    def get(cls, key, default=None):
        try:
            config = cls.objects.get(key=key)
            return config.value
        except Config.DoesNotExist:
            return default

    @classmethod
    def set(cls, key, value):
        config, created = Config.objects.get_or_create(key=key)
        config.value = value
        config.save()
        return config

class Notice(Templete):
    """お知らせ"""
    class Meta:
        ordering = ['created_at']
    title = models.CharField("タイトル", max_length=80)
    description = models.TextField("本文")
    priority = models.IntegerField(default=0)
    is_public = models.BooleanField("公開にするか", blank=True, default=False)

    def __str__(self):
        return self.title
