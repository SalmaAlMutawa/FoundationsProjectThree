# CLASSES AND METHODS
class Person():
    def __init__(self, name, bio, age):
        self.name = name
        self.bio = bio
        self.age = age


class Club():
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.club_members = []


    def assign_president(self, person):
        self.president = person


    def recruit_member(self, person):
        if person not in self.club_members:
           self.club_members.append(person)

    def average_age(self):
        age = 0
        numb_of_members = len(self.club_members)
        for person in self.club_members:
            age += person.age
        
        average = age/numb_of_members 
        return average
        



    def print_member_list(self):
        for person in self.club_members:
            print ("\t- %s (%s years old) - %s" %(person.name, person.age, person.bio))

