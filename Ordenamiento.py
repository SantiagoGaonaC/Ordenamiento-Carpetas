# -*- coding: utf-8 -*-
"""
Created on Thu Apr  1 13:18:52 2021

@author: sgaon
"""
import os
import stat
import shutil
import datetime

# listdir: nombres directorio nombrado por la ruta que se le marca en este caso . que es la local del .py
# isfile: sobre el archivo que estamos manejando que en este caso son las listas de listdir

archivos = [f for f in os.listdir('.') if os.path.isfile(f)]


for i in archivos:
    if i.endswith('.py'): #Ignoramos archivos .py
        continue
    detalles = os.stat(i)#estadistica de la ruta
    a_creado = detalles[stat.ST_CTIME] #Creación archivo
    a_modificado = detalles[stat.ST_MTIME] #Última modificación
    a_acceso = detalles[stat.ST_ATIME] #Último acceso
    ultima_fecha = min(a_creado, a_modificado, a_acceso)#Devolver ultima fecha  
    a_año = str(datetime.date.fromtimestamp(ultima_fecha).year) #devuelve el año
    a_mes = datetime.date.fromtimestamp(ultima_fecha).strftime("%B") #B nombre completo mes
    archivo = str(a_año + '\\' + str(a_mes))
    if not os.path.exists(a_año):
        os.mkdir(a_año) #Crear carpeta con el año
    if not os.path.exists(archivo):
        os.mkdir(archivo) #Crear carpeta dentro del año y luego mes
    # print('Archivo movido \'' + str(i) + '\'')
    shutil.move(i, archivo) #Mover los archivos

  
