user_input = str(input("Spell out your name! (Seperate letters by comma, ex. 'j,o,e') -> "))
name_list = user_input.split(",")
count = 0
name = ""
while count < len(name_list):
  name += name_list[count]
  count += 1

if len(name) % 2 == 1:
  print("Hey, " + name + "! Your name has an odd number of letters.")
else:
  print("Hey, " + name + "! Your name has an even number of letters.")

