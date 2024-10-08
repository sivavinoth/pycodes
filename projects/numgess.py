import random


def numguess():
    ans = random.randint(1, 6)
    mxl = 3
    c = 0

    while (
        c < mxl
    ):  # this while loop runs until conditon is true that is c less than mxl
        print("guess number btn 1 to 6")
        print(f"++++++++++ total {mxl} now you have { mxl - c} remaining ++++++++++")
        user_in = int(input("Enter the no :"))

        if user_in == ans:
            print(f" right guess {user_in}")
            break
        if user_in > ans:
            print(f"guess is high {user_in}")
        else:
            print(f"the guess is low {user_in}")

        c += 1

    if c == mxl and user_in != ans:
        print("- your out of guess -")


numguess()
