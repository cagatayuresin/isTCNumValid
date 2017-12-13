from isthisavalidtc import *

def main():
    k = input("IsTCValid?[1], RandomTC[2]: ")
    if k == "1":
        y = input("Please Enter TC: ")
        if isTCvalid(y) == True:
            print("Valid TC")
        else:
            print("Invalid TC")
    elif k == "2":
        y = randomValidTC()
        print("Random TC: " + y)
    main()

main()