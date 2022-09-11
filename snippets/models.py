from django.conf import settings
from django.db import models


# Managerのカスタマイズ
class DraftSnippetManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_draft=True)


class SnippetQuerySet(models.QuerySet):
    def drafts(self):
        return self.filter(is_draft=False)

    # アンダースコアから始まる関数
    # Managerからアクセス不可、QuerySetからアクセス可能
    def _recent_updates(self):
        return self.order_by("-updated_at")

    # queryset_only = True
    # Managerからアクセス不可、QuerySetからアクセス可能
    # recent_updates.queryset_only = True


class Snippet(models.Model):
    title = models.CharField("タイトル", max_length=128)
    code = models.TextField("コード", blank=True)
    description = models.TextField(
        "説明",
        null=False,  # nullは許容しない
        default="",  # デフォルトは空文字
        blank=True,  # バリデーション処理に使用
    )
    is_draft = models.BooleanField("Draft", default=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    updated_at = models.DateTimeField("更新日", auto_now=True)

    # 通常のManagerを使う場合
    # objects = models.Manager()
    objects = SnippetQuerySet.as_manager()
    # QuerySet をうけとって、Managerを作成する
    # objects = DraftSnippetManager.from_queryset(SnippetQuerySet)()
    drafts = DraftSnippetManager()

    # 細かい設定ができる
    class Meta:
        # テーブル名の変更
        db_table = "snippets"

    def __str__(self):
        return f"{self.pk} {self.title}"


class Comment(models.Model):
    text = models.CharField("コメントを投稿する", max_length=128)
    commented_at = models.DateTimeField("投稿日", auto_now_add=True)
    commented_to = models.ForeignKey(
        Snippet, verbose_name="スニペット", on_delete=models.CASCADE
    )
    commented_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, verbose_name="投稿者", on_delete=models.CASCADE
    )

    class Meta:
        db_table = "comments"

    def __str__(self):
        return f"{self.pk} {self.text}"


class Tag(models.Model):
    name = models.CharField("タグ名", max_length=32)
    # ManyToMany
    # これを設定すると、中間テーブルが自動で生成
    snippets = models.ManyToManyField(
        Snippet, related_name="tags", related_query_name="tag"
    )

    class Meta:
        db_table = "tags"

    def __str__(self):
        return f"{self.pk} {self.name}"


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
