import re
text = "a ab abb abbb ac"
print(re.findall(r'ab*', text))
