file=open("data.txt","w+")
line=file.read();
print("New file content:"+line)
file.write("Hello\nWorld!")
line=file.read()
print("New content update:"+line)

file.seek(0)
line=file.read()
print("Content after seek:"+line)
file.close()
