def simple_assembler(program):
    registers = {}
    
    def parser(program):
        array = []
        for line in program:
            array.append(line.split(" "))
        for instruction in array:
            if instruction[1].isdigit():
                instruction[1] = int(instruction[1])
            if len(instruction) > 2 :
                instruction[2] = int(instruction[2])
        return array
    array = parser(program)
    pointer = 0
    
    while pointer < len(array):
        if array[pointer][0] == "mov":
            if isinstance(array[pointer][2], int):
                registers[array[pointer][1]] = array[pointer][2]
            else: registers[array[pointer][1]] = registers[array[pointer][2]]
            print(f"instruction{array[pointer]}executed correctly with pointer value of {pointer}")
            pointer+=1
        elif array[pointer][0] == "inc":
            registers[array[pointer][1]]+=1
            print(f"instruction{array[pointer]}executed correctly with pointer value of {pointer}")
            pointer+=1
        elif array[pointer][0]=="dec":
            registers[array[pointer][1]]-=1
            print(f"instruction{array[pointer]}executed correctly with pointer value of {pointer}")
            pointer+=1
        elif array[pointer][0]=="jnz":
            if array[pointer][1] in registers and registers[array[pointer][1]]!= 0 and isinstance(array[pointer][1],int) and array[pointer][1]!=0:
                print(f"instruction{array[pointer]}executed correctly with pointer value of {pointer}")
                pointer+=int(array[pointer][2])

            else: pointer+=1
        else: pointer+=1
    return print(registers)
    

simple_assembler(['mov a 5','inc a', 'mov b 56','jnz 0 2', 'dec a','dec a','jnz a -1','inc a'])