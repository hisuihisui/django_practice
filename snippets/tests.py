from django.test import TestCase
from django.urls import resolve

from . import views


# Create your tests here.
class TopPageViewTest(TestCase):
    def test_top_returns_200(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)

    def test_top_returns_expected_content(self):
        response = self.client.get("/")
        self.assertEqual(response.content, b"Hello World")


class CreateSnippetTest(TestCase):
    def test_should_resolve_snippet_new(self):
        # パスを指定して対応するviews関数を探す
        found = resolve("/snippets/new/")
        # 関数同士の比較
        self.assertEqual(views.snippet_new, found.func)


class SnippetDetailTest(TestCase):
    def test_should_resolve_snippet_detail(self):
        found = resolve("/snippets/1/")
        self.assertEqual(views.snippet_detail, found.func)


class EditSnippetTest(TestCase):
    def test_should_resolve_snippet_edit(self):
        found = resolve("/snippets/1/edit/")
        self.assertEqual(views.snippet_edit, found.func)
