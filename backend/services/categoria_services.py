from database import get_connection

def obtener_categorias():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_categoria,
               nombre,
               descripcion
        FROM categoria
        ORDER BY id_categoria;
    """)

    categorias = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for categoria in categorias:
        resultado.append({
            "id_categoria": categoria[0],
            "nombre": categoria[1],
            "descripcion": categoria[2]
        })

    return resultado

def obtener_categoria_por_id(id_categoria):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_categoria,
               nombre,
               descripcion
        FROM categoria
        WHERE id_categoria = %s;
    """, (id_categoria,))

    categoria = cursor.fetchone()

    cursor.close()
    conexion.close()

    if categoria is None:
        return {
            "estado": "ERROR",
            "mensaje": "Categoria no encontrada"
        }

    return {
        "id_categoria": categoria[0],
            "nombre": categoria[1],
            "descripcion": categoria[2]
    }

def crear_categoria(nombre, descripcion):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO categoria
        (nombre, descripcion)
        VALUES (%s, %s)
        RETURNING id_categoria;
    """, (nombre, descripcion))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Categoria creada correctamente",
        "id_categoria": nuevo_id
    }

def actualizar_categoria(id_categoria, nombre, descripcion):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE categoria
        SET nombre = %s,
            descripcion = %s
        WHERE id_categoria = %s;
    """, (nombre, descripcion, id_categoria))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Categoria no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Categoria actualizada correctamente"
    }

def eliminar_categoria(id_categoria):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM categoria
        WHERE id_categoria = %s;
    """, (id_categoria,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Categoria no encontrada"
        }

    return {
        "estado": "OK",
        "mensaje": "Categoria eliminada correctamente"
    }