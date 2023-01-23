startpoint=[]
variables=[]
terminals=[]
rules=[]
ok=""

f = open("cfg_config_file")
s = f.readline().split()
while(len(s)):
    if "//" in s[0]:
        s = f.readline().split()
    if s[0] == "StartPoint:":
        ok = "startpoint"
    if s[0] == "Variables:":
        ok = "variables"
    if s[0] == "Terminals:":
        ok = "terminals"
    if s[0] == "Rules:":
        ok = "rules"
    if ok == "startpoint" and s[0] != "StartPoint:" and s[0] != ":" and s[0] != "//" and s[0] != "End":
        startpoint.append(s[0])
    if ok == "variables" and s[0] != "Variables:" and s[0] != ":" and s[0] != "//" and s[0] != "End":
        variables.append(s[0])
    if ok == "terminals" and s[0] != "Terminals:" and s[0] != ":" and s[0] != "//" and s[0] != "End":
        terminals.append(s[0])
    if ok == "rules" and s[0] != "Rules:" and s[0] != ":" and s[0] != "//" and s[0] != "End" and s[0][0] != "//":
        lista=s[0].split("->")
        lista1=lista[0]
        lista2=lista[1].split("|")
        rules.append((lista1,lista2))
    s = f.readline().split()
# print(startpoint)
# print(variables)
# print(terminals)
# print(rules)

valid=1
if len(startpoint)!=1:
    valid=0
else:
    for i in startpoint:
        if i not in variables:
            valid=0
            break
        if i!=rules[0][0]:
            valid=0

for var in variables:
    if var in terminals:
        valid=0
        break
for rule in rules:
    #print(rule[0])
    if rule[0] not in variables:
        valid=0
        break
    for x in rule[1]:
        for simbol in x:
            #print(simbol)
            if simbol not in variables and simbol not in terminals:
                valid=0
                break

if(valid==1):
    print("CFG valid")
else:
    print("CFG invalid")

