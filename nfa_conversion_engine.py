transitions = []
sigma = []
state = []
final_states = []
start=[]
ok = 0
f = open("nfa_config_file")
s = f.readline().split()
while(len(s)):
    if "#" in s[0]:
        s = f.readline().split()
    if s[0] == "Sigma":
        ok = "Sigma"
    if s[0] == "Transitions":
        ok = "Transitions"
    if s[0] == "States":
        ok = "States"
    if ok == "Sigma" and s[0] != "Sigma" and s[0] != ":" and s[0] != "#" and s[0] != "End":
        sigma.append(s[0])
    if ok == "States" and s[0] != "States" and s[0] != ":" and s[0] != "#" and s[0] != "End" and s[0][0] != "#":
        list_state=[]
        list_state.append(s[0])
        state.append(list_state)
        if len(s) == 3 and "#" not in s and ",#" not in s:
            if s[2]=='F':
                final_states.append(s[0]);
            if s[2]=='S':
                start.append(s[0])
    if ok == "Transitions" and s[0] != "Transitions" and s[0] != ":" and s[0] != "#" and s[0] != "End" and s[0][0] != "#":
        list_transitions = []
        list_transitions.append(s[0])
        list_transitions.append(s[2])
        list_transitions.append(s[4])
        transitions.append(list_transitions)
    s = f.readline().split()

transitions_2=[]
for stare in state:
    stare_curenta=stare
    # print(stare)
    for simbol in sigma:
        lista_stari=[]  #starile in care putem ajunge cu simbolul dat
        for s in stare_curenta:
            for tranzitie in transitions:
                if tranzitie[0]==s and tranzitie[1]==simbol:
                    if tranzitie[2] not in lista_stari:
                        lista_stari.append(tranzitie[2])
        if lista_stari:
            nr=len(lista_stari)
            ok=0
            for ss in state:
                nr3=len(ss)
                nr2 = 0
                if nr3 == nr: #daca au acelasi nr de elemente
                    for w in lista_stari:
                        if w in ss:
                            nr2=nr2+1
                    if(nr2==nr): #daca toate elementele din lista stari se gasesc in ss
                        ok=1
                        lista_stari=ss #daca e gasita lista dar in alta ordine o rescriem
            l_mare = []
            l_mare.append(stare_curenta)
            l_mare.append(simbol)
            l_mare.append(lista_stari)
            transitions_2.append(l_mare)
            if lista_stari not in state:
                state.append(lista_stari)
                print(lista_stari)


reachable = []
reachable.append(start)

for a in reachable:
    for t in transitions_2:
        if t[0] in reachable:
            if t[2] not in reachable:
                reachable.append(t[2])

transitions_3=[]

for t in transitions_2:
    ok=0
    for acc in reachable:
        if t[0]==acc:
            ok=1
    if ok ==1:
        transitions_3.append(t)


state_2=[]
for stare in reachable:
    temp =[]
    temp.append(stare)
    for final in final_states:
        if final in stare:
            temp.append('F')
    if stare==start:
        temp.append('S')
    state_2.append(temp)

print("Sigma:")
for litera in sigma:
    print(litera)
print("End")
print("States:")
for s2 in state_2:
    if(len(s2)!=1):
        if s2[1]=="S":
            print(*s2[0],sep="",end=", S")
        if s2[1]=="F":
            print(*s2[0],sep="",end=", F")
        print("")
    else:
        print(*s2[0], sep="")
print("End")
print("Transitions:")
for t2 in transitions_3:
    print(*t2[0], sep="", end=", ")
    print(t2[1], end=", ")
    print(*t2[2], sep="",)
print("End")
