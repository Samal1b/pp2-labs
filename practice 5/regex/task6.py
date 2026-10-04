import re
text = "Hello, world. How are you"
print(re.sub(r'[ ,.]', ':', text))
