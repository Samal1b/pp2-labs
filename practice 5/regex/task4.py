import re
text = "Hello World Python TEST Apple"
print(re.findall(r'\b[A-Z][a-z]+\b', text))
