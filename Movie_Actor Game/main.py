lst={"SEAN CONNERY":"from russia with love","ROGER MOORE":"live and let die ","PIERCE BROSNAN":"Die another day","DANIEL CRAIG":"skyfall"}
correct=0
for i in range(0,4):
    name=input("name an actor:").upper()
    if name in ("SEAN CONNERY","ROGER MOORE","PIERCE BROSNAN","DANIEL CRAIG"):
        print(f"well done: {name} was in {lst[name]}")
        correct+=1
    else:
        print("Sorry.", name, "hasn't played Bond as far as I know.")
        correct+=0
print("You Got", correct, "out of 4.")




