file=open("text.txt","r")
line=file.readline()
while line:
    print(line)
    line=file.readline()
file.close()

file=open("text.txt","r")
line=file.readline().strip('*\n')
while line:
    print(line)
    line=file.readline().strip('*\n')
file.close()