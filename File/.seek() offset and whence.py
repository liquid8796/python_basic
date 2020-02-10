file = open('code_tips.txt', 'w+')
file.write('-use simple function and variable names\n-comment code\n-organize code into functions\n')
file.seek(0)
line=file.read()
print(line)

file.seek(4)
line=file.read()
print(line)
