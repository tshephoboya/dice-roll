from random import choice

def update_count(lcount, val):
    lcount[val-1] = lcount[val-1] + 1

def roll_dice():
    global count_list
    count_list = [0,0,0,0,0,0]

    while True:
        try:
            number_of_rolls = int(input("How many times do you want to roll? "))
            break
        except Exception as e:
            print("Please enter interger number:")

    for val in range(number_of_rolls):
        update_count(count_list, choice(range(1,7)))

    for i in range(6):
        print(str(i+1), count_list[i])

    if input('Roll again: y/n: ').lower() == 'y':
        roll_dice()

roll_dice()
