import mysql.connector
from mysql.connector import Error
import pandas as pd
def conectar():
    '''
    
    establece la conexion a la bd biblioteca
    '''

    try:
        conexion = mysql.connector.connect(
            host = "localhost",
            database = "biblioteca",
            user = "root"
            #password=""
        )
    except mysql.connector.Error as e:
        print(f"Hubo un error al conectar a la BD {e}")
    else:
        if conexion.is_connected():
            return conexion
        return None
class autor:
    def __init__(self, name_autor,seudonimo_autor,codigo_pais,fecha_nac,fecha_def,biografia_autor,foto_autor):
        self.name_autor = name_autor
        self.seudonimo_autor = seudonimo_autor
        self.fecha_nac = fecha_nac
        self.fecha_def = fecha_def
        self.biografia_autor = biografia_autor
        self.foto_autor = foto_autor
        self.codigo_pais = codigo_pais


    def crear(self):
        """
        insertar el autor en la BD
        """
        try:
            conn = conectar()
            if conn is not None:
                cursor = conn.cursor()
                sql = "INSERT INTO autor (nombre_autor, seudonimo_autor, codigo_pais, fecha_nac, fecha_def, biografia_autor, foto_autor) values (%s, %s, %s, %s, %s, %s, %s)"
                valores = (self.nombre_autor, self.seudonimo_autor, self.codigo_pais, self.fecha_nac, self.fecha_def, self.biografia_autor, self.foto_autor)
                cursor.execute(sql, valores)
                conn.commit()
                print("autor agregada correctamente")
                cursor.close()
                conn.close()
        except Error as e:
            print(F"Eror al insertar autor {e}")
    
    def leer(self):
        """
        leer los autores de la BD biblioteca
        """
        try:
            conn = conectar()
            if conn is not None:
                cursor = conn.cursor()
                sql = "SELECT *FROM  autor"
                cursor.execute(sql) 
                resultados = cursor.fetchall()  # Obtiene todos los resultados
            for autor in resultados:
                datos = pd.read_sql(sql,conn)
                print(datos)
                cursor.close()  # Cierra el cursor
                conn.close()  # Cierra la conexión
        except Error as e:
            print(f"Error al leer autores {e}")  

    def mostrar_datos(self):
        """Mostrar autores de la BD en formato tabla"""
        try:
            conn = conectar()  # Conecta a la base de datos
            if conn is not None:
                sql = "SELECT * FROM autor"
                datos = pd.read_sql(sql, conn)  # Usa pandas para leer la consulta SQL en un DataFrame
                print(datos)  # Muestra el DataFrame
                conn.close()  # Cierra la conexión
        except Error as e:
            print(f"Error al mostrar datos {e}")


#programa principal

nombre = input("Ingrese un nombre: ")
seudonimo = input("Ingrese seudonimo: ")  
codigo = input("Ingrese codigo del pais: ")  
nacimineto = input("Ingrese fecha nacimiento: ")  
defuncion = input("Ingrese fecha defuncion: ")  
biografia = input("Ingrese biografia: ")  
foto = input("Ingrese foto: ")  
