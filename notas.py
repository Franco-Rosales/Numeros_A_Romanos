hola = 'Hola mundo!!!'
print(hola)

#================================================================
# Tipos de datos

# Texto (String)
a = "String"
d = """Con Comillas triples
    Podemos hacer saltos de lineas
        con las simples no se puede"""
        
# Numeros (Integer)
b = 10

# Numeros con coma (Float)
e = 9.8

# Banderas (Boolean)
c = True
f = False

#================================================================

del c # con del logramos eliminar una variable en un momento del codigo

#================================================================

nombre = input("Ingrese su nombre: ")
#Forma de concatenar variables independientemente de su tipo convirtiendolas en strings

# Concatenar con f strings
bienvenida = f"hola  {nombre}  Como estas? "
print(bienvenida)

#================================================================
# buscar un pedazo de texto en algun lado (operadores de pertenencia)
print("ola" in bienvenida)
print("Como"  not in bienvenida)

#================================================================
# Datos compuestos

# Las listas se pueden modificar 
Lista = ['franco','Rosales',21,43812238,'andres',True]
print([0]) # Nos pasa el primer elemento

# Las tuplas no se pueden modificar
Tupla = ('franco','Rosales',21,43812238,'andres',True)

# Conjunto (set), no tienen un orden fijo, y pueden cambiar o intercambiarse. (se pueden reconstruir pero no se pueden cambiar los elementos dentro de el)
set = {'franco','Rosales',21,43812238,'andres',True}
# Tampoco podemos acceder por un indice, tampoco repetir valores, pero lo podemos mostrar completo.


# Diccionario (key value) o (clave valor)
diccionario = {'nombre':'franco',
               'apellido':'Rosales',
               'edad' :21, 
               'DNI': 43812238}
print(diccionario['apellido'])
print(diccionario['nombre'])




