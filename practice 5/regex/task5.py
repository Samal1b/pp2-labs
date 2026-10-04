import re
text = "a123b hello aXYZb"
print(re.findall(r'a.*b', text))
