import matplotlib.pyplot as plt

def dda_line(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    slope = dy / dx if abs(dx) > abs(dy) else dx / dy  # Handle slopes > 1 and < 1

    if abs(slope) < 1:
        step_x = 1
        step_y = slope * step_x
    else:
        step_y = 1
        step_x = slope * step_y 

    x = x1
    y = y1

    points_x = [x]
    points_y = [y]

    while round(x) != x2 or round(y) != y2:
        x += step_x
        y += step_y
        points_x.append(round(x))
        points_y.append(round(y))
        print(f"({round(x)},{round(y)})")

    
    return points_x, points_y

# Example Usage
x1, y1 = 0, 0  # Start point
x2, y2 = 10, 8  # End point

x_coords, y_coords = dda_line(x1, y1, x2, y2)

plt.plot(x_coords, y_coords,marker="o",markersize="5")
plt.xlim(0, 15)  # Adjust axis limits if needed
plt.ylim(0, 15)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Drawn using DDA Algorithm')
plt.show()
