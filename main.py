def elevenController(input):
    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    check = False
    if len(input) == 11:
        for i in input:
            for k in numbers:
                if i == k:
                    check = True
                else:
                    continue
        if check == True:
            return True
        else:
            return False
    else:
        return False

def controllerOne(input):
    oddsum = 0
    evensum = 0
    odds = ""
    evens = ""
    algrthm_odds = 0
    algrthm_evens = 0

    counter = 0
    for i in input:
        counter = counter + 1
        if counter % 2 == 1:
            odds = odds + i
        else:
            evens = evens + i

    for i in odds:
        oddsum = oddsum + int(i)

    for i in evens:
        evensum = evensum + int(i)

    counter = 0
    for i in odds:
        counter = counter + 1
        if counter <= 5:
            algrthm_odds = algrthm_odds + int(i)

    counter = 0
    for i in evens:
        counter = counter + 1
        if counter <= 4:
            algrthm_evens = algrthm_evens + int(i)

    algrthm_one = ((7 * algrthm_odds) + (9 * algrthm_evens)) % 10

    if str(algrthm_one) == input[9]:
        return True
    else:
        return False


def controllerTwo(input):
    oddsum = 0
    odds = ""
    algrthm_odds = 0

    counter = 0
    for i in input:
        counter = counter + 1
        if counter % 2 == 1:
            odds = odds + i

    for i in odds:
        oddsum = oddsum + int(i)

    counter = 0
    for i in odds:
        counter = counter + 1
        if counter <= 5:
            algrthm_odds = algrthm_odds + int(i)

    algrthm_two = (8 * algrthm_odds) % 10

    if str(algrthm_two) == input[10]:
        return True
    else:
        return False

def controllerThree(input):
    firstten = 0
    counter = 0
    for i in input:
        counter = counter + 1
        if counter < 11:
            firstten = firstten + int(i)

    algrthm_three = firstten % 10

    if str(algrthm_three) == input[10]:
        return True
    else:
        return False

#-----------------------------------------------
def isTCvalid(input):
    if elevenController(input) == True:
        if controllerOne(input) == True:
            if controllerTwo(input) == True:
                if controllerThree(input) == True:
                    print("Valid TC")
                    main()
                else:
                    print("Invalid TC")
                    main()
            else:
                print("Invalid TC")
                main()
        else:
            print("Invalid TC")
            main()
    else:
        print("TC number is a 11-digit number, please try again!")
        main()

def main():
    TCnumber = input("TC number: ")
    isTCvalid(TCnumber)

main()