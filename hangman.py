import random

Word = ["cat", "dog", "pig", "ant", "ape", "ass", "bat", "bee", "cow", "fox"]
Word_random = random.choice(Word)

def hangman(word):
    wrong = -1
    stages = ["",
              "_________         ",
              "|                 ",
              "|        |        ",
              "|        0        ",
              "|       /|\       ",
              "|       / \       ",
              "|                 ",
              ]
    
    rletters = list(word)
    board = ["_"] * len(word)
    win = False
    print("ハングマンへようこそ!")
    while wrong < len(stages):
        print("\n")
        msg = "1文字を予想してね: "
        char = input(msg)
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print(" ".join(board))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "_" not in board:
            print("あなたの勝ち")
            print(" ".join(board))
            win = True
            break
    if not win:
        print("\n")
        print("\n".join(stages[0:wrong+1]))
        print("\nあなたの負け!正解は{}.".format(word))


hangman(Word_random)

