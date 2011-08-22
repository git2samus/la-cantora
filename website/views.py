from google.appengine.ext.webapp import RequestHandler, template
from util import context_dict

class WebsiteHandler(RequestHandler):
    def get(self):
        q = self.request.get('q')

        page = template.render('templates/index.html', context_dict(locals(), 'result'))
        self.response.out.write(page)

