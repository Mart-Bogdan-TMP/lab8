from django.conf.urls import url
from . import views

app_name = 'tables'

urlpatterns = [
    url(r'^info/', views.to_homepage, name='homepage'),
    # /tables/
    url(r'^$', views.index, name='index'),

     # /tables/table_name_details/
    url(r'^tables/posts', views.details_posts, name='details_posts'),

    #add_objectname
    url(r'^post_create/$', views.PostCreate.as_view(), name='create_post'),

    # remove_objectname
    url(r'^delete/(?P<pk>\d+)$', views.post_delete, name='delete_post'),
]