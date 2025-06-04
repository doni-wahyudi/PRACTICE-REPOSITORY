class Donate:
    def __init__(self, nickname, origin):
        self.nickname = nickname
        self.origin = origin

    def caller(self):    
        print(f"Hi there {self.nickname} from {self.origin}! Nice to meet you!")


class Remarks(Donate):
    def caller(self): # this will override caller method in donate class
        print(f"Hope God will bless you {self.nickname}!")


class Participate(Donate): # you could inherit again the donate class (polymorphism)
    def __init__(self, nickname, origin, total):
        super().__init__(nickname, origin)
        self.total = total

        print(f"Thankyou {self.nickname}, your donation of Rp. {total:,} have been accepted")

name = input("Please input your name : ")
place = input("Where do you live: ")

option = input("Do you want to make a donation? (Y/N): ")

if option.lower() == "y":
    total = int(input("How much you would like to donate: "))
    person_A = Participate(name, place, total)
    closing = Remarks(name, place)
    closing.caller()
else:
    print(f"Got it, Thankyou for your visit {name}")

