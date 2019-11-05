
#%%
import random


def money(prize, cash):
    if True:
        prize = prize * 2
        cash = prize + prize
        return prize, cash


questions = {
    1: [["What is justin's favorite game?"], ["A. Blazblue", "B. Roblox", "C. Tekken", "D. Pokemon"], ["D"]],
    2: [["What is mika's favorite game?"], ["A. Roblox", "B. Men of War", "C. Hearts of Iron", "D. Solitaire"], ["A"]],
    3: [["Which country made the anime 'Azure Lane'?"], ["A. China", "B. Korea", "C. Japan", "D. Taiwan"], ["A"]],
    4: [["Which is Indonesia's Second President?"],
        ["A. B.J. Habibie", "B. Soeharto", "C. Amir Syafrudin", "D. Soekarno"], ["C"]],
    5: [["Who wrote harry potter?"], ["A. Graham Maxwell"], ["B. J.J. Abrams"], ["C. JK Rowling"], ["D. AA Cummings"], ["C"]],
    6: [["Who got rejected from art school?"], ["A. Karl Marx", "B. Hitler", "C. Teddy Roosevelt", "D. Princess Diana"],
        ["B"]],
    7: [["How many times did the dutch try to take back Indo after independence?"], ["A. 1", "B. 2", "C. it was the americans who tried", "D. 3"],
        ["B"]],
    8: [["Who created the first compiler?"], ["A. Admiral Grace Hopper", "B. General Norman Schwarzkopf", "C. Robert Oppenheimer", "D. Von Braun"], ["A"]],
    9: [["Whats the famous comupter language made by IBM?"], ["A. Python", "B. B", "C. C", "D. Fortran"], ["D"]],
    10: [["Who discovered alternating current electricity?"], ["A. Von Braun", "B. Bell", "C. Edison", "D. Tesla"], ["D"]],
}

i = 0
cash = 0
prize = 250
a, b = True, True
while i <= (len(questions) + 1) // 2:
    num = random.choice(list(questions.keys()))

    Help = {"1": "50-50 lifeline", "2": "ASk friend", "": "Press any key to continue"}
    choice = input(f"{Help} \nPlease input help method: ")
    if choice == "1" and a == True:
        List = ["A", "B", "C", "D"]
        List.remove(questions[num][2][0])
        print()
        wrong = random.choices(List)
        print(f"Hint: ({questions[num][2][0]} or {wrong[0]})")
        del Help["1"]
        a = False

    elif choice == "2" and b == True:
        List = ["A", "B", "C", "D"]
        List.extend([questions[num][2][0], questions[num][2][0]])
        random.shuffle(List)
        print(f"'Hey! What's up bro, the answer is {random.choice(List)}")
        del Help["2"]
        b = False
    else:
        False

    ans = input(f"{i + 1}. {questions[num][0][0]}\n{questions[num][1]}")
    ans = ans.upper()
    if ans == questions[num][2][0]:
        prize, cash = money(prize, cash)
        print(f"Congratulation! You got {prize} and your cash is {cash}.\n>>Next, you will get {money(prize, cash)}\n")
        del questions[num]


    else:
        print("Invalid input!")
        i -= 1
        break
    i += 1

if i < (len(questions) + 1) // 2:
    print(f"Unfortunately, you finished the game until question {i} with cash amount {cash}")