import sys

total_darts = 9
if len(sys.argv) > 1:
    total_darts = int(sys.argv[1])

in_circle = 0
for i in range(total_darts):

    print(f"throwing dart#{i}")