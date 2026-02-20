num_max = 0

for i in range(6):
    num = input("整数を入力してください")
    if int(num) > num_max:
        num_max = int(num)

print(f"最大は{num_max}です")