from enum import Enum, auto


class RideStatus(Enum):
    RUNNING = auto()
    E_STOPPED = auto()
    CASCADED = auto()


class VehicleState(Enum):
    WAITING = auto()
    LOADING = auto()
    READY_TO_DISPATCH = auto()
    MOVING = auto()
    STOPPED = auto()
    RETURNING = auto()

class Zone(Enum):
    DISPATCH = auto()
    READY = auto()
    LOAD = auto()
    UNLOAD = auto()
    HOLD_1 = auto()
    HOLD_2 = auto()
    ZONE_1= auto()
    ZONE_2 = auto()
    ZONE_3 = auto()
    ZONE_4 = auto()
    ZONE_5 = auto()
    ZONE_6 = auto()
    ZONE_7 = auto()
    ZONE_8 = auto()
    ZONE_9 = auto()
    ZONE_10 = auto()
    ZONE_11 = auto()
    ZONE_12 = auto()
    ZONE_13 = auto()
    ZONE_14 = auto()
    ZONE_15 = auto()