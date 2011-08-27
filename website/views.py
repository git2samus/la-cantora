from google.appengine.ext.webapp import RequestHandler, template
from webservice import youtube
from util import context_dict

class WebsiteHandler(RequestHandler):
    def get(self):
        request, response = self.request, self.response

        q = request.get('q')
        if q:
            result = youtube.search(q, restrict=request.remote_addr)

        page = template.render('templates/index.html', context_dict(locals(), 'result'))
        response.out.write(page)

