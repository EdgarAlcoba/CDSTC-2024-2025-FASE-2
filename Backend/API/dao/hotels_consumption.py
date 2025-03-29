from sqlmodel import select
from sqlalchemy import func

from ..dto import hotel_consumption
from ..utils.constants import init as get_constants
from ..utils.db import get_session
from ..dto.hotel_consumption import HotelConsumption

class HotelsConsumption:
    @staticmethod
    def calculate_sustainability_percent(
        energy_kwh: int, waste_kg: int,
        recycle_percent: float, water_usage_m3: int,
        energy_kwh_max: int, waste_kg_max: int, water_usage_m3_max: int) -> float:
        constants = get_constants()

        energy_converted: float = energy_kwh/energy_kwh_max
        waste_kg_converted: float = waste_kg/waste_kg_max
        water_usage_m3_converted: float = water_usage_m3/water_usage_m3_max
        recycle_percent_converted: float = 1 - (recycle_percent/100)

        sustainability_percent: float = 100 - (
            (constants['SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE'] * energy_converted) +
            (constants['SUSTAINABILITY_INDEX_WASTE_IMPORTANCE'] * waste_kg_converted) +
            (constants['SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE'] * recycle_percent_converted) +
            (constants['SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE'] * water_usage_m3_converted)
        ) * 100

        return sustainability_percent

    @staticmethod
    def generate_sustainability_indexes():
        # Obtain maximum values
        session = next(get_session())
        query_get_maximums = select(
            func.max(HotelConsumption.energy_kwh),
            func.max(HotelConsumption.waste_kg),
            func.max(HotelConsumption.water_usage_m3)
        )
        maximums_result = session.execute(query_get_maximums).first()
        if len(maximums_result) < 1:
            raise RuntimeWarning('Tried to generate hotels consumption with no hotels consumption data')
        energy_kwh_max = maximums_result[0]
        waste_kg_max = maximums_result[1]
        water_usage_m3_max = maximums_result[2]

        # Get hotels consumptions to compute their indexes
        db_hotels_consumption: list[HotelConsumption] = session.scalars(select(HotelConsumption)).all()

        for db_hotel_consumption in db_hotels_consumption:
            db_hotel_consumption.sustainability_percent = \
                HotelsConsumption.calculate_sustainability_percent(
                    db_hotel_consumption.energy_kwh, db_hotel_consumption.waste_kg,
                    db_hotel_consumption.recycle_percent, db_hotel_consumption.water_usage_m3,
                    energy_kwh_max, waste_kg_max, water_usage_m3_max
                )
        session.commit()