import re
text = "HelloWorldPython"
print(re.sub(r'(?<!^)(?=[A-Z])', ' ', text))
