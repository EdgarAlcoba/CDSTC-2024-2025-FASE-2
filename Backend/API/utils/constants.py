import os

def init_sustainability(constants: dict[str,any]):
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

def init_jwt(constants: dict[str,any]) -> any:
    jwt_secret_key = os.environ.get(
        "JWT_SECRET_KEY",
        "53aac3bcc5ef7f3596ddbbd3aef2f8b01a776a6ca9c0b5e7e8e69a1feb5ac88a"
    )
    if len(jwt_secret_key) != 64:
        raise RuntimeError("JWT_SECRET_KEY must be 64 characters long. You can generate one using the command (openssl rand -hex 32)")
    constants["JWT_SECRET_KEY"] = jwt_secret_key

    jwt_algorithm = os.environ.get("JWT_ALGORITHM", "HS256")
    jwt_supported_algorithms = ["HS256", "HS384", "HS512", "ES256", "ES256K", "ES384", "ES512",
                                "RS256", "RS384", "RS512", "PS256", "PS384", "PS512"]
    if jwt_algorithm not in jwt_supported_algorithms:
        raise RuntimeError(f"JWT_ALGORITHM is not supported. Supported algorithms are {jwt_supported_algorithms}")
    constants["JWT_ALGORITHM"] = jwt_algorithm

    jwt_expire_minutes = os.environ.get("JWT_EXPIRE_MINUTES", 1440)
    jwt_expire_minutes_int: int
    try:
        jwt_expire_minutes_int = int(jwt_expire_minutes)
        if jwt_expire_minutes_int < 0:
            raise ValueError
        constants["JWT_EXPIRE_MINUTES"] = jwt_expire_minutes_int
    except ValueError:
        raise RuntimeError("JWT_EXPIRE_MINUTES must be a positive integer")

def init_superadmin(constants: dict[str,any]) -> any:
    superadmin_email = os.environ.get("SUPERADMIN_EMAIL", "superadmin")
    if len(superadmin_email) < 1:
        raise RuntimeError("SUPERADMIN_EMAIL cannot be empty")
    constants["SUPERADMIN_EMAIL"] = superadmin_email

    superadmin_password = os.environ.get("SUPERADMIN_PASSWORD", "0000")
    if len(superadmin_password) < 1:
        raise RuntimeError("SUPERADMIN_PASSWORD cannot be empty")
    constants["SUPERADMIN_PASSWORD"] = superadmin_password

def init_ai(constants: dict[str,any]):
    ai_batch_size = os.environ.get("AI_BATCH_SIZE", 1000)
    try:
        ai_batch_size = int(ai_batch_size)
        if ai_batch_size < 1:
            raise ValueError
    except ValueError:
        raise RuntimeError("AI_BATCH_SIZE must be a positive integer")
    constants["AI_BATCH_SIZE"] = ai_batch_size

def init() -> dict[str, any]:
    constants = {}
    init_sustainability(constants)
    init_jwt(constants)
    init_superadmin(constants)
    init_ai(constants)
    return constants





