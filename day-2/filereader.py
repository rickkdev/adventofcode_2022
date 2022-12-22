def initArrayFromFile():
    with open('input.txt', 'r') as f:
   
        lines = f.readlines()

    array = []
    temp = []

    for line in lines:

        line = line.strip()
        array.append(line)
        
    f.close()

    return array