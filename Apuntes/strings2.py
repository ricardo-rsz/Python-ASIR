name = "John"
surname = "Smith"
fullname = name + surname

txt = f"The Alan Turing student is {name} {surname}"

print(fullname)
print(name,surname)
print(txt)

name2 = "   pepito    "

name2 = name2.strip().capitalize()
print(name2)

txtToSearch = "CPIFP"
txt = "This school name is CPIFP Alan Turing"
position = txt.find("CPIFP")
if position!=-1:
    schoolname = txt[position:]
    print(schoolname)
    schoolname2 = txt[position:position+len(txtToSearch)]
    print(schoolname2)