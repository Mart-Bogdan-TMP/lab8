from django.conf.urls import url
from . import views

app_name = 'tables'

urlpatterns = [
    #return to homepage
    url(r'^info/', views.to_homepage, name='homepage'),

#=================================================================================
#TABLES
#=================================================================================
    url(r'^$', views.index, name='index'),

    # /posts/

    url(r'^tables/posts', views.details_posts, name='details_posts'),
    url(r'^post_create/$', views.PostCreate.as_view(), name='create_post'),
    url(r'^post_delete/(?P<pk>\d+)$', views.post_delete, name='delete_post'),

    # /workers/
    url(r'^tables/workers', views.details_workers, name='details_workers'),
    url(r'^worker_create/$', views.WorkerCreate.as_view(), name='create_worker'),
    url(r'^worker_delete/(?P<pk>\d+)$', views.worker_delete, name='delete_worker'),
]