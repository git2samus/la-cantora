#!/usr/bin/env python
import os, sys, settings
sys.path.append(os.path.join(settings.APPROOT, 'lib', 'python'))

from google.appengine.dist import use_library
use_library('django', '1.2')

from google.appengine.ext.webapp import WSGIApplication
from google.appengine.ext.webapp.util import run_wsgi_app
from website.views import WebsiteHandler

def main():
    urlpatterns = [
        ('/', WebsiteHandler)
    ]
    application = WSGIApplication(urlpatterns, debug=settings.DEBUG)
    run_wsgi_app(application)


if __name__ == '__main__':
    main()
