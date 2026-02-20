def get_min(num1, num2):
    if num1 > num2:
        return num2
    else:
        return num1

num1 = int(input("自然数一つ目を入力："))
num2 = int(input("自然数二つ目を入力："))

print(f"小さい方は{get_min(num1, num2)}です。")

def get_gcd(num1, num2):
    max_num = get_min(num1, num2)
    for i in range(2, max_num):
        if num1 % i == 0 and num2 % i == 0:
            koyaku = i
    return koyaku

print(f"最大公約数は{get_gcd(num1, num2)}です。")
