class Donate:
    def __init__(self, nickname, origin):
        self.nickname = nickname
        self.origin = origin
    
    def caller(self):
        print(f"Hi there {self.nickname} from {self.origin}! Nice to meet you!")

    # def address(self):
    #     print(f"I'm from {self.origin}")

    def participate(self,total):
        member = {}
        member[name] = total
        print(f"Thankyou {self.nickname}, your donation of Rp. {total:,} have been accepted")
        return member


name = input("Please input your name : ")
place = input("Where do you live: ")

person_A = Donate(name, place)

person_A.caller()

option = input("Do you want to make a donation? (Y/N): ")

if option.lower() == "y":
    total = int(input("How much you would like to donate: "))
    member = person_A.participate(total)
else:
    print(f"Got it, Thankyou for your visit {name}")

print(member)
# person_A.address()