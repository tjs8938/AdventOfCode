def exp(x, y):
    return int((((x + y - 2) * (x + y - 1)) / 2) + x - 1)


code = 20151125
iterations = exp(3029, 2947)
for i in range(iterations):
    code = (code * 252533) % 33554393

print(code)
