import csv

file = open('input.txt')
my_list = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

my_list[1] = 12
my_list[2] = 2

pc = 0
while my_list[pc] != 99:
    print(my_list[pc:pc+4])
    opcode = my_list[pc]
    param1 = my_list[my_list[pc + 1]]
    param2 = my_list[my_list[pc + 2]]
    dest = my_list[pc + 3]

    if opcode == 1:
        my_list[dest] = param1 + param2
        print("Store " + str(param1) + " + " + str(param2) + " at " + str(dest))
    elif opcode == 2:
        my_list[dest] = param1 * param2
        print("Store " + str(param1) + " * " + str(param2) + " at " + str(dest))
    else:
        break

    print(my_list)
    pc += 4

print(pc)
print(len(my_list))
print(my_list)
