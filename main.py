from simulation.vehicle import Vehicle


def main():
    # Create a vehicle
    vehicle = Vehicle(vehicle_id=1)
    vehicle = Vehicle(vehicle_id=2)
    vehicle = Vehicle(vehicle_id=3)
    vehicle = Vehicle(vehicle_id=4)
    vehicle = Vehicle(vehicle_id=5)
    vehicle = Vehicle(vehicle_id=6)
    vehicle = Vehicle(vehicle_id=7)
    vehicle = Vehicle(vehicle_id=8)
    vehicle = Vehicle(vehicle_id=9)
    vehicle = Vehicle(vehicle_id=10)
    vehicle = Vehicle(vehicle_id=11)
    vehicle = Vehicle(vehicle_id=12)
    vehicle = Vehicle(vehicle_id=13)
    vehicle = Vehicle(vehicle_id=14)
    vehicle = Vehicle(vehicle_id=15)

    # Show initial state
    print("Initial State:", vehicle.state)

    # Load guests
    vehicle.load_guests()
    print("After Loading:", vehicle.state)

    # Check restraints
    vehicle.check_restraints()
    print("After Restraint Check:", vehicle.state)

    # Attempt dispatch
    success = vehicle.dispatch()

    if success:
        print("Vehicle dispatched!")
    else:
        print("Dispatch failed.")

    # Show final vehicle information
    print("Current State:", vehicle.state)
    print("Vehicle Position:", vehicle.position)


if __name__ == "__main__":
    main()