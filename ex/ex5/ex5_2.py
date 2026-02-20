def check_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False    
    return True

num = int(input("自然数を入力してください："))
if check_prime(num) == False:
    print("素数ではありません")
else:
    print("素数です。")