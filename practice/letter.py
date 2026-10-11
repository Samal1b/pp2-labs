import re

text="Hello World hello"

let=re.findall('[A-Z].+', text)
print(let)