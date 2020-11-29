import pytube


def get_youtube_video_url(url):
    video = pytube.YouTube(url)
    videos = []
    for item in video.streams:
        if item.audio_codec == None:
            continue
        video_item = {}
        video_item["res"] = item.resolution
        video_item["type"] = item.mime_type
        video_item["itag"] = item.itag
        video_item["url"] = item.url
        video_item["title"] = item.title
        videos.append(video_item)
    return videos, video.thumbnail_url, video.title
