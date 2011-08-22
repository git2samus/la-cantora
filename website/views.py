from google.appengine.ext.webapp import RequestHandler

class WebsiteHandler(RequestHandler):
    def get(self):
        self.response.out.write('Hello world!')

