# this is an adventure game
print("***Wellcome to this ADVENTURE game!!!***")
ans = input("Are you ready to go to this adventure?[y/n]: ")

if ans.lower() == "y":
    cave_jungle = input("Where do you want to go?[cave/jungle]: ")
    if cave_jungle.lower() == "cave":
        print("\n*Wellcome to the cave*")
        com = input("You saw a bear sleeping in the cave;\nWhat Will you do?[run/fight]: ")
        if com.lower() == "fight":
            print("The bear is stronger than you. You loose!!!")
        elif com.lower() == "run":
            print("You saved your life!")
        else:
            print("I cannot understand.")

    elif cave_jungle.lower() == "jungle":
        print("\n*Wellcome to the jungle*")
        com = input("You saw a tiger in the jungle;\nWhat Will you do?[run/fight]: ")
        if com.lower() == "fight":
            print("The tiger is stronger than you. You loose!!!")
        elif com.lower() == "run":
            print("You saved your life!")
        else:
            print("I cannot understand.")
else:
    print("Ok, that's fine.")