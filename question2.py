import re
file = open("items_hacked.txt",'r')
pattern = "[a-z]{3}[A-Z]{3}[\w\d:::]+[A-Z]{3}[a-z]{3}"
file_string = file.read()
it =re.findall(pattern,file_string)
for item in it:
    print(item[6:-6])
