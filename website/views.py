from google.appengine.ext.webapp import RequestHandler, template

# helper to initialize template context from locals()
def context_dict(locals_dict, *varnames, **overrides):
    context = {'request': locals_dict.get('request')}
    context.update((varname, locals_dict.get(varname)) for varname in varnames)
    context.update(overrides)
    return context

class WebsiteHandler(RequestHandler):
    def get(self):
        q = self.request.get('q')

        page = template.render('templates/index.html', context_dict(locals(), 'result'))
        self.response.out.write(page)

