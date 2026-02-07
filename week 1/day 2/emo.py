grade=[]

total=0

for i in range(5):
    sub=int(input("ENTER SUBJECT MARKS"))
    grade.append(sub)
    total=total+sub
    average=total/5
print("TOTAL: ",total)
print("AVERAGE: ",average)
print(grade)

if average<35:
    print("YOU FAILED NIGGA")
elif average>=35 and average<50:
    print("C")
elif average>=50 and average<75:
    print("B")
elif average>=75 and average<90:
    print("A")
else:
    print("READ LESS NIGGA")
    