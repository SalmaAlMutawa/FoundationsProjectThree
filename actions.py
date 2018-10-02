# UTILS AND FUNCTIONALITY
from data import  population, clubs
from components import Club, Person

my_name = "Salma"
my_age = 22
my_bio = "aiming to not be a noob"
myself = Person(my_name, my_bio, my_age)

def introduction():
    print("\nHello, %s. Welcome to our portal." % my_name)

def options():
    print ("-------------------------------------------------------------------")
    print ("""Would you like to:
        1) Create a new Club
        2) Browse and join Clubs
        3) View existing Clubs
        4) Display members of a club
       -1) Close application
    """)
    operation = int(input ("Enter the number of the option you would like to perform: "))
    return operation
    
    

def create_club():
    club_name = input("Choose your club name: ")
    club_description = input ("What is the club about? ")
    new_club = Club(club_name, club_description)
    new_club.assign_president(myself)
    print ("Enter the number of members you would like to recruit in your club or enter -1 to stop.")
    i=1
    #print the names list
    for person in population:
        print ("[%s] %s" %(i, person.name))
        i+=1
    #user chooses the names
    member_choice = input()
    while int(member_choice) != -1:            
        if int(member_choice) in range (1,16):
            new_club.recruit_member(myself)
            new_club.recruit_member(population[int(member_choice)-1])
        else:
            print ("Invalid member, please try again.")
        member_choice = input()
    print ("------------------------------------------------------")
    print ("\tClub name: %s\n\tClub description: %s\n\tClub President: %s" % (new_club.name, club_description, my_name))
    print ("\tClub Members:")
    new_club.print_member_list()
    avg_age = new_club.average_age()
    print ("\tThe average age in this club is %s years old." %avg_age)
    clubs.append(new_club)




def view_clubs():
    for club in clubs:
        print ("\n\tClub name: %s\n\tClub Description: %s\n\tNumber of members:%s" %(club.name, club.description, len(club.club_members)))
    

def view_club_members():
    club_choice = input ("\nEnter the club name whose members you'd like to see: ")
    print ("\n\tMembers:")
    for club in clubs:
        if club_choice.lower() == club.name.lower():
            club.print_member_list()
            print ("\n\tClub President: %s" %club.president.name)
                

    

def join_clubs():
    choice = input ("\nEnter the name of the club you would like to join: ")
    for club in clubs:
        if choice.lower()==club.name.lower():
            club.recruit_member(myself)
            print ("\n\t%s just joined the %s!" %(myself.name, club.name))
        # print ("\nSorry, invalid club name.")
    
    

def application():
    introduction()
    operation = ""
    while operation != -1:
        operation = options()
        if operation == 1:
            create_club()
        elif operation==2:
            view_clubs()
            join_clubs()
        elif operation ==3:
            view_clubs()
        elif operation == 4:
            view_clubs()
            view_club_members()
        elif operation == -1:
            break
        else:
            print ("Sorry, invalid option. Please try again.")
        

    
