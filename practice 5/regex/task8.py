import re
text = "HelloWorldPython"
print(re.split(r'(?=[A-Z])', text))
