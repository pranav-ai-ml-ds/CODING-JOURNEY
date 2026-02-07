item1=int(input("ENTER PRICE OF FIRST ITEM: "))
item2=int(input("ENTER PRICE OF SECOND ITEM: "))
item3=int(input("ENTER PRICE OF THIRD ITEM: "))

total=item1+item2+item3
tax=(total*0.18)
amount=total+tax

print("TOTAL COST OF ITEMS=",total)
print("TAX",tax)
print("AMOUNT TO BE PAID ",amount)