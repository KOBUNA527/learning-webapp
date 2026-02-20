import random

def get_cpu_choice():
    jan_list = ["グー", "チョキ", "パー"]
    return random.choice(jan_list)

def determine_winner(choice1, choice2):
    if choice1 == choice2:
        return "あいこ"
    elif (
        (choice1 == "グー" and choice2 == "チョキ")
        or (choice1 == "チョキ" and choice2 == "パー")
        or (choice1 == "パー" and choice2 == "グー")
    ):
        return "あなた"
    else:
        return "CPU" 

you_win = 0
cpu_win = 0 

while True:
    you_choice = input("「グー」「チョキ」「パー」で入力してください。")
    cpu_choice = get_cpu_choice()

    if you_choice not in ["グー", "チョキ", "パー"]:
        print("入力形式が異なります。")
    else:
        print(f"あなたが入力したのは{you_choice}です。")
        print(f"CPUが入力したのは{cpu_choice}です。")
        winner = determine_winner(you_choice, cpu_choice)

        if winner == "あいこ":
            print("あいこです。") 
        elif winner == "あなた":
            you_win += 1
            print(f"{winner}の勝ちです。")
            print(f"勝利数　あなた：{you_win}回　CPU:{cpu_win}回")
        else:
            cpu_win += 1
            print(f"{winner}の勝ちです。")
            print(f"勝利数　あなた：{you_win}回　CPU:{cpu_win}回")

    if you_win == 2:
        print(f"勝者はあなたです。")
        break
    if cpu_win == 2:
        print(f"勝者はCPUです。")
        break
