file=open("nam.txt","r")

lines=file.readlines()
print(lines)
'''Clear the \n character in list'''
count=0
for i in lines:
    lines[count]=i[:-1]
    count+=1
print(lines)