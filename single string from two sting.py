str1=input("enter the first string")
str2=input("enter second string")
new_a=str2[:2]+str1[2:]
new_b=str1[:2]+str2[2:]
print("the new string after swapping first two character of both string:",(new_a+''+new_b))
