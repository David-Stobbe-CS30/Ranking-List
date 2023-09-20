def printList():
    rank = 1
    for i in rankList:
        print(f'{rank}: {i}')
        rank+=1

rankList = open('rankingList.txt', 'r').read().split('\n')
rankList.pop()
exit = False
while not exit:
    print("MAIN MENU")
    print("1: PRINT LIST")
    print("2: ADD ITEM TO END")
    print("3: REMOVE LAST ITEM")
    print("4: INSERT AT POSITION")
    print("5: REMOVE AT POSITION")
    print("6: MOVE TO POSITION")
    print("7: EDIT ITEM")
    print("8: EXIT")
    choice = int(input("ENTER OPTION: "))

    if(choice == 1):
        print("RANK LIST")
        if(len(rankList) > 0):
            printList()
        else:
            print("NO ITEMS IN THE RANK LIST")
    elif(choice == 2):
        print("ADD ITEM TO END")
        item = input("Enter Item: ")
        rankList.append(item)
        printList()
    elif(choice == 3):
        print("REMOVE LAST ITEM")
        print(f'{rankList.pop()} removed from list')
        printList()
    elif(choice == 4):
        print("INSERT ITEM")
        pos = int(input("Insert Position: "))
        item = input("Item to Insert: ")
        rankList.insert(pos - 1, item)
        printList()
    elif(choice == 5):
        print("REMOVE AT POSITION")
        pos = int(input("Position to remove: "))
        print(f'{rankList.pop(pos - 1)} removed from list')
        printList()
    elif(choice == 6):
        print("MOVE TO POSITION")
        pos = int(input("move item from: "))
        newpos = int(input("move item to: "))
        rankList.insert(newpos - 1, rankList.pop(pos - 1))
        printList()
    elif(choice == 7):
        pos = int(input("enter position: "))
        item = input("replace with: ")
        rankList[pos - 1] = item
        printList()
    else:
        file = open('rankingList.txt', 'w')
        for i in rankList:
            file.write(f'{i}\n')
        exit = True
