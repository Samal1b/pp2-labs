import re

with open("raw.txt","r", encoding="utf-8") as file:
    text=file.read()

price = re.findall(r'\d+(?: \d{3})*,\d{2}', text)
print(price)
products = re.findall(r'\d+\.\n(.+)', text)
print(products)
total = re.search(r'ИТОГО:\s*\n?([\d ]+,\d{2})', text)
print(total.group(1))
date_time = re.search(r'\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2}', text)
print(date_time.group())
payment = re.search(r'([А-Яа-яA-Za-z ]+):\s*\n[\d ]+,\d{2}', text)
print(payment.group(1))

print("\n Чек")

print("Товары:")
for product in products:
    print("-", product)

print("\nОбщая сумма:", total.group(1))
print("Дата и время:", date_time.group())
print("Способ оплаты:", payment.group(1))

