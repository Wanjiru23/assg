answer=input("what is the answer to the great question of life?")
def life(answer):
 if (answer==42): 
    print("Yes")
 elif(answer=="fourty two"):
    print("Yes")
 elif(answer=="fourty-two"):
    print("Yes")
 else:
    print("No")
  #INDENT the if statement after declaration and ALWAYS use "" when the value is an undefined string!!!
  #all if and elif statements start the same distanc from the line.  

life(answer) 
#call the defined function as shown above after the elif ladder has run  