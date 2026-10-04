import re
text = "ab abb abbb abbbb"
print(re.findall(r'ab{2,3}', text))
