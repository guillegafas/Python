import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="ahorcado"
)


mycursor = mydb.cursor()
total_palabras = []
# Obtener el número total de palabras en la tabla
mycursor.execute("SELECT palabra FROM palabras")
total_palabras = mycursor.fetchall()


print(total_palabras)
print(total_palabras[1])

lista_de_caracteres = ['p', 'y', 't', 'h', 'o', 'n']

# Concatenar los caracteres para formar la palabra
palabra_completa = ''.join(lista_de_caracteres)

# Imprimir la palabra completa
print("Palabra completa:", palabra_completa)