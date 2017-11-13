def printHelloByList(L):
    if type(L) == list:
        for x in L:
            print("Hello,{}!".format(x))
    else:
        print("Paramter is not a list!")

L = ['Bart', 'Lisa', 'Adam']
printHelloByList(L)


        