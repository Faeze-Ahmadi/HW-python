#HW5
for x in range(1, 101):
    for y in range(1, 101):
        z = (x2 + y2)**0.5
        if z.is_integer():
            print(f"x: {x}, y: {y}, z: {int(z)}")