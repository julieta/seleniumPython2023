#imprimir
print ('Hola Mundo')

Nombre = 'Udemy'  #formateo de string
print (f'Hola {Nombre}')

#----Lista---------

array = ['Venezuela', 'Argentina', 'Chile', 'Perú']
print(array[0])
array.append('Bolivia') #para agregar elemento al array
print(array)

i=0
for pais in array:
    if pais== "Argentina":
        print(pais)
        print(f'{Nombre}, vive en {pais}')
        #break # rompe le look
        continue #continua con el proceso
    if pais== "Bolivia":
        print(f'{Nombre}, vive en {pais}')
        break
    i++1


#----Diccionarios--------- tiene un elemento y un valor

diccionario= {'nombreInvitado' : 'Carlos', 'edad' : 22, 'cursos' : ['Python', 'JS'] }
print(diccionario)


















































