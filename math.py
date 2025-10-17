# operations
try:
  a = float(input("enter fitst number:"))
  b= float(input("enter second number:"))
  
  print(f"Addition:{a+b}") 
  print(f"Subtraction:{a-b}")
except ValueError:
  print("please enter valid number")
