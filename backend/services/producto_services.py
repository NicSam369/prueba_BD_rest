from database import get_connection

def obtener_productos():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_producto,
               nombre,
               descripcion,
               precio,
               stock,
               id_categoria
        FROM producto
        ORDER BY id_producto;
    """)

    productos = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for producto in productos:
        resultado.append({
            "id_producto": producto[0],
            "nombre": producto[1],
            "descripcion": producto[2],
            "precio": float(producto[3]),
            "stock": producto[4],
            "id_categoria": producto[5]
        })

    return resultado

def obtener_producto_por_id(id_producto):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_producto,
               nombre,
               descripcion,
               precio,
               stock,
               id_categoria
        FROM producto
        WHERE id_producto = %s;
    """, (id_producto,))

    producto = cursor.fetchone()

    cursor.close()
    conexion.close()

    if producto is None:
        return {
            "estado": "ERROR",
            "mensaje": "Producto no encontrado"
        }

    return {
        "id_producto": producto[0],
        "nombre": producto[1],
        "descripcion": producto[2],
        "precio": float(producto[3]),
        "stock": producto[4],
        "id_categoria": producto[5]
    }

def crear_producto(nombre, descripcion, precio, stock, id_categoria):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO producto
        (nombre, descripcion, precio, stock, id_categoria)
        VALUES (%s, %s, %s, %s, %s)
        RETURNING id_producto;
    """, (nombre, descripcion, precio, stock, id_categoria))

    nuevo_id = cursor.fetchone()[0]

    conexion.commit()

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Producto creado correctamente",
        "id_producto": nuevo_id
    }

def actualizar_producto(id_producto, nombre, descripcion, precio, stock, id_categoria):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        UPDATE producto
        SET nombre = %s,
            descripcion = %s,
            precio = %s,
            stock = %s,
            id_categoria = %s
        WHERE id_producto = %s;
    """, (nombre, descripcion, precio, stock, id_categoria, id_producto))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Producto no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Producto actualizado correctamente"
    }

def eliminar_producto(id_producto):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM producto
        WHERE id_producto = %s;
    """, (id_producto,))

    conexion.commit()

    filas = cursor.rowcount

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Producto no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Producto eliminado correctamente"
    }