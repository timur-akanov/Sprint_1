s = '1h 45m,360s,25m,30m 120s,2h 60s'

total_minutes = 0
for item in s.split(','):
    time = 0
    for part in item.split():
        if part.endswith('h'):
            time += int(part[:-1]) * 60
        elif part.endswith('m'):
            time += int(part[:-1])
        elif part.endswith('s'):
            time += int(part[:-1]) // 60 
    print(time)
    total_minutes += time

print("Total minutes:", total_minutes)

