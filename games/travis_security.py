# Travis the ridicules Security System
user_list = ["Janani", "Shivani", "Ashokumar", "Suganthi"]

while True:
    print("Hello! I am Bobilla, the Security here")
    name = input("What is your name?: ").strip().capitalize()

    if name in user_list:
        print("Hello {}".format(name))
        remove = input("I have found your name in the existing system--Would you like to be removed from the system (yes/no)?: ").strip().lower()

        if remove == "yes":
            secondChance = input("AWW! Please don't leave. Are you 100% sure you want to remove your name (yes/no)?: ").strip().lower()

            if secondChance == "yes":
                user_list.remove(name)
                print("Its Ok, I know you will come back.")

            elif secondChance =="no":
                print("I knew it! Thank you so much for staying")

        elif remove == "no":
            print("I don't want your leave anyway :)")


    else:
        add_name = input("Well {}, Your name isn't in my system. Would you like me add your name to the system (yes/no)?: ".format(name)).strip().lower()

        if add_name == "yes":
                print("Welcome to the system {}. You are my new best friend :):)".format(name))
                user_list.append(name)

        elif add_name == "no":
                print("That's ok! It was nice meeting you {}. See you around".format(name))

            
  
