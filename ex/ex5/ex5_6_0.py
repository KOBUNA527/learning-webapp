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

cpu_choice = get_cpu_choice()
print(f"CPUの手は{cpu_choice}です。")

you_choice = input("「グー」「チョキ」「パー」で入力してください。")
if you_choice not in ["グー", "チョキ", "パー"]:
    print("入力形式が異なります。")
else:
    print(f"あなたが入力したのは{you_choice}です。")
    winner = determine_winner(you_choice, cpu_choice)
    if winner == "あいこ":
        print("あいこです。") 
    else:
        print(f"勝者は{winner}です。")