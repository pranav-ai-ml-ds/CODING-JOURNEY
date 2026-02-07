shopping_list=[]

for i in range(5):
    item=input("ENETR THE ITEM TO BUY: ")
    shopping_list.append(item)

print("YOUR SHOPPING LIST")
for i in range(len(shopping_list)):
    print(str(i+1)+".",shopping_list)


    # Shopping List Manager

shopping_list = []

# Add 5 items
for i in range(5):
    item = input("Enter item to buy: ")
    shopping_list.append(item)

# Display the list
print("\n--- YOUR SHOPPING LIST ---")
for i in range(len(shopping_list)):
    print(str(i + 1) + ".", shopping_list[i])
