key = 1234
print("Introduce your password :")
userkey = int(input())


if userkey == key :
    print("------------------")
    print("What does you want to do : ")
    listabc = ["Transfer" ,"or" , "Withdrawal"]
    for e in listabc :
        print(e)
    print("------------------")
    print("please enter what you want to do :")
    what2do = str(input())
    print("------------------")
    if what2do == "transfer":
        listatr = ["Interbank", "or", "Our bank"]
        for p in listatr:
            print(p)
        print("-------------------")
        print("enter what type would be your transfer :")
        bankorintbank = str(input())
        print("-------------------")
        if bankorintbank == "interbank":
            print("insert the account number :")
            print("-------------------")
            accountNumber = str(input())
            print("-------------------")
            print("How much money you want to transfer ? :")
            trmoney = int(input())
            print("-------------------")
            print("The transfer has been completed with a transferred amount of", trmoney, "soles to", accountNumber,
                  "account number")

        if bankorintbank == "our bank":
            print("insert the account number (9 characters ):")
            accountournum = str(input())
            print("-------------------")
            print("How much money you will like to transfer?")
            trmn = str(input())
            print("-------------------")
            print("the money has bean transfer to ", accountournum, "with a amount of money of", trmn, "soles")

    if what2do == "withdrawal":
        print("Enter the amount to withdraw :")
        moneywithdraw = int(input())

        print("the withdrawal has been completed with an amount of", moneywithdraw, "soles",
              "thank you for trusting us your money  ")
        print("----------------")


else :
    print("Im sorry the passwords doesn´t match")





