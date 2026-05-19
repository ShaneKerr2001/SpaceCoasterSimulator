from enum import Enum, auto


class RideStatus(Enum):
    RUNNING = auto()
    STOPPED = auto()
    DELAYED = auto()


class VehicleState(Enum):
    WAITING_IN_STATION = auto()
    LOADING = auto()
    READY_TO_DISPATCH = auto()
    ON_TRACK = auto()
    RETURNING = auto()