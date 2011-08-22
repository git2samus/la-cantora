from google.appengine.ext.webapp import RequestHandler, template

class WebsiteHandler(RequestHandler):
    def get(self):
        page = template.render('templates/index.html', {})
        self.response.out.write(page)

