lis=input("enter a list(apace seperated):")
s1=lis.split()
print(s1)
result=''
for element in s1:
    result += str(element)
    print("concatenate in the list:",result)
