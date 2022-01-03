input_file = open("input.txt")
# input_file = open("test1.txt")
# input_file = open("test2.txt")

input_lines = input_file.read().splitlines()
adapters = [int(x) for x in input_lines]
adapters.append(0)
adapters.sort()

paths = [1]
for adapter in range(1, max(adapters)+1):
    path_count = 0
    for i in range(max(0, adapter - 3), adapter):
        if i in adapters:
            path_count += paths[i]
    paths.append(path_count)

print(paths[-1])
