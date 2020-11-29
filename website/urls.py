from django.urls import path
from . import views
from . import ajax

app_name = "website"

urlpatterns = [
    path('ajax/get-video-links', ajax.get_video_links, name="get_video_links"),
]

urlpatterns += [
    path('', views.Index.as_view(), name="index"),
]
