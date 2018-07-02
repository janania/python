#Cinema Simulator
movies = {
    "Coco": [12, 3],
    "Hotel Transylvania 2" : [10, 5],
    "Despicable Me 3": [6, 10],
    "The Emoji Movie" : [14, 3],
    "The Boss Baby": [8, 10],
    "Wonder": [11, 15],
    "A Dog's Purpose" : [12, 7],
    "Cars 3" : [7, 6],
    "Beauty And The Beast" : [13, 4]
    }

while True:
    choice = input("What movie would you like to watch?: ").strip().title()

    if choice in movies:
        age = int(input("How old are you?: ").strip())

        if age >= movies[choice][0]:
            print("You are under the age limit")
            tickets = int(input("How many tickets would you like to purchase?: ").strip())

            if tickets <= movies[choice][1]:
                print("We have {} tickets available for {}. Enjoy the movie".format(tickets, choice))
                movies[choice][1] = movies[choice][1] - tickets

            elif tickets > movies[choice][1]:
                ticket_number = movies[choice][1]
                print("Sorry we don't have that many tickets; We only have {} tickets.".format(ticket_number))

                if ticket_number == 0:
                    print("Sorry we are sold out")

        else:
            print("You are too young to watch the movie")

    else:
        print("Sorry {} is not available at Fake Theaters".format(choice))
                      

            

   
        
        
