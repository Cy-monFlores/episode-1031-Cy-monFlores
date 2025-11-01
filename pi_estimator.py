import sys
import random
total_darts = 9
if len(sys.argv) > 1:
    total_darts = int(sys.argv[1])

in_circle = 0
for i in range(total_darts):
    dart_x = random.random()
    dart_y = random.random()
    
    if dart_x*dart_x + dart_y*dart_y <= 1:
        in_circle += 1
print(f"in circle: {in_circle} out of {total_darts}")