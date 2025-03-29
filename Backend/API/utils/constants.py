import os

def init_sustainability(constants: dict[str,any]) -> any:
    sustainability_indexes = {
        "SUSTAINABILITY_INDEX_ENERGY_IMPORTANCE": "0.40",
        "SUSTAINABILITY_INDEX_WASTE_IMPORTANCE": "0.2",
        "SUSTAINABILITY_INDEX_RECYCLING_IMPORTANCE": "0.3",
        "SUSTAINABILITY_INDEX_WATER_USAGE_IMPORTANCE": "0.1"
    }

    for key,default_value in sustainability_indexes.items():
        value = os.environ.get(key, default_value)
        try:
            return_value = float(value)
            if return_value < 0 or return_value > 1:
                raise RuntimeError
            constants[key] = return_value
        except ValueError:
            raise RuntimeError(f"{key} must be a importance percentage expressed in a float between 0 and 1. Got {value}")

    total_importance: float = 0
    for key in sustainability_indexes:
        total_importance += constants[key]
    total_importance = round(total_importance, 2)
    if total_importance < 0 or total_importance > 1:
        raise RuntimeError(f"Sustainability index importances sum must be a float between 0 and 1. Got {total_importance}")


def init() -> dict[str, any]:
    constants = {}
    init_sustainability(constants)
    return constants





