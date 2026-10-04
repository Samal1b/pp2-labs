import re
text = "hello_world test abc_def ghi_123"
print(re.findall(r'\b[a-z]+_[a-z]+\b', text))
