### Print a welcome message
print("Welcome to the haunted mansion!")
print("you are a distant family member of a rich millinioaore who has just passed awy, leavin gyou with milions")
print("As the newfound owner, you decide to play a vist to the masion")
print("the hose is dated, creaky and falling apprt. you walk in the front door")
print("do you want to accept the gift or death?")

### Prompt user for
lifeChoice = input("> ")

if(lifeChoice == "gift"):
    print("you have accepted the gift of immortality")
    print("As you said yes, you instantly feeling the sharp fangs devouer you")
    print("you now have the ability to fly or dont fly?")

    flyChoice = input("> ")

    if(flyChoice == "fly"):
    
   
      print("Invalid choice. Please enter fly or dont fly")

elif(lifeChoice == "death"):


  print("Invalid choice. Please enter gift or death")