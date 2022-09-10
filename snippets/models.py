from django.conf import settings
from django.db import models


# Create your models here.
class Snippet(models.Model):
    title = models.CharField("タイトル", max_length=128)
    code = models.TextField("コード", blank=True)
    description = models.TextField(
        "説明",
        null=False,  # nullは許容しない
        default="",  # デフォルトは空文字
        blank=True,  # バリデーション処理に使用
    )
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    # 細かい設定ができる
    class Meta:
        # テーブル名の変更
        db_table = "snippets"

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.CharField("コメントを投稿する", max_length=128)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(
        Snippet, verbose_name="スニペット", on_delete=models.CASCADE
    )
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )


class Card(models.Model):
    # 選択肢の作成
    # models.IntegerChoices や models.TextChoices を使う
    class Suit(models.IntegerChoices):
        DIAMOND = 1
        SPADE = 2
        HEART = 3
        CLUB = 4

    # choices属性で指定
    suit = models.IntegerField(choices=Suit.choices)
