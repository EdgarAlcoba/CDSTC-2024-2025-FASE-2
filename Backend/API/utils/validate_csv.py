from fastapi import UploadFile, HTTPException
from datetime import date, datetime

def validate_all_csv_exist(files: list[UploadFile]) -> dict[str, UploadFile]:
    num_files: int = len(files)
    valid_files: dict[str, UploadFile] = {}

    for i in range(num_files):
        filename = files[i].filename

        if filename == 'datos_sostenibilidad.csv':
            valid_files['datos_sostenibilidad'] = files[i]
            continue

        if filename == 'ocupacion_hotelera.csv':
            valid_files['ocupacion_hotelera'] = files[i]
            continue

        if filename == 'opiniones_turisticas.csv':
            valid_files['opiniones_turisticas'] = files[i]
            continue

        if filename == 'rutas_turisticas.csv':
            valid_files['rutas_turisticas'] = files[i]
            continue

        if filename == 'uso_transporte.csv':
            valid_files['uso_transporte'] = files[i]
            continue

    if valid_files.get('datos_sostenibilidad') is None:
        raise HTTPException(status_code=400, detail="datos_sostenibilidad.csv file is missing")

    if valid_files.get('ocupacion_hotelera') is None:
        raise HTTPException(status_code=400, detail="ocupacion_hotelera.csv file is missing")

    if valid_files.get('opiniones_turisticas') is None:
        raise HTTPException(status_code=400, detail="opiniones_turisticas.csv file is missing")

    if valid_files.get('rutas_turisticas') is None:
        raise HTTPException(status_code=400, detail="rutas_turisticas.csv file is missing")

    if valid_files.get('uso_transporte') is None:
        raise HTTPException(status_code=400, detail="uso_transporte.csv file is missing")

    return valid_files

def validate_datos_sostenibilidad(row: str, row_num: int):
    filename: str = "datos_sostenibilidad.csv"
    csv_hotel_name: str = row["hotel_nombre"]
    if len(csv_hotel_name) == 0:
        raise HTTPException(status_code=400, detail=f"{filename} has an empty hotel name in row {row_num}")
    csv_hotel_date: date
    try:
        csv_hotel_date = datetime.strptime(row["fecha"], '%Y-%m-%d').date()
    except ValueError:
        # Quirk to remove lefover d mistake in a row
        if row["fecha"].endswith("d"):
            csv_hotel_date = datetime.strptime(row["fecha"][:-1], "%Y-%m-%d").date()
        else:
            raise HTTPException(status_code=400, detail=f"{filename} has an invalid date value in row {row_num}, must be in format YYYY-MM-DD")
    csv_hotel_power_kwh: int
    try:
        csv_hotel_power_kwh = int(row["consumo_energia_kwh"])
    except ValueError:
        raise HTTPException(status_code=400,
                            detail=f"{filename} has an invalid power usage value in row {row_num}, must be an integer")
    csv_hotel_generated_waste: int
    try:
        csv_hotel_generated_waste = int(row["residuos_generados_kg"])
    except ValueError:
        raise HTTPException(status_code=400,
                            detail=f"{filename} has an invalid generated waste value in row {row_num}, must be an integer")
    csv_hotel_recycle_percent: float
    try:
        csv_hotel_recycle_percent = float(row["porcentaje_reciclaje"])
        if csv_hotel_recycle_percent > 100 or csv_hotel_recycle_percent < 0:
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid hotel recycle percent value in row {row_num}, must be a float [0-100]"
        )
    csv_hotel_water_usage: int
    try:
        csv_hotel_water_usage = int(row["uso_agua_m3"])
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid water usage value in row {row_num}, must be a float [0-100]"
        )

    return (
        csv_hotel_name, csv_hotel_date,
        csv_hotel_generated_waste, csv_hotel_recycle_percent,
        csv_hotel_water_usage, csv_hotel_power_kwh
    )

def validate_ocupacion_hostelera(row: str, row_num: int):
    filename: str = "ocupacion_hostera.csv"
    csv_hotel_name: str = row["hotel_nombre"]
    if len(csv_hotel_name) == 0:
        raise HTTPException(status_code=400, detail=f"{filename} has an empty hotel name in row {row_num}")
    csv_occupation_on: date
    try:
        csv_occupation_on = datetime.strptime(row["fecha"], '%Y-%m-%d').date()
    except ValueError:
        # Quirk to remove lefover d mistake in a row
        if row["fecha"].endswith("d"):
            csv_occupation_on = datetime.strptime(row["fecha"][:-1], "%Y-%m-%d").date()
        else:
            raise HTTPException(status_code=400, detail=f"{filename} has an invalid date in row {row_num}, must be in format YYYY-MM-DD")
    csv_rate_percent: int
    try:
        csv_rate_percent = int(row["tasa_ocupacion"])
        if csv_rate_percent > 100 or csv_rate_percent < 0:
            raise ValueError
    except ValueError:
        raise HTTPException(status_code=400,
                            detail=f"{filename} has an invalid occupation percent in row {row_num}, must be an integer [0-100]")
    csv_confirmed_reservations: int
    try:
        csv_confirmed_reservations = int(row["reservas_confirmadas"])
    except ValueError:
        raise HTTPException(status_code=400,
                            detail=f"{filename} has an invalid confirmed reservation number in row {row_num}, must be an integer")
    csv_cancellations: int
    try:
        csv_cancellations = int(row["cancelaciones"])
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid cancellations number in row {row_num}, must be an integer"
        )
    csv_avg_night_price: int
    try:
        csv_avg_night_price = int(row["precio_promedio_noche"])
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid average night price in row {row_num}, must be a float"
        )

    return (
        csv_hotel_name, csv_occupation_on,
        csv_rate_percent, csv_confirmed_reservations,
        csv_cancellations, csv_avg_night_price
    )

def validate_opiniones_turisticas(row: str, row_num: int):
    filename: str = "opiniones_turisticas.csv"
    csv_review_date: date
    try:
        csv_review_date = datetime.strptime(str(row["fecha"]).strip(), '%Y-%m-%d').date()
    except ValueError:
        # Quirk to remove lefover d mistake in a row
        if row["fecha"].endswith("d"):
            csv_review_date = datetime.strptime(row["fecha"][:-1], "%Y-%m-%d").date()
        else:
            raise HTTPException(
                status_code=400,
                detail=f"{filename} has an invalid date value in row {row_num}, must be in format YYYY-MM-DD"
            )

    csv_service_type: str = row["tipo_servicio"]
    if len(csv_service_type) == 0:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty service type in row {row_num}"
        )

    if csv_service_type not in ["Servicio", "Hotel", "Ruta"]:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid service type in row {row_num}, must be one of [Servicio, Hotel, Ruta]"
        )

    csv_service_name: str = row["nombre_servicio"]
    if len(csv_service_name) == 0:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty service name in row {row_num}"
        )

    csv_stars: int
    try:
        csv_stars = int(row["puntuacion"])
        if csv_stars < 0 or csv_stars > 5:
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid star count value in row {row_num}, must be an integer with format [0-5]"
        )

    csv_review: str = str(row["comentario"]).replace('"', '') + str(row["idioma"]).replace('"', '')
    if len(csv_review) == 0:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty comment value in row {row_num}"
        )

    return (
        csv_review_date, csv_service_type,
        csv_service_name, csv_stars,
        csv_review
    )

def validate_rutas_turisticas(row: str, row_num: int):
    # TODO validate csv rutas turisticas
    print("")

def validate_datos_uso_transporte(row: str, row_num: int):
    filename: str = "datos_uso_transporte.csv"
    csv_transport_usage_date: date = datetime.now().date()
    try:
        csv_transport_usage_date = datetime.strptime(row["fecha"], '%Y-%m-%d').date()
    except ValueError:
        # Quirk to remove lefover d mistake in a row
        if row["fecha"].endswith("d"):
            csv_hotel_date = datetime.strptime(row["fecha"][:-1], "%Y-%m-%d").date()
        else:
            raise HTTPException(
                status_code=400,
                detail=f"{filename} has an invalid date value in row {row_num}, must be in format YYYY-MM-DD"
            )
    csv_transport_usage_type: str = row["tipo_transporte"]
    if len(csv_transport_usage_type) == 0:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty transport type value in row {row_num}"
        )
    csv_transport_usage_num_users: int
    try:
        csv_transport_usage_num_users = int(row["num_usuarios"])
        if csv_transport_usage_num_users < 0:
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid user count value in row {row_num}, must be a positive integer"
        )
    csv_transport_usage_avg_trip_time: int
    try:
        csv_transport_usage_avg_trip_time = int(row["num_usuarios"])
        if csv_transport_usage_avg_trip_time < 0:
            raise ValueError
    except ValueError:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid average trip time value in row {row_num}, must be a positive integer"
        )

    csv_transport_usage_popular_route: str = row["ruta_popular"]
    csv_transport_usage_popular_route_split = csv_transport_usage_popular_route.split("-")
    if len(csv_transport_usage_popular_route_split) < 2:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an invalid route format in row {row_num}, must be a (origin - destination) format"
        )

    csv_transport_usage_popular_route_from = csv_transport_usage_popular_route_split[0].strip()
    csv_transport_usage_popular_route_to = csv_transport_usage_popular_route_split[1].strip()

    if len(csv_transport_usage_popular_route_from) < 1:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty route origin in row {row_num}"
        )

    if len(csv_transport_usage_popular_route_to) < 1:
        raise HTTPException(
            status_code=400,
            detail=f"{filename} has an empty route destination in row {row_num}"
        )

    return (
        csv_transport_usage_date,
        csv_transport_usage_type,
        csv_transport_usage_num_users,
        csv_transport_usage_avg_trip_time,
        csv_transport_usage_popular_route_from,
        csv_transport_usage_popular_route_to
    )