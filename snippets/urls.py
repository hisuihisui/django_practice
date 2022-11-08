from django.urls import include, path
from rest_framework import routers

from snippets import api_views as snippet_api_views
from snippets.views import snippet_detail, snippet_edit, snippet_new


router = routers.DefaultRouter()
router.register("snippets", snippet_api_views.SnippetViewSet)

urlpatterns = [
    path("new/", snippet_new, name="snippet_new"),
    path("<int:snippet_id>/", snippet_detail, name="snippet_detail"),
    path("<int:snippet_id>/edit/", snippet_edit, name="snippet_edit"),
    path("api/", include(router.urls)),
]
