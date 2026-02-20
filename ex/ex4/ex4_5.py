nums = []
while True:
    num = input("整数を入力してください")
    if int(num) == 0:
        break
    else:
        nums.append(int(num)) 

print(sum(nums)/len(nums))