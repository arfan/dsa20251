
def check_pass(p):
    if p=='zzzz':
        print("password correct")
        return True

found = False
for c1num in range(ord('a'), ord('z')+1):
    if found:
        break
    c1 = chr(c1num)

    for c2num in range(ord('a'), ord('z')+1):
        if found:
            break
        c2 = chr(c2num)

        for c3num in range(ord('a'), ord('z')+1):
            if found:
                break
            c3 = chr(c3num)
        
            for c4num in range(ord('a'), ord('z')+1):
                c4 = chr(c4num)

                guess = c1+c2+c3+c4

                print(guess)

                if check_pass(guess):
                    print("password is:", guess)
                    found = True
                    break
