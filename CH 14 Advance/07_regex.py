import re

text = "Contact us at support@example.com or sales@example.org"
pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
matches = re.findall(pattern, text)
print("Email matches:", matches)

name = "John Doe 12345"
print("Digits:", re.findall(r"\d+", name))
print("Words:", re.findall(r"\w+", name))

phone = "+91-98765-43210"
matched = re.fullmatch(r"\+?\d{2}-\d{5}-\d{5}", phone)
print("Phone valid:", bool(matched))
