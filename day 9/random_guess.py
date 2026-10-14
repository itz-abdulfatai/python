import random

def run_guess(user_guess, result):
    if  0 < user_guess < 11:
        if user_guess == result:
            print('you are a genius!')
            return True

    else:
        print('hey bozo, I said 1~10')
    return False

answer = random.randint(1, 10)
if __name__ == '__main__':
    while True:
        try:

            guess = int(input('guess a number 1~10: '))
            if run_guess(guess, answer):
                break
        except ValueError:
            print("please enter a number")
            continue
