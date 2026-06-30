from database import get_connection
import psycopg2

def obtener_clientes():
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_cliente,
               nombre,
               apellido,
               email,
               dni,
               telefono,
               fecha_registro
        FROM cliente
        ORDER BY id_cliente;
    """)

    clientes = cursor.fetchall()

    cursor.close()
    conexion.close()

    resultado = []

    for cliente in clientes:
        resultado.append({
            "id_cliente": cliente[0],
            "nombre": cliente[1],
            "apellido": cliente[2],
            "email": cliente[3],
            "dni": cliente[4],
            "telefono": cliente[5],
            "fecha_registro": str(cliente[6])
        })

    return resultado

def obtener_cliente_por_id(id_cliente):
    conexion = get_connection()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id_cliente,
               nombre,
               apellido,
               email,
               dni,
               telefono,
               fecha_registro
        FROM cliente
        WHERE id_cliente = %s;
    """, (id_cliente,))

    cliente = cursor.fetchone()

    cursor.close()
    conexion.close()

    if cliente is None:
        return {
            "estado": "ERROR",
            "mensaje": "Cliente no encontrado"
        }

    return {
        "id_cliente": cliente[0],
        "nombre": cliente[1],
        "apellido": cliente[2],
        "email": cliente[3],
        "dni": cliente[4],
        "telefono": cliente[5],
        "fecha_registro": str(cliente[6])
    }

def crear_cliente(nombre, apellido, email, dni, telefono):
    conexion = get_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            INSERT INTO cliente
            (nombre, apellido, email, dni, telefono)
            VALUES (%s, %s, %s, %s, %s)
            RETURNING id_cliente;
        """, (nombre, apellido, email, dni, telefono))

        nuevo_id = cursor.fetchone()[0]
        conexion.commit()

    except psycopg2.errors.UniqueViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "Ya existe un cliente con ese email o DNI"
        }

    except psycopg2.errors.CheckViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "Uno de los valores ingresados no cumple las reglas permitidas"
        }

    except psycopg2.errors.NotNullViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "Falta completar un campo obligatorio"
        }

    except Exception as e:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": f"No se pudo crear el cliente: {str(e)}"
        }

    cursor.close()
    conexion.close()

    return {
        "estado": "OK",
        "mensaje": "Cliente creado correctamente",
        "id_cliente": nuevo_id
    }

def actualizar_cliente(id_cliente, nombre, apellido, email, dni, telefono):
    conexion = get_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            UPDATE cliente
            SET nombre = %s,
                apellido = %s,
                email = %s,
                dni = %s,
                telefono = %s
            WHERE id_cliente = %s;
        """, (nombre, apellido, email, dni, telefono, id_cliente))

        conexion.commit()
        filas = cursor.rowcount

    except psycopg2.errors.UniqueViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "Ya existe otro cliente con ese email o DNI"
        }

    except psycopg2.errors.CheckViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "Uno de los valores ingresados no cumple las reglas permitidas"
        }

    except Exception as e:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": f"No se pudo actualizar el cliente: {str(e)}"
        }

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Cliente no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Cliente actualizado correctamente"
    }

def eliminar_cliente(id_cliente):
    conexion = get_connection()
    cursor = conexion.cursor()

    try:
        cursor.execute("""
            DELETE FROM cliente
            WHERE id_cliente = %s;
        """, (id_cliente,))

        conexion.commit()
        filas = cursor.rowcount

    except psycopg2.errors.ForeignKeyViolation:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": "No se puede eliminar: el cliente tiene pedidos o reservas relacionadas"
        }

    except Exception as e:
        conexion.rollback()
        cursor.close()
        conexion.close()
        return {
            "estado": "ERROR",
            "mensaje": f"No se pudo eliminar el cliente: {str(e)}"
        }

    cursor.close()
    conexion.close()

    if filas == 0:
        return {
            "estado": "ERROR",
            "mensaje": "Cliente no encontrado"
        }

    return {
        "estado": "OK",
        "mensaje": "Cliente eliminado correctamente"
    }