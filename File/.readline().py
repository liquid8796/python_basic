file=open("nam.txt","r")

file.readline()
tmp1=file.readline()
tmp2=file.readline()
tmp3=file.readline()
file.close()
print(tmp1+tmp2+tmp3)
list=[tmp1,tmp2,tmp3]
print(list)
