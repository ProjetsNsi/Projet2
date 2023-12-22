import time

def est_present_naif(motif, texte):
    """
    motif - str, chaîne de caractères
    texte - str, chaîne de caractères
    Sortie: bool - True si motif est dans texte, False sinon

    >>> motif = 'CAAGT'
    >>> texte = 'ATCAAGTTCAAGTCAGTCCCCAAGTTGATGCAAGT'
    >>> est_present_naif(motif, texte)
    True
    """
    for i in range(len(texte)):
        j = 0
        while j < len(motif) and  j+i < len(texte) and texte[j+i] == motif[j] :
            j+=1
        if j==len(motif):
            return True
    return False



def positions_naif(motif, texte):
    """
    motif - str, chaîne de caractères
    texte - str, chaîne de caractères
    Sortie: list - Tableau des positions où trouver motif dans texte

    >>> motif = 'CAAGT'
    >>> texte = 'ATCAAGTTCAAGTCAGTCCCCAAGTTGATGCAAGT'
    >>> positions_naif(motif, texte)
    [2, 8, 20, 30]
    """
    result = []
    for i in range(len(texte)):
        j = 0
        while j < len(motif) and  j+i < len(texte) and texte[j+i] == motif[j] :
            j+=1
        if j==len(motif):
            result.append(i)
    return result


def recherche_n(motif,texte,globalindesirable):
    """
    motif - str, chaîne de caractères à chercher dans texte
    texte - str, chaîne de caractères contenant des points suivis de sauts à la ligne ("./n")
    globalindesirable - list, tableau contenant les indices des caractères indésirés.
    Sortie - str, Chaine de caractères contenant les différents paragraphes où se trouve le motif d'après l'algorithme naif
    """
    assert len(motif)!=0, "Le motif est vide"
    tab = [0] #Si le motif est dans avant le premier saut à la ligne, on retourne quand même le premier paragraphe et non le deuxième
    tab += positions_naif(".\n", texte)
    tab2 = positions_naif(motif,texte)
    assert len(tab)!=1, "Il n'y a pas de paragraphes dans le tableau, utilisez donc la fonctions positions_naif"
    res = ""
    j = 0
    cmpt = 0
    while j < len(tab2) and cmpt < 15: #On limite le nombre de paragraphes renvoyés à 15
        i = indice_par_dichotomie(tab2[j],tab)
        result = ""
        if i == 0 and i!= len(tab)-1:
            for k in range(tab[i],tab[i+1]+1):
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        elif i != len(tab)-1:
            for k in range(tab[i]+2,tab[i+1]+1):    # On commence à tab[i]+2 pour éviter de retourner ".\n"
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        else :
            for k in range(tab[i]+2, len(texte)-1):# On commence à tab[i]+2 pour éviter de retourner ".\n"
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        if result not in res:           #On évite de renvoyer deux fois le même paragraphe
            res += result +"\n" +"\n"
            cmpt += 1
        j+=1
    return res

def indice_par_dichotomie(val, tab):
    """
    tab - list, tableau d'entiers, trié en ordre croissant
    val - int, entier
    Sortie: int - indice de val si val est dans tab, -1 sinon.
            La recherche est faite suivant le principe de dichotomie.
    """
    debut = 0
    fin = len(tab) - 1
    milieu = (debut + fin) // 2
    while debut <= fin:
        milieu = (debut + fin) // 2
        if tab[milieu] > val and tab[milieu-1]<val:
            return milieu - 1
        elif tab[milieu] > val:
            fin = milieu - 1
        else :
            debut = milieu + 1

    return milieu


def bad_carac_horspool(motif):
    """
    motif - str, chaîne de caractères
    Sortie: dict - dictionnaire tel que :
                 - les clefs sont les caractères de motif
                 - les valeurs associées sont leur indice "le plus à droite" dans motif
            Le dernier caractère de motif n'est pas parcouru

    """
    dico = dict()
    for i in range(len(motif)-1):
        dico[motif[i]] = len(motif)-1-i
    return dico


def positions_horspool(motif, texte):
    """
    motif - str, chaîne de caractères
    texte - str, chaîne de caractères
    Sortie: list - Tableau des positions où trouver motif dans texte selon l'optimisation d'Horspool
    """
    assert len(motif)!=0, "Le motif est vide"
    n = len(texte)
    m = len(motif)
    dico = bad_carac_horspool(motif)
    i = m - 1
    result = []
    while i < n:
        k = 0
        while k < m and motif[m - 1 - k] == texte[i - k]:
            k += 1
        if k == m:
            result.append(i - m + 1)

        if texte[i] in dico:
            i += dico[texte[i]]
        else:
            i += m
    return result


def bon_suffixe(motif):
    nvmotif = ""
    dico = dict()
    for i in range(len(motif)-1,0,-1):
        n = len(motif)-1-i
        nvmotif = motif[i] + nvmotif
        tab = positions_horspool(nvmotif, motif)
        for elt in tab :
            if 0 < elt and motif[elt-1] != motif[i-1]:
                dico[nvmotif] = len(motif)-len(nvmotif)-elt
        if nvmotif not in dico.keys() :
            tab2 = positions_horspool(motif[0], nvmotif)
            for j in range(len(tab2)-1,-1,-1) :
                cmpt = tab2[j]
                while cmpt < len(nvmotif)-1 and nvmotif[cmpt] == motif[cmpt-tab2[j]] :
                    cmpt += 1
                if cmpt == len(nvmotif)-1 and nvmotif[cmpt] == motif[cmpt-tab2[j]] :
                    tabfin = positions_horspool(motif[0], motif)
                    dico[nvmotif] = tabfin[-len(tab2)+j]
        if nvmotif not in dico.keys() :
            dico[nvmotif] = len(motif)
    return dico


def positions_BM(motif,texte):
    """
    motif - str, chaîne de caractères
    texte - str, chaîne de caractères
    Sortie: list - Tableau des positions où trouver motif dans texte selon l'algorithme de Boyer-Moore
    """
    assert len(motif)!=0, "Le motif est vide"
    n = len(texte)
    m = len(motif)
    dico = bad_carac_horspool(motif)
    dico2 = bon_suffixe(motif)
    i = m - 1
    result = []
    while i < n:
        k = 0
        sous_motif = ""
        while k < m and motif[m-1-k] == texte[i-k]:
            k += 1
            sous_motif = motif[m-k] + sous_motif
        if k == m:
            result.append(i - m + 1)
        if texte[i] in dico and sous_motif in dico2:
            i += max(dico[texte[i]],dico2[sous_motif]) #On avance du maximum entre les deux règles pour gagner du temps.
        elif texte[i] in dico:
            i += dico[texte[i]]
        else:
            i += m
    return result

def recherche_bm(motif,texte,globalindesirable):
    """
    motif - str, chaîne de caractères à chercher dans texte
    texte - str, chaîne de caractères contenant des points suivis de sauts à la ligne ("./n")
    globalindesirable - list, tableau contenant les indices des caractères indésirés.
    Sortie - str, Chaine de caractères contenant les différents paragraphes où se trouve le motif d'après l'algorithme de Boyer-Moore
    """
    assert len(motif)!=0, "Le motif est vide"
    tab = [0] #Si le motif est dans avant le premier saut à la ligne, on retourne quand même le premier paragraphe et non le deuxième
    tab += positions_BM(".\n", texte)
    tab2 = positions_BM(motif,texte)
    assert len(tab)!=1, "Il n'y a pas de paragraphes dans le tableau, utilisez donc la fonctions positions_BM"
    res = ""
    j = 0
    cmpt = 0
    while j < len(tab2) and cmpt < 15: #On limite le nombre de paragraphes renvoyés à 15
        i = indice_par_dichotomie(tab2[j],tab)
        result = ""
        if i == 0 and i!= len(tab)-1:
            for k in range(tab[i],tab[i+1]+1):
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        elif i != len(tab)-1:
            for k in range(tab[i]+2,tab[i+1]+1):    # On commence à tab[i]+2 pour éviter de retourner ".\n"
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        else :
            for k in range(tab[i]+2, len(texte)-1): # On commence à tab[i]+2 pour éviter de retourner ".\n"
                if texte[k] == "\n":
                    result += " "
                elif k not in globalindesirable:
                    result += texte[k]
        if result not in res:           #On évite de renvoyer deux fois le même paragraphe
            res += result +"\n" +"\n"
            cmpt += 1
        j+=1
    return res

def benchmarknaif(motif,texte,globalindesirable):
    total = 0
    for k in range(20):
        debut = time.perf_counter()
        recherche_n(motif,texte,globalindesirable)
        fin = time.perf_counter()
        duree = fin - debut
        total += duree
    moyenne = total / 20.0
    return moyenne


def benchmarkbm(motif,texte,globalindesirable):
    total = 0
    for k in range(20):
        debut = time.perf_counter()
        recherche_bm(motif,texte,globalindesirable)
        fin = time.perf_counter()
        duree = fin - debut
        total += duree
    moyenne = total / 20.0
    return moyenne




