with open('day1.txt', 'r') as f:
   
    lines = f.readlines()

array = []
temp = []

for line in lines:

    line = line.strip()

    if line:
        temp.append(line)
    
    else:
        array.append(temp)
        temp = []

array.append(temp)

f.close()

for inner_list in array:
    for i, item in enumerate(inner_list):
        inner_list[i] = int(item)


highest_calories = 0
highest_rows = []

for row in array:
    total_calories = sum(row)
    if len(highest_rows) < 3:
        highest_rows.append(total_calories)        
    else:
        lowestNumber = min(highest_rows)
        if total_calories > lowestNumber:
            highest_rows.remove(lowestNumber)
            highest_rows.append(total_calories)

print(sum(highest_rows))
