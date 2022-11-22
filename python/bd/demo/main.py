import sqlite3

def main():
    nombre = input("Nombre de Alumno: ")

    if encuentra_alumno(nombre):
        print("Alumno encontrado!")
    else:
        print("Alumno no encontrado!")

def encuentra_alumno(nombre):
    conn = sqlite3.connect('C:\\Users\\Luise\\Desktop\\Openbc\\python\\bd\\demo\\alumnos.db')
    cursor = conn.cursor()

    query = f"select id, nombre, apellido from alumnos where nombre = '{nombre}'"
    print("Query a ejecutar ", query)

    rows = cursor.execute(query)
    data = rows.fetchone()
    print(data)

    cursor.close()
    conn.close()

    if data == None:
        return False
    
    return True

if __name__ == '__main__':
    main()