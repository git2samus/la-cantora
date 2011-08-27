from urllib import urlencode
from urllib2 import Request, urlopen
import settings

def search(q, restrict=None):
    query_string_dict = {
        'q': q,
        'v': 2,
    }
    if restrict:
        query_string_dict.update(restrict=restrict)

    endpoint = 'https://gdata.youtube.com/feeds/api/videos'
    query_string = urlencode(query_string_dict)

    request = Request('%s?%s' % (endpoint, query_string))
    request.add_header('X-GData-Key', 'key=%s' % settings.YOUTUBE_API_KEY)

    response = urlopen(request)
    return response.read()

