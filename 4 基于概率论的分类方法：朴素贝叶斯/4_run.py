
sent = 'This book is the best book on Python or M.L. I have ever laid eyes upon.'
print(sent)

array = sent.split()
print(array)

import re
reg_ex = re.compile('\\W*')
array = reg_ex.split(sent)
print(array)

items = [item for item in array if len(item) > 0]
print(items)

items = [item.lower() for item in array if len(item) > 0]
print(items)

text = open('email/ham/6.txt').read()
print(text)
array = reg_ex.split(text)
print(array)