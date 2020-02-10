file=open('nam.txt','r')

out=file.read(2)
print(out)

out2=file.read(3)
print(out2)

file.read(4)

out3=file.read(5)
print(out3)

tmp=file.read(10)
print(tmp)
tmp+=file.read(5)
print(tmp)
