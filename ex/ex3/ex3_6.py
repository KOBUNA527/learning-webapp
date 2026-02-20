num1 = int(input("一つ目の整数を入力してください"))
num2 = int(input("二つ目の整数を入力してください"))
num3 = int(input("三つ目の整数を入力してください"))

if num1 > num2:
    if num1 > num3:
        print(f"一番大きい値は｛num1｝です")
    elif num1 < num3 and num2 < num3:
        print(f"一番大きい値は｛num3｝です")
    else:
        print(f"一番大きい値は｛num2｝です")