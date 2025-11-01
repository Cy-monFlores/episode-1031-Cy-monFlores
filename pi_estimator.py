import sys

total_darts = 9
if len(sys.argv) > 1:
    total_darts = int(sys.argv[1])

print(f"we will throw {total_darts} overall")