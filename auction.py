from replit import clear
from art import logo
import os

def clear():
    os.system("clear" if os.name == "posix" else "cls")

# Kullanımı
clear()
print(logo)
print("Welcome to the secret auction program.")
list= {}

max_key=""
max_value=0


name=input("What's your name?:")
bid=int(input("What is your bid?:"))
list[name]=bid
should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")
while should_continue=="yes":
  clear()
  name=input("What's your name?:")
  bid=int(input("What is your bid?:"))
  list[name]=bid
  should_continue=input("Are there any other bidders? Type 'yes' or 'no'.")


for name,bid in   list.items():
  if bid>max_value:
    max_value= bid
    max_key=name
    
#max_key=(max(list, key=list.get))
#max_value = list[max_key]
print(f"The winner is {max_key} with a bid of {max_value}.")