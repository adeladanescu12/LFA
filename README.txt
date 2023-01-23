In cfg_config_file avem 4 sectiuni:
-in sectiunea "StartPoints" avem variabila de start(poate fi una singura);
-in sectiunea "Variables" avem variabilele, adica "non-terminals" si inclusiv variabila de start;
-in sectiunea "Terminals" avem stringurile "terminals". Multimea de terminals trebuie sa fie disjuncta de multimea de variabile;
-in sectiunea "Rules" avem productions, adica regulile.Fiecare regula contine o sageata "->". In stanga sagetii se pot afla doar variabile,
iar in dreapta sagetii un string de variabile si terminale. Prin conventie, prima regula trebuie sa inceapa cu variabila de start. Daca mai multe reguli
au aceeasi variabila in partea dreapta atunci le vom scrie pe o singura linie, separand dupa sageata stringurile de la fiecare regula in parte
cu simbolul "|".
Fiecare element din fiecare sectiune este scris pe cate un rand.
Fiecare comentariu incepe cu "//". Acestea sunt scrise fie pe linie noua fie pe aceeasi linie dupa inserarea unui spatiu.
Fiecare sectiune se incheie cu "End".


