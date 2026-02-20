shohin_list = {}

def add_shohin(): 
    name = input("商品名を入力してください:")
    if name in shohin_list:
        print("その商品は登録済みです")
        return

    zaiko = int(input("在庫数を入力してください:"))
    if zaiko < 0:
        print("正の整数で入力してください")
        return

    shohin_list[name] = zaiko
    print("商品が追加されました")

def update_stock():
    name = input("商品名を入力してください：") 
    if name not in shohin_list:
        print("その商品は登録されていません")
        return

    change = int(input("増減数を入力してください。(減る場合、負の整数で入力)："))

    if shohin_list[name] + change < 0:
        print("在庫数が０以下となるため更新できません")
        return
    else:
        shohin_list[name] += change
        print(f"{name}の在庫数を{shohin_list[name]}個に更新しました")

def print_list():
    if not shohin_list:
        print("在庫がありません")
        return

    for name, zaiko in shohin_list.items():
        print(f"{name}：{zaiko}")
        return

def dead_stock():
    out = []
    
    for name, zaiko in shohin_list.items():
        if zaiko == 0:
            out.append(name)

    if not out:
        print("在庫切れの商品はありません")
        return
    else:
        print("【在庫切れの商品】")
        for name in out:
            print(name)
    

def main():
    while True:
        print("--- 在庫管理システム ---")
        print("1. 商品の追加")
        print("2. 商品の在庫数の更新")
        print("3. 在庫一覧の表示")
        print("4. 在庫切れ商品の表示")
        print("5. プログラムの終了")
        
        choice = input("番号を選択してください")

        if choice == "1":
            add_shohin()
        elif choice == "2":
            update_stock()
        elif choice == "3":
            print_list()
        elif choice == "4":
            dead_stock()
        elif choice == "5":
            print("プログラムを終了します")
            break
        else:
            print("入力形式が異なります。")

main()