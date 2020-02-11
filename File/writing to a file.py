log_file = open('log_file.txt', 'w+')
log_file.close()
log_file = open('log_file.txt', 'a+')
def logger(log):
    log_entry = input("enter log item (enter to quit): ")
    count = 0

    while log_entry:
        count += 1
        log.write(str(count) + ": " + log_entry + "\n")
        log_entry = input("enter log item (enter to quit): ")
        
    return count
logger(log_file)    
log_file.seek(0)
log_text = log_file.read()
print()
print(log_text)
log_file.close()

count_file = open("count_file.txt", "w+")
count_file.write("Count is: 0")
count_file.seek(0)
print(count_file.readline().strip())
count_file.close()
count_file = open("count_file.txt", "r+")
count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)
count = int(count_line[10:])+1
count_file.seek(10)
count_file.write(str(count))
count_file.seek(0)
print("\nAFTER\n" + count_file.readline().strip())
count_file.close()
def inc_count(cnt_file):
    cnt_file.seek(0,0)
    cnt_line = cnt_file.readline().strip()
    cnt = int(cnt_line[10:])+1
    cnt_file.seek(10,0)
    cnt_file.write(str(cnt))
    return cnt
count_file = open("count_file.txt", "r+")

count_file.seek(0)
count_line = count_file.readline().strip()
print("BEFORE\n" + count_line)

for i in range(5):
    count = inc_count(count_file)
    count_file.seek(0)
    print("\nAFTER inc_count() call", i+1, "\n" + count_file.readline().strip())

count_file.close()
'''

MODE	Description
'r'	read only mode
'w'	write - overwrites file with same name
'w+'	write and read mode - overwrites file with same name
'r+'	read and write mode (no overwrite, can use seek)
'a'	opens for appending to end of file (no overwrite, no need seek)
'a+'	opens for appending to end of file (no overwrite) plus read

'''