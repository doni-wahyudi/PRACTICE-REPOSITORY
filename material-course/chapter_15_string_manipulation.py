name = "  doni wahyudi  "
action = "DO SELF LEARNING"
name_mess = "!!!doni wahyudi!!!"

# print(f"{name.upper()}")
# print(f"{action.lower()}")

# new_action = action.lower().replace("learning","practice")
# print(new_action)

# action_list = action.split() #split string to list
# print(action_list)

# activity = "_".join(action_list) #combine list to string with addition words "_"
# print(activity)

# print(name)
# print(name.strip()) #remove space in first and last
# print(name_mess.strip("!")) #or remove specific string in first and last

# position = action.find("SELF") #give the index of specific word
# print(position)

# print(action.count("E")) #count specific word

# print(action[3:7]) #string slicing from index 3 to 6
# print(action[action.find("SELF"):action.find("SELF")+len('self')])

# if "DO" in action: #check if specific word contained in string
#     print("There's DO in action")
# else:
#     print("There is no DO in action")

# print(len("  doni wahyudi  "))
# print(len(name))

vocal = 0
for alphabet in name:
    if alphabet in "aiueo":
        vocal += 1 #count number of strings in name matched in aiueo
print(f"There's a total of {vocal} vocal words in name")

