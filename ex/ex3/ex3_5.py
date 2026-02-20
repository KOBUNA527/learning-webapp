year = input("西暦年を入力してください")

if int(year) % 4 == 0:
    if int(year) % 100 == 0 and int(year) % 400 != 0:
        print("うるう年ではありません")
    else:
        print("うるう年です")