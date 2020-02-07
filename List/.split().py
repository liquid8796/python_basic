sentence="Hello, I am Nam. Nice to meet you!"
new_list=sentence.split()
print(new_list)

sentence="Nam-said-hello-to-world!"
new_list=sentence.split('-')
print(new_list)

sentence="""Hello to my buddy
I love you so much
So don't leave me alone!"""
new_list=sentence.split('\n')
print(sentence)
print(new_list)
