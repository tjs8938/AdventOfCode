import csv
import math

input_file = open("input.txt")
input = input_file.read().splitlines()[0]

image = list(input[:150])

for i in range(0, 150):
    layer = 1
    while image[i] == '2':
        image[i] = input[layer*150 + i]
        layer += 1


for i in range(0, 6):
    print("".join(image[25*i:25*(i+1)]).replace('0', ' '))
