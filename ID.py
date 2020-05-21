t=int(input())
for i in range(t):
    str=input()
    if (str=="b" or str=="B"):
        print("BattleShip")
    elif (str=="c" or str=="C"):
        print("Cruiser")
    elif (str=="d" or str=="D"):
        print("Destroyer")
    else:
        print("Frigate")