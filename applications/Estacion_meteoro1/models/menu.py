response.title = settings.title
response.subtitle = settings.subtitle
response.meta.author = '%(author)s <%(author_email)s>' % settings
response.meta.keywords = settings.keywords
response.meta.description = settings.description
response.menu = [
(T('Index'),URL('default','index')==URL(),URL('default','index'),[]),
(T('Registro Clima'),URL('default','registro_clima_manage')==URL(),URL('default','registro_clima_manage'),[]),
(T('Actual'),URL('default','actual_manage')==URL(),URL('default','actual_manage'),[]),
]