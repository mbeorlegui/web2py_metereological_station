# -*- coding: utf-8 -*-

import sqlite3

### required - do no delete
def user(): return dict(form=auth())
def download(): return response.download(request,db)
def call(): return service()
### end requires

temp9=0
temp8=0
temp7=0
temp6=0
temp5=0
temp4=0
temp3=0
temp2=0
temp1=0
temp0=0
humedad9=0
humedad8=0
humedad7=0
humedad6=0
humedad5=0
humedad4=0
humedad3=0
humedad2=0
humedad1=0
humedad0=0
presion9=0
presion8=0
presion7=0
presion6=0
presion5=0
presion4=0
presion3=0
presion2=0
presion1=0
presion0=0
st9=0
st8=0
st7=0
st6=0
st5=0
st4=0
st3=0
st2=0
st1=0
st0=0

def index():
    response.flash = T("Hola usuarios!")
    return dict(message=T('Welcome to web2py!'))

def error():
    return dict()

def registro_clima_manage():
    form = SQLFORM.smartgrid(db.t_registro_clima,onupdate=auth.archive)
    return locals()

def actual_manage():
    return dict()

def pide_datos():
	global temp9, temp8, temp7, temp6, temp5, temp4, temp3, temp2, temp1, temp0
	global humedad9, humedad8, humedad7, humedad6, humedad5, humedad4, humedad3, humedad2, humedad1, humedad0
	global presion9, presion8, presion7, presion6, presion5, presion4, presion3, presion2, presion1, presion0
	global st9, st8, st7, st6, st5, st4, st3, st2, st1, st0
	
	con=sqlite3.connect('C:\storage.sqlite')
	##C:\Users\Marcelo\Desktop\PRUEBAS\storage.sqlite
	##C:\storage.sqlite
	##C:\Users\Marcelo\Desktop\web2py\applications\Estacion_meteoro\databases\storage.sqlite

	cursor = con.cursor()
	
	a=0

	cursor.execute("SELECT temperatura FROM t_registro_clima order by id desc LIMIT 10")

	for i in cursor:
		
		if a==0:
			temp0=i[0]
		if a==1:
			temp1=i[0]
		if a==2:
			temp2=i[0]
		if a==3:
			temp3=i[0]
		if a==4:
			temp4=i[0]
		if a==5:
			temp5=i[0]
		if a==6:
			temp6=i[0]
		if a==7:
			temp7=i[0]
		if a==8:
			temp8=i[0]
		if a==9:
			temp9=i[0]
		a=a+1

	a=0
	cursor.execute("SELECT humedad FROM t_registro_clima order by id desc LIMIT 10")

	for i in cursor:
		
		if a==0:
			humedad0=i[0]
		if a==1:
			humedad1=i[0]
		if a==2:
			humedad2=i[0]
		if a==3:
			humedad3=i[0]
		if a==4:
			humedad4=i[0]
		if a==5:
			humedad5=i[0]
		if a==6:
			humedad6=i[0]
		if a==7:
			humedad7=i[0]
		if a==8:
			humedad8=i[0]
		if a==9:
			humedad9=i[0]
		a=a+1

	a=0
	cursor.execute("SELECT fechahora FROM t_registro_clima order by id desc LIMIT 10")

	for i in cursor:
		
		if a==0:
			fechahora0=i[0]
		if a==1:
			fechahora1=i[0]
		if a==2:
			fechahora2=i[0]
		if a==3:
			fechahora3=i[0]
		if a==4:
			fechahora4=i[0]
		if a==5:
			fechahora5=i[0]
		if a==6:
			fechahora6=i[0]
		if a==7:
			fechahora7=i[0]
		if a==8:
			fechahora8=i[0]
		if a==9:
			fechahora9=i[0]
		a=a+1

	a=0
	cursor.execute("SELECT sensacion_termica FROM t_registro_clima order by id desc LIMIT 10")

	for i in cursor:
		
		if a==0:
			st0=i[0]
		if a==1:
			st1=i[0]
		if a==2:
			st2=i[0]
		if a==3:
			st3=i[0]
		if a==4:
			st4=i[0]
		if a==5:
			st5=i[0]
		if a==6:
			st6=i[0]
		if a==7:
			st7=i[0]
		if a==8:
			st8=i[0]
		if a==9:
			st9=i[0]
		a=a+1

	a=0
	cursor.execute("SELECT presion FROM t_registro_clima order by id desc LIMIT 10")

	for i in cursor:
		
		if a==0:
			presion0=i[0]
		if a==1:
			presion1=i[0]
		if a==2:
			presion2=i[0]
		if a==3:
			presion3=i[0]
		if a==4:
			presion4=i[0]
		if a==5:
			presion5=i[0]
		if a==6:
			presion6=i[0]
		if a==7:
			presion7=i[0]
		if a==8:
			presion8=i[0]
		if a==9:
			presion9=i[0]
		a=a+1



@service.json
def series_temp():
	global temp9, temp8, temp7, temp6, temp5, temp4, temp3, temp2, temp1, temp0
	
	s = '{"series":[['
	
	flotante = float(temp9)
	s = s + "%f, " % (flotante)
	flotante = float(temp8)
	s = s + "%f, " % (flotante)
	flotante = float(temp7)
	s = s + "%f, " % (flotante)
	flotante = float(temp6)
	s = s + "%f, " % (flotante)
	flotante = float(temp5)
	s = s + "%f, " % (flotante)
	flotante = float(temp4)
	s = s + "%f, " % (flotante)
	flotante = float(temp3)
	s = s + "%f, " % (flotante)
	flotante = float(temp2)
	s = s + "%f, " % (flotante)
	flotante = float(temp1)
	s = s + "%f, " % (flotante)
	flotante = float(temp0)
	s = s + "%f, " % (flotante)
	
	s = s[:-2] + ']]}'
	print s
	return s
	
@service.json
def series_hume():
	global humedad9, humedad8, humedad7, humedad6, humedad5, humedad4, humedad3, humedad2, humedad1, humedad0
	
	s = '{"series":[['
	
	flotante = float(humedad9)
	s = s + "%f, " % (flotante)
	flotante = float(humedad8)
	s = s + "%f, " % (flotante)
	flotante = float(humedad7)
	s = s + "%f, " % (flotante)
	flotante = float(humedad6)
	s = s + "%f, " % (flotante)
	flotante = float(humedad5)
	s = s + "%f, " % (flotante)
	flotante = float(humedad4)
	s = s + "%f, " % (flotante)
	flotante = float(humedad3)
	s = s + "%f, " % (flotante)
	flotante = float(humedad2)
	s = s + "%f, " % (flotante)
	flotante = float(humedad1)
	s = s + "%f, " % (flotante)
	flotante = float(humedad0)
	s = s + "%f, " % (flotante)

	s = s[:-2] + ']]}'
	print s
	return s
  
@service.json    
def series_presion():
	global presion9, presion8, presion7, presion6, presion5, presion4, presion3, presion2, presion1, presion0
	
	s = '{"series":[['
	
	flotante = float(presion9)
	s = s + "%f, " % (flotante)
	flotante = float(presion8)
	s = s + "%f, " % (flotante)
	flotante = float(presion7)
	s = s + "%f, " % (flotante)
	flotante = float(presion6)
	s = s + "%f, " % (flotante)
	flotante = float(presion5)
	s = s + "%f, " % (flotante)
	flotante = float(presion4)
	s = s + "%f, " % (flotante)
	flotante = float(presion3)
	s = s + "%f, " % (flotante)
	flotante = float(presion2)
	s = s + "%f, " % (flotante)
	flotante = float(presion1)
	s = s + "%f, " % (flotante)
	flotante = float(presion0)
	s = s + "%f, " % (flotante)
	
	s = s[:-2] + ']]}'
	
	print s
	return s
	
	
@service.json
def series_st():
	global st9, st8, st7, st6, st5, st4, st3, st2, st1, st0
	
	s = '{"series":[['

	flotante = float(st9)
	s = s + "%f, " % (flotante)
	flotante = float(st8)
	s = s + "%f, " % (flotante)
	flotante = float(st7)
	s = s + "%f, " % (flotante)
	flotante = float(st6)
	s = s + "%f, " % (flotante)
	flotante = float(st5)
	s = s + "%f, " % (flotante)
	flotante = float(st4)
	s = s + "%f, " % (flotante)
	flotante = float(st3)
	s = s + "%f, " % (flotante)
	flotante = float(st2)
	s = s + "%f, " % (flotante)
	flotante = float(st1)
	s = s + "%f, " % (flotante)
	flotante = float(st0)
	s = s + "%f, " % (flotante)
	
	
	s = s[:-2] + ']]}'
	print s
	return s
	
pide_datos()
##series_temp()
##series_st()
##series_presion()

