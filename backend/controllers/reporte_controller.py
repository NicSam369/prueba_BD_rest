import io
import csv
from flask import request, Response
from services.reporte_services import obtener_reporte_categorias


def reporte_categorias():
    formato = request.args.get("formato")
    datos = obtener_reporte_categorias()

    if formato == "csv":
        output = io.StringIO()
        writer = csv.writer(output)
        writer.writerow(["categoria", "producto", "num_pedidos", "total_unidades", "ingreso_total"])
        for fila in datos:
            writer.writerow([
                fila["categoria"],
                fila["producto"],
                fila["num_pedidos"],
                fila["total_unidades"],
                fila["ingreso_total"]
            ])

        return Response(
            output.getvalue(),
            mimetype="text/csv",
            headers={"Content-Disposition": "attachment; filename=reporte_categorias.csv"}
        )

    return {
        "estado": "OK",
        "data": datos
    }
