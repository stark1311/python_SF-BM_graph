import matplotlib.pyplot as plt

def calculate_shear_force_and_bending_moment(length, udl):
    # Calculate reactions at supports
    reaction = udl * length / 2

    # Initialize lists for shear force and bending moment
    shear_force = []
    bending_moment = []

    # Calculate shear force and bending moment at each point along the beam
    for x in range(length + 1):
        distance_from_support = x
        v = reaction - udl * distance_from_support
        m = reaction * distance_from_support - (udl * distance_from_support ** 2) / 2

        shear_force.append(v)
        bending_moment.append(m)

    return shear_force, bending_moment

def plot_diagrams(length, shear_force, bending_moment):
    # Create x-axis values
    x = list(range(length + 1))

    # Plot shear force diagram
    plt.subplot(2, 1, 1)
    plt.plot(x, shear_force, 'b-', linewidth=2)
    plt.xlabel('Distance along the beam (m)')
    plt.ylabel('Shear Force (kN)')
    plt.title('Shear Force Diagram')

    # Plot bending moment diagram
    plt.subplot(2, 1, 2)
    plt.plot(x, bending_moment, 'r-', linewidth=2)
    plt.xlabel('Distance along the beam (m)')
    plt.ylabel('Bending Moment (kNm)')
    plt.title('Bending Moment Diagram')

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()

# Example usage
length_of_beam = int(input("Enter the length of the beam (in meters): "))
udl_value = int(input("Enter the value of the uniformly distributed load (in kN/m): "))

shear_force_values, bending_moment_values = calculate_shear_force_and_bending_moment(length_of_beam, udl_value)

plot_diagrams(length_of_beam, shear_force_values, bending_moment_values)
