from art import logo1
#Calculator
#Add function
def add(n1,n2):
  return n1+n2

#Subtract Function
def sub(n1,n2):
  return n1-n2

#Multiply
def multiply(n1,n2):
  return n1*n2

#Divide
def divide(n1,n2):
  return n1/n2

operations = {
  "+":add,
  "-":sub,
  "*":multiply,
  "/":divide
}
def calculator():
  print(logo1)
  num1=float(input("What's the first number?: "))
  for key in operations:
    print(key)
  should_continue=True
  while should_continue:
    
    operation_symbol= input("Pick an operation: ")
    num2=float(input("What's the next number?: "))
    answer = operations[operation_symbol](n1=num1,n2=num2)
    
    print(f"{num1} {operation_symbol} {num2} = {answer}")
  
    if input(f"Type 'y' to continue calculating with {answer},or type 'n' new start...: ")=="y":
      num1=answer
    else:
      should_continue= False
      calculator()
  

calculator()