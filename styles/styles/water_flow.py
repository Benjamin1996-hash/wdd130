def water_column_height(tower_height, tank_height):
    """Calculate the height of the water column."""
    return tower_height + (3 * tank_height) / 4


def pressure_gain_from_water_height(height):
    """Calculate the pressure gain from water height."""
    water_density = 998.2  # kg/m^3
    gravity = 9.80665  # m/s^2
    return (water_density * gravity * height) / 1000  # Convert to kPa


def pressure_loss_from_pipe(pipe_diameter, pipe_length, friction_factor, fluid_velocity):
    """Calculate the pressure loss from pipe friction."""
    water_density = 998.2  # kg/m^3
    return (-friction_factor * pipe_length * water_density * fluid_velocity ** 2) / (2000 * pipe_diameter)  # kPa


# Example usage
if __name__ == "__main__":
    # Test values
    print("Water Column Height:", water_column_height(10, 5))  # Example input values
    print("Pressure Gain from Water Height:", pressure_gain_from_water_height(7.5))  # Example input
    print("Pressure Loss from Pipe:", pressure_loss_from_pipe(0.05, 10, 0.02, 2))  # Example input
