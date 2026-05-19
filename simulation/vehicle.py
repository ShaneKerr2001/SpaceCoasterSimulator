from simulation.enums import VehicleState


class Vehicle:
    def __init__(self, vehicle_id):
        self.vehicle_id = vehicle_id
        self.state = VehicleState.WAITING_IN_STATION
        self.position = 0
        self.loaded = False
        self.restraints_checked = False

    def load_guests(self):
        self.loaded = True
        self.state = VehicleState.LOADING

    def check_restraints(self):
        if self.loaded:
            self.restraints_checked = True
            self.state = VehicleState.READY_TO_DISPATCH

    def dispatch(self):
        if self.state == VehicleState.READY_TO_DISPATCH:
            self.state = VehicleState.ON_TRACK
            self.position = 1
            return True

        return False