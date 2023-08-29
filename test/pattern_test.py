import re

text = "119 \nAlways On Display (Відображення \nінформації при вимкненому екрані)"
pattern = r'\d+\s+(?:\S+\s?)+\(.+?\)'
matches = re.findall(pattern, text)

for match in matches:
    print(match)
