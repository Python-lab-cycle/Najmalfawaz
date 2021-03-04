import csv
csv_col=['ID','NAME','PLACE']
dict_data=[{'ID':1,'NAME':'murshid','PLACE':'kunnamkulam'},
           {'ID':2,'NAME':'abdul','PLACE':'kunnamkulam'},
           {'ID':3,'NAME':'najmal','PLACE':'malappuram'},
           {'ID':4,'NAME':'fawaz','PLACE':'malappuram'},
           {'ID':5,'NAME':'alan','PLACE':'thrissur'},
           {'ID':6,'NAME':'ajmal','PLACE':'idukki'},
           {'ID':7,'NAME':'jeny','PLACE':'alapuzha'},
           {'ID':8,'NAME':'anu','PLACE':'ernakulam'},
           {'ID':9,'NAME':'ameen','PLACE':'kannur'},
           {'ID':10,'NAME':'ebin','PLACE':'muvattupuzha'},]
try:
    with open("Names.csv",'w')as file1:
        writer1=csv.DictWriter(file1,fieldnames=csv_col)
        writer1.writeheader()
        for data1 in dict_data:
            writer1.writerow(data1)

except IOError:
        print("I/O error")
data1=csv.DictReader(open("Names.csv"))
print("CSV file as a dictionary:\n")
for row in data1:
    print(row)
            
    
