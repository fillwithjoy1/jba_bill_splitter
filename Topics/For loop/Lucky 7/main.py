number_n = int(input())

for _ in range(number_n):
    read_input = int(input())
    if read_input / 7 == read_input // 7:
        print(pow(read_input, 2))