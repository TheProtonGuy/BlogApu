from django.urls import path
from . import views

urlpatterns = [
    path("get-blogs/", views.get_all_blogs),
    path("get-blog/<int:id>/", views.get_single_blog),
    path("create-blog/", views.create_blog),
    path("update-blog/<int:id>/", views.update_blog),
    path("delete-blog/<int:id>/", views.delete_blog),
]