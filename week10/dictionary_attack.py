def check_pass(p):
    if p=='zzzz':
        print("password correct")
        return True


with open('dictionary.txt', 'r') as f:
    for line in f:
        guess = line.strip()

        print(guess)

        if check_pass(guess):
            print("password found:", guess)
            break