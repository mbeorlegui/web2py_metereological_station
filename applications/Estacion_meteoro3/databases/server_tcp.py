#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sqlite3

con = sqlite3.connect('registro.db')

##cur = con.cursor()
##qry = """insert into t_registro_clima
##			(f_temperatura, 
##			 f_humedad, 
##			 f_sensacion_termica)  
##		values (?, ?, ?)"""
##
##te = '343'
##hu = '777'
##st = '999'
##
##cur.execute(qry, (te, hu, st))
##con.commit()
##		
##exit()

direccion = ""
puerto = 9138

s = socket.socket()

s.bind(( direccion, puerto))

while True:
	s.listen(1)

	sc, addr = s.accept()

	err = 0
	while True:
		try:
		#if True:
			recibido = sc.recv(1024)
	  
			if recibido == "exit":
				err = 0
				break
	  
			print "Recibido:", recibido	
			
			if len(recibido) > 0:
				try: 
                                        cur = con.cursor()
					qry = """insert into t_registro_clima
                                                                        (fecha=fechahora,
                                                                        temperatura= T,
                                                                        humedad= H,
                                                                        sensacion_termica= ST,
                                                                        direccion_viento=DV,
                                                                        velocidad_viento=VV,
                                                                        indice_uv=UV,
                                                                        cantidad_lluvia=LL)
                                                                        values (?, ?, ?)"""
					
					aux = recibido
					T,H,ST,DV,VV,UV,LL=aux.split(";")
					T=float(T[1:])
					H=H[1:]
					ST=float(ST[2:])
					DV=DV[2:]
					VV=VV[2:]
					UV=UV[2:]
					LL=LL[2:]
					T=T/10
					ST=ST/10
					
					cur.execute(qry, (fechahora,T,H,ST,DV,VV,UV,LL))
					con.commit()
					
				except:
                                        print("error de base de datos")
					
		
		except:
			sc.close()  
			err = 1
			break 
		
if err == 0:
	sc.close()
	s.close()
	conn.close()
