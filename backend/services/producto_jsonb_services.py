from database import get_connection


def obtener_productos_jsonb(filtro=None, valor=None):
    conexion = get_connection()
    cursor = conexion.cursor()

    base_query = """
        SELECT
            p.nombre,
            c.nombre AS categoria,
            p.precio,
            p.datos_extra ->> 'nivel_picante'             AS picante,
            p.datos_extra -> 'nutricion' ->> 'calorias'   AS calorias,
            p.datos_extra -> 'etiquetas'                   AS etiquetas
        FROM producto p
        LEFT JOIN categoria c ON c.id_categoria = p.id_categoria
        WHERE p.datos_extra IS NOT NULL
    """

    params = []

    if filtro == "sin_gluten":
        # etiqueta exacta "sin gluten"
        base_query += " AND p.datos_extra -> 'etiquetas' ? 'sin gluten'"

    elif filtro == "etiqueta" and valor:
        base_query += " AND p.datos_extra -> 'etiquetas' ? %s"
        params.append(valor)

    elif filtro == "alergeno" and valor:
        # el frontend manda 'lacteos' pero los datos usan 'leche', buscamos los dos
        buscar = "leche" if valor in ("lacteos", "leche") else valor
        base_query += " AND p.datos_extra -> 'alergenos' ? %s"
        params.append(buscar)

    elif filtro == "picante" and valor:
        base_query += " AND p.datos_extra ->> 'nivel_picante' = %s"
        params.append(valor)

    elif filtro == "rapidos":
        # filtra productos cuyo tiempo_preparacion en JSONB es <= 15
        # si no tienen ese campo simplemente no aparecen
        base_query += " AND (p.datos_extra ->> 'tiempo_preparacion')::int <= 15"

    base_query += " ORDER BY p.nombre;"

    cursor.execute(base_query, params)
    filas = cursor.fetchall()
    cursor.close()
    conexion.close()

    resultado = []
    for fila in filas:
        resultado.append({
            "nombre":    fila[0],
            "categoria": fila[1],
            "precio":    float(fila[2]) if fila[2] is not None else None,
            "picante":   fila[3],
            "calorias":  fila[4],
            "etiquetas": fila[5] if fila[5] else []
        })

    return {"data": resultado}
