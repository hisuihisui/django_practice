from django.contrib.auth import get_user_model
from django.test import RequestFactory, TestCase
from django.urls import resolve

from snippets.models import Snippet
from snippets.views import snippet_edit, top

UserModel = get_user_model()


# Create your tests here.
# TestCaseクラスは各テストケースの実行前にトランザクションを開始
#  → 終了後ロールバックをして、変更を取り消す
class TopPageTest(TestCase):
    def test_top_page_returns_200_and_expected_title(self):
        response = self.client.get("/")
        self.assertContains(response, "Django スニペット", status_code=200)

    def test_top_page_uses_expected_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "snippets/top.html")


class TopPageRenderSnippetsTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass001",
        )
        self.snippet = Snippet.objects.create(
            title="title1",
            code="print('hello')",
            description="description1",
            created_by=self.user,
        )

    def test_should_return_snippet_title(self):
        # RequestFactoryクラス
        # GETやPOSTメソッドのRequestオブジェクトを簡単に生成
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.snippet.title)

    def test_should_return_username(self):
        request = RequestFactory().get("/")
        request.user = self.user
        response = top(request)
        self.assertContains(response, self.user.username)


class CreateSnippetTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass001",
        )
        # ログインする
        self.client.force_login(self.user)

    def test_render_creation_form(self):
        response = self.client.get("/snippets/new/")
        self.assertContains(response, "スニペットの登録", status_code=200)

    def test_create_snippet(self):
        data = {
            "title": "タイトル",
            "code": "コード",
            "description": "解説",
        }
        self.client.post("/snippets/new/", data)
        snippet = Snippet.objects.get(title="タイトル")
        self.assertEqual(snippet.code, "コード")
        self.assertEqual(snippet.description, "解説")


class SnippetDetailTest(TestCase):
    def setUp(self):
        self.user = UserModel.objects.create(
            username="test_user",
            email="test@example.com",
            password="top_secret_pass001",
        )
        self.snippet = Snippet.objects.create(
            title="タイトル",
            code="コード",
            description="解説",
            created_by=self.user,
        )

    def test_should_use_expected_template(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertTemplateUsed(response, "snippets/snippet_detail.html")

    def test_detail_page_returns_200_and_expected_heading(self):
        response = self.client.get("/snippets/%s/" % self.snippet.id)
        self.assertContains(response, self.snippet.title, status_code=200)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(snippet_edit, found.func)
