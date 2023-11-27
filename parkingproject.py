#parking lot project 
import random
spot = random.randint(1,30)
open = True
question = True
parked = ['HJK8763','KLI1421','JBG1782', 'PKL9012', 'KPl73654', 'ASD1234', 'CSDK3289', 'DKV3258', 'PKE2182', 'YTE2190', 'EWOF2131', 'WQW0321']
capacity = 30 
availible = capacity - len(parked)
while open == True:
    while question == True:
        print("Welcome, would you like to park or view our capcity?")
        print("1) Park")
        print("2) Capacity")
        response = int(input("1 or 2: "))
        if response == 1: 
            break
        elif response == 2:
            print(f"Our capacity is {capacity}")
            print('We have two floors, each floor has 15 parking spots')
            print(f"We currently have {availible} empty slots ")
            continue
        else:
            print("Error, please enter a valid response")
    if spot <= 15:
        floor = 1
    else:
        floor = 2
    plate = input("Enter you plate: ")
    if parked.count(plate) == 1:
        print('This plate is already registered to a car parked in this lot')
        print('Try again later or check your plate')
        print('')
        continue
    else:
        print(f'Your parking spot is on floor {floor}, spot number {spot}') 
        parked.insert(spot, plate)
    leaving = random.randint(1, 12)
    if leaving == spot:
        leaving = random.randint(1,12)
        if leaving <= 6:
            floor2 = 1 
        else:
            floor2 = 2
    else:
        if leaving <= 6:
            floor2 = 1 
        else:
            floor2 = 2
    print('')
    print('')
    print(f"The vehicle on floor {floor2} spot {leaving} has left")
    left = leaving 
    parked.pop(left)
    print(parked)
    print('')