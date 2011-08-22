# helper to initialize template context from locals()
def context_dict(locals_dict, *varnames, **overrides):
    context = {'request': locals_dict.get('request')}
    context.update((varname, locals_dict.get(varname)) for varname in varnames)
    context.update(overrides)
    return context
