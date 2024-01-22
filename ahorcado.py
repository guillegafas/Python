import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ahorcado"
)


mycursor = mydb.cursor()

# Obtener el número total de palabras en la tabla
mycursor.execute("SELECT palabra FROM palabras")
total_palabras = mycursor.fetchall()

print(total_palabras)




print('Bienvenido al ahorcado')
z = int(input('Dime del 1-5 que juego quieres jugar'))
print(total_palabras[z])
f = str(total_palabras[z])
print(f)
palabra = []
intento = []
for caracter in f:
    palabra.append(caracter)
print
for i in range(len(palabra)):
    intento.append(' ')
print(intento)
while palabra != intento: 
    l = input('introduce una letra ')
    num = 0
    for i in range(len(palabra)):
        if palabra[i] == l:
            intento[i] = l
    if l not in palabra:
        print('letra incorrecta')
    print(intento)
print('Game over')