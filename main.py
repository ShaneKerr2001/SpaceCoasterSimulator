from simulation.vehicle import Vehicle


def main():
    # Create a vehicle
    vehicle = Vehicle(vehicle_id=1)

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