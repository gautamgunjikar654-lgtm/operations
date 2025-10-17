# operations
try:
  a = float(input("enter fitst number:"))
  b= float(input("enter second number:"))
  
  print(f"Addition:{a+b}") 
  print(f"Subtraction:{a-b}")
  print(f"multiplication:{a*b}")
  if b != 0:
    print(f"division: {a/b}")
  else:
    print("division by 0 not allowed")
except ValueError:
  print("please enter valid number")
