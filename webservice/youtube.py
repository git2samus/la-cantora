from gdata.youtube.service import YouTubeService, YouTubeVideoQuery
from gdata.alt.appengine import run_on_appengine
import settings

def get_embed_code(entry):
    swf_url = entry.GetSwfUrl()
    if swf_url:
        return '''
            <object width="425" height="350">
                <param name="movie" value="%s"></param>
                <embed src="%s" type="application/x-shockwave-flash" width="425" height="350"></embed>
            </object>
        ''' % (swf_url, swf_url)

def search(q, restrict=None):
    yt_service = YouTubeService()
    run_on_appengine(yt_service)

    yt_service.ssl = True
    yt_service.developer_key = settings.YOUTUBE_API_KEY

    query = YouTubeVideoQuery()
    query.vq = q
    if restrict:
        query.restriction = restrict

    query.max_results = 1
    feed = yt_service.YouTubeQuery(query)
    return get_embed_code(feed.entry[0])
