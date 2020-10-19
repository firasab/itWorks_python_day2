import myItems as it

print("welcome to our store , this is what we have in our stor!")
for item in it.items:
    print("=========================")
    print(f"name : {item ['name']}")
    print(f"price : {item['price']}")
    print("=========================")
    
    
print("please enter how many items you want to buy !")
much = int(input())
count = 0
for i  in range (0 , much )  :
    print("please enter the item name you want to buy (one by one )")
    want_item = input()
    for search in it.items:
        if want_item == search['name']:
            amount = int(search['price'])
            count += amount
        else :
            continue 
    
    
print("Your total price is :" , count)



print("please tell us if you would like us to add new items to our Super Market !")
add_items = input()
print("please leave a comment for us :D")
add_comment = str(input())
print("please give us a feedback from 1-5")
feedback = int(input())

def feedback2():
  f = open("feedback.txt", "w+")
  f.write(f"the client like to add : {add_items}\n")
  f.write(f"the client like to comment : {add_comment}\n")
  f.write(f"the client feedback is : {feedback}\n")
  f.close() 

feedback2()
print("Thank you for comming <3")




















