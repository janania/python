#name
name = input("What is your name?: ").strip()
#age
age = input("How old are you?: ").strip()
#school
school = input("What school do you attend?: ").strip()
#food
food = input("What is your favorite fastfood?: ").strip()
#goal
goal = input("What is your goal for the new year?: ").strip()
#output_format
output = """Your name is {} and you are {} years old. You go to {} and your favorite
fast food is {}. Your goal for 2018 is to {}""".format(name, age, school, food, goal)
#print_output
thanks = "Thanks for taking this quick survey :)"
print(output)
print()
print(thanks)
