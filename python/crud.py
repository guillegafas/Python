import mysql.connector
import hashlib

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="usuarios1"
)

#creamos usuario
def crear_usuario():
    usuario = input("nombre de usuario: ")
    contrasena = input("contraseña: ")
    # generamos hash
    contrasena_haseada = str(hashlib.sha256(contrasena.encode()).hexdigest())
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO usuarios (nombre, pass) VALUES (%s, %s)", (usuario, contrasena_haseada))
    mydb.commit()
    print("Se ha creado el usuario")

#borramos usuario
def borrar_usuario():
    mycursor = mydb.cursor()
    mycursor.execute("DELETE FROM usuarios WHERE id = %s", (id_usuario,))
    mydb.commit()
    print("Usuario borrado")

def ingresar_usuario():
    usuario = input("nombre de usuario ")
    contrasena = input("Contraseña: ")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM usuarios WHERE nombre = %s", (usuario,))
    tabla = mycursor.fetchone()
# ahora en el if le decimos (if tabla) es como decirle que me valide que existe esa fila en la tabla, seria equivalente a esto: tabla[1] == usuario y que el id exista
    if tabla and tabla[2] == hashlib.sha256(contrasena.encode()).hexdigest():
 
        print("Usuario ", tabla[1], "ingresado")
    else:+
        print("Nombre de usuario o contraseña incorrectos")
    mydb.commit()

print("Bienvenido")
print("¿Que deseas hacer?")
print("1. Crear usuario")
print("2. Iniciar usuario")
print("3. Eliminar usuario")

eleccion = int(input("elige una opcion "))
if eleccion == 1:
        crear_usuario()
elif eleccion == 2:
        ingresar_usuario()
elif eleccion == 3:
        id_usuario = input("Ingresa tu ID de usuario: ")
        borrar_usuario()
else:
        print("Mete un numero correcto")