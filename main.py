from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
end_bid=False
bidders_name={}
while not end_bid:  
  name=input("What's your name?")
  price=int(input("What's your bid?"))
  yes_no=input("Is there any other who want to bid in the room?")
  bidders_name[name]=price
  if yes_no=="no":
    end_bid=True
  else:
    clear()
print(bidders_name)
    
max_key=max(bidders_name,key=bidders_name.get)
max_value=max(bidders_name.values())
print(f"The winner is {max_key} with the bid of ${max_value}")