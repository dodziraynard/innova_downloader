from . utils import get_youtube_video_url
from django.shortcuts import render
from . utils import get_youtube_video_url


def get_video_links(request):
    url = request.POST.get("url")
    videos, thumbnail_url, title = get_youtube_video_url(url)
    context = {
        "title": title,
        "thumbnail_url": thumbnail_url,
        "videos": videos,
    }
    return render(request, "download_ajax.html", context)
