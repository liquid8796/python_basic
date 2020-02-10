file=open("nam.txt","r")

line=file.readline()
while line:
    print(line[:-1].upper())
    line=file.readline()
file.close()