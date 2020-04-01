def get_numeric(prompt):
    while True:
        try:
            res = float(input(prompt))
            break
        except (ValueError, NameError):
            print("Numbers only please!")
    return res


def calc_acceleration(initial_velocity, braking_time):
    return initial_velocity / braking_time


initial_velocity = get_numeric("Enter initial velocity in meters per second:")
braking_time = get_numeric("Enter braking time in seconds:")

print("Acceleration is %.2f m/s^2" % calc_acceleration(initial_velocity, braking_time))
