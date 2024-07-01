# HW18
import math

def calculate_sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume

# Example usage
radii = [5, 10, 12]  # You can change the radii
for r in radii:
    volume = calculate_sphere_volume(r)
    print(f"Volume of sphere with radius {r} is {volume} (HW18)")
