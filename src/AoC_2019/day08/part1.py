import csv

input_file = open("input.txt")
input = input_file.read().splitlines()[0]

layers = []

for i in range(0, len(input)):
    if i % 150 == 0:
        current_layer = [0, 0, 0]
        layers.append(current_layer)

    current_layer[int(input[i])] += 1

layers.sort(key=lambda x: x[0])
print(layers)

print(layers[0][1] * layers[0][2])