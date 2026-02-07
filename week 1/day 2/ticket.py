age=int(input("ENTER THE PERSON'S AGE"))
if age<3:
    print("FREE")
elif age>=3 and age<=12:
    print("PRICE IS 10$")
elif age>=13 and age<=64:
    print("PRICE IS 20$")
elif age>=65:
    print("PRICE IS 15$")        