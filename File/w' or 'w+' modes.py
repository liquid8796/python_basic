file=open("data.txt","w")
print(file)
file.write("Hello\nWorld!")
file.close()

file=open("data.txt","r")
line=file.read()
print(line)
file.close()