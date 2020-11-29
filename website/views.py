from django.shortcuts import render
from django.views.generic import View
from . utils import get_youtube_video_url


class Index(View):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        url = request.POST.get("url")
        videos, thumbnail_url, title = get_youtube_video_url(url)
        context = {
            "title": title,
            "thumbnail_url": thumbnail_url,
            "videos": videos,
        }
        return render(request, "download.html", context)
