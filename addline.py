line1="murshi is a ******"
file=input("enter the file name:")
f1=open(file,"w")
f1.write(line1)
f1.close()
f1=open(file,"r")
line=f1.read()
print("",line)
f1.close()
