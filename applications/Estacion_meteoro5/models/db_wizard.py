### we prepend t_ to tablenames and f_ to fieldnames for disambiguity


########################################
db.define_table('t_registro_clima',
    Field('fechahora', type='string',
          label=T('Fecha y hora')),
    Field('temperatura', type='string',
          label=T('Temperatura')),
    Field('humedad', type='string',
          label=T('Humedad')),
    Field('sensacion_termica', type='string',
          label=T('Sensacion termica')),
    Field('direccion_viento', type='string',
          label=T('Direccion de viento (km/h)')),
    Field('velocidad_viento', type='string',
          label=T('Velocidad de viento')),
    Field('indice_uv', type='string',
          label=T('Indice UV')),
    Field('cantidad_lluvia', type='string',
          label=T('Cantidad de lluvia (mm)')),
    format='%(f_temperatura)s',
    migrate=settings.migrate)

db.define_table('t_registro_clima_archive',db.t_registro_clima,Field('current_record','reference t_registro_clima',readable=False,writable=False))
