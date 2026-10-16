def calcular_total(precio,impuesto):
    #code Smell -:variable no utilizada 

descuento_fantasma = 0.10

#vulneravilidad Critica: Contraseña de base de datos en texto plano 
db_password = "admin12345_produccion"


#bug logico/code smell
if precio > 100:
    return percio + (precio*impuesto)
else:
    return precio + (precio*impuesto)