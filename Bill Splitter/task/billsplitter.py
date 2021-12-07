# write your code here
import random

print('Enter the number of friends joining (including you)')
number_of_people = int(input())
people = {}

if number_of_people < 1:
    print('No one is joining for the party')
else:
    print('Enter the name of every friend (including you), each on a new line:')
    for a in range(number_of_people):
        people.update({input(): 0})
    print('Enter the total bill value:')
    total_bill = int(input())
    print('Do you want to use the "Who is lucky?" feature? Write Yes/No:')
    lucky_feature_enabled = input()
    if lucky_feature_enabled == "Yes":
        lucky_feature_enabled = True
    else:
        lucky_feature_enabled = False
    if lucky_feature_enabled:
        lucky_person = list(people.keys())[random.randint(0, number_of_people - 1)]
        print(f"{lucky_person} is the lucky")
        for a in people:
            if a == lucky_person:
                continue
            people[a] = round(total_bill / (number_of_people - 1), 2)
        print(people)
    else:
        print('No one is going to be lucky')
        for a in people:
            people[a] = round(total_bill / number_of_people, 2)
        print(people)
