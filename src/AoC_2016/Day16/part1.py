
seed: str = "00101000101111010"


def checksum_for_data_size(data_size):
    a = seed
    while len(a) < data_size:
        b = ""
        for c in a[::-1]:
            b += ('1' if c == '0' else '0')
        a = a + '0' + b
    a = a[:data_size]
    block_size = 1
    block_count = len(a)
    while block_count % 2 == 0:
        block_count = block_count >> 1
        block_size = block_size << 1
    checksum = ""
    for i in range(block_count):
        block = a[i * block_size:(i + 1) * block_size]
        if block.count('1') % 2 == 0:
            checksum += '1'
        else:
            checksum += '0'
    return checksum


print(checksum_for_data_size(272))
print(checksum_for_data_size(35651584))
