def validChecking(str):
    oprt = ['+', '-', '*', '/']
    for i in range(len(str)):
        if str[i].isalpha():
            if str[i].islower():
                print("Input error")
                return False
        else :
            if str[i] not in oprt :
                print("Input error")
                return False
    return True
    #to be continue

def readFile():
    with open('data.txt','r') as rf :
        print("Open file success")
        content = rf.read()
    validChecking(content)

    rf.close()