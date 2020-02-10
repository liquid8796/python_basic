file=open("nam.txt","r")
line=file.readline()
while line:
    print(line)
    line=file.readline()
file.close()

file=open("nam.txt","r")
line=file.readline().strip()
while line:
    print(line)
    line=file.readline().strip()
file.close()

