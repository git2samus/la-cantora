#!/usr/bin/env python

from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app
from website.views import WebsiteHandler

def main():
    urlpatterns = [
        ('/', WebsiteHandler)
    ]
    application = WSGIApplication(urlpatterns, debug=True)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
