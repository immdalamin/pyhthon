# Mad Libs game
print("Wellcome to THE MAD LIBS game!!!")
name1 = input("Type your name: ")
adjective1 = input("Type an adjective: ")
adjective2 = input("Type another adjective: ")
body_part1 = input("Type a name of your body part: ")

story1 = f"***\n{name1}'s morning began with a disaster.\n\
His mismatched sock collection, a chaotic symphony of {adjective1} and {adjective2}, \n\
had vanished!. Without his lucky {adjective1} pair, {name1} was sure the day \n\
would be a {adjective2} mess.  He stomped to your door, a wild look in his {body_part1}.\n***"

print(story1)
ans = input("Do you want to play again? [y/n]: ")
y = "y"

if ans.lower() == y:
    name2 = input("Type your name: ")
    adjective3 = input("Type an adjective: ")
    adjective4 = input("Type another adjective: ")
    place = input("Type a name of a place in your home: ")
    body_part2 = input("Type a name of your body part: ")

    story2 = f"***\n{name2}, a man whose fashion sense could be described as 'worn-out {adjective3} \n\
socks and a {adjective4} Hawaiian shirt on principle', had a crisis. His entire collection of \n\
mismatched socks, a collection that rivaled a {place}'s sock drawer, had vanished!. Without \n\
his lucky pair of {adjective3} and {adjective4} socks, {name2} felt utterly unprepared to face\n\
the day. He marched to his best friend's house, a suspicious glint in his {body_part2}.\n***"
    print(story2)

    ans1 = input("Do you want to play again? [y/n]: ")
    if ans1.lower() == y:
        name3 = input("Type your name: ")
        age = input("Type your age: ")
        noun1 = input("Type a noun: ")
        noun2 = input("Type a noun: ")
        plural_noun = input("Type a plural noun: ")
        adjective5 = input("Type an adjective: ")
        animal = input("Type a name of an animal: ")
        body_part2 = input("Type a name of your body part: ")

        story3 = f"***\nOnce upon a time, {name3}, aged {age}, embarked on a wild journey armed\n\
with a {noun1} and a {noun2}. Along the way, they encountered a {adjective5} {animal} \n\
in a {noun1} who offered them a ride on their {noun2}. After crash-landing in a land of \n\
{plural_noun}, {name3} joined a talent show to win {noun1}, but was interrupted by \n\
{adjective5} {plural_noun}! Following an epic showdown, {name3} emerged victorious, \n\
forever known as the 'Master of {adjective5} {noun2}.'\n***"
        print(story3)

        ans2 = input("Do you want to play again? [y/n]: ")
        if ans2.lower() == 'y':
            name4 = input("Type your name: ")
            fear = input("Type your silly fear: ")
            action = input("Type a clumsy action: ")
            subs = input("Type a disgusting substance: ")
            person = input("Type your annoying person: ")

            story4 = f"""***\nYou, {name4}'s greatest fear is {fear}.
One day, while {action}, they end up covered in {subs}.
The worst part? They have to ask {person} for help!\n***"""
            print(story4)

            ans3 = input("Do you want to play again? [y/n]: ")
            if ans3.lower() == 'y':
                name5 = input("Type your name: ")
                voice = input("Type about your terrible singing voice: ")
                show = input("Type a name of a talent show: ")
                famous = input("Type a name of a famous people: ")

                story5 = f"""***\nYou, {name5}, known for their {voice}, 
decides to audition for {show}. The judges are {famous}
and their reaction is priceless!\n***"""
                print(story5)

            else:
                print("Game closed!")
        else:
            print("Game closed!")
    else:
        print("Game closed!")
else:
    print("Game closed!")
