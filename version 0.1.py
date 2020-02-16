def simple_assembler(program):
    registers = {}
    array = []
    for line in program:
        array.append(line.split(" "))
    pointer = 0
    while pointer < len(array):
    
        if array[pointer][0] == "mov" and array[pointer][2].isnumeric():
            registers[array[pointer][1]] = int(array[pointer][2])
            pointer+=1
        elif array[pointer][0] == "mov" and array[pointer][2].isalpha():
            registers[array[pointer][1]] = registers[array[pointer][2]]
            pointer+=1
        elif array[pointer][0] == "inc":
            registers[array[pointer][1]]+=1
            pointer+=1
        elif array[pointer][0]=="dec":
            registers[array[pointer][1]]-=1
            pointer+=1
        elif array[pointer][0]=="jnz" and registers[array[pointer][1]] !=0:
            pointer+=int(array[pointer][2])
        else: pointer+=1
    return registers