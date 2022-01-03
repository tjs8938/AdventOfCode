import csv

for i in range(0, 100):
    for j in range(0, 100):

        file = open('input.txt')
        my_list = [[int(x) for x in rec] for rec in csv.reader(file, delimiter=',')][0]

        my_list[1] = i
        my_list[2] = j

        pc = 0
        while my_list[pc] != 99:
            opcode = my_list[pc]
            param1 = my_list[my_list[pc + 1]]
            param2 = my_list[my_list[pc + 2]]
            dest = my_list[pc + 3]

            if opcode == 1:
                my_list[dest] = param1 + param2
            elif opcode == 2:
                my_list[dest] = param1 * param2
            else:
                break

            pc += 4

        if my_list[0] == 19690720:
            print(100 * i + j)
            exit(0)
