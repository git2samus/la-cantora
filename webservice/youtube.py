from gdata.youtube.service import YouTubeService, YouTubeVideoQuery
from gdata.alt.appengine import run_on_appengine
import settings

def search(q, restrict=None):
    yt_service = YouTubeService()
    run_on_appengine(yt_service)

    yt_service.ssl = True
    yt_service.developer_key = settings.YOUTUBE_API_KEY

    query = YouTubeVideoQuery()
    query.vq = q
    if restrict:
        query.restriction = restrict

    return yt_service.YouTubeQuery(query)
