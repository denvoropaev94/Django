from .views import my_view, TemplIf, view_for
from django.urls import path
from .views import index, about
from .views import author_posts, post_full


urlpatterns = [
    path('', my_view, name="index"),
    path('if/', TemplIf.as_view(), name='templ_if'),
    path('for/', view_for, name='templ_for'),
    path('index/', index, name='index'),
    path('about/', about, name='about'),
    path('author/<int:author_id>/', author_posts, name="author_posts"),
    path('post/<int:post_id>/', post_full, name='post_full'),
]
