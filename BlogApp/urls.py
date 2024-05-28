from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main_view, name='main'),
    path('szukaj/<str:tag_name>', views.tag_view, name='szukaj'),
    path('post/<int:post_id>', views.post_view, name='post'),
    path('dodaj_post', views.add_post_view, name='add_post'),
    path('usun_post/<int:post_id>', views.delete_post_view, name='delete_post'),
    path('dodaj_komentarz/<int:post_id>', views.add_comment_view, name='add_comment'),
    path('usun_komentarz/<int:post_id>/<int:comment_id>', views.delete_comment_view, name='delete_comment'),
]