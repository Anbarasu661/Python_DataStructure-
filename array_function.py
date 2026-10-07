import re

cars1 = ["MumbaiChennaiKerala"]

text = cars1[0]

#"[A-Z] finds an uppercase letter, and [a-z]* finds all the lowercase letters that follow it."
# findall() searches the entire string and returns all matching values.
cities = re.findall('[A-Z][a-z]*', text)

for x in cities:
    print(x)

    