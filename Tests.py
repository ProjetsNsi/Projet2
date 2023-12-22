from TextSearch import *


if __name__ == '__main__':
    #Tests du module, les résultats attendus sont toujours True, si non cela est précisé à côté de la ligne concernée
    import doctest
    doctest.testmod()

    #Tests de est_present_naif
    print("Tests de est_present_naif \n")
    print(est_present_naif("","texte") == True)
    print(est_present_naif("a","cbazq") == True)
    print(est_present_naif("b","aa") == False)
    print(est_present_naif("aa","b") == False)

    #Tests de positions_naif
    print("\nTests de positions_naif \n")
    print(positions_naif("","texte") == [0,1,2,3,4])
    print(positions_naif("a","cbazq") == [2])
    print(positions_naif("b","aa") == [])
    print(positions_naif("aa","b") == [])

    #Tests de recherche_n
    print("\nTests de recherche_n \n")
    #print(recherche_n("","texte.\n",[]))  Si on réalise ce test, une assertion sera déclenché, je la met donc en commentaire pour ne pas stopper le programme, mais vous pouvez l'essayer après avoir vérifier une première fois le programme
    #print(recherche_n("a","texte",[])) Pareil
    print(recherche_n("a","cba.\nzq",[]) == "cba.\n\n")
    print(recherche_n("b","aa.\n",[]) == "")
    print(recherche_n("aa","b.\n",[]) == "")

    #Tests de bad_carac_horspool
    print("\nTests de bad_carac_horspool \n")
    print(bad_carac_horspool("") == {})
    print(bad_carac_horspool("anpanman") == {'a': 1, 'n': 3, 'p': 5, 'm': 2})

    #Tests de positions_horspool
    print("\nTests de positions_horspool \n")
    #print(positions_horspool("","texte")) Assertion de nouveau
    print(positions_horspool("a","cbazq") == [2])
    print(positions_horspool("b","aa") == [])
    print(positions_horspool("aa","b") == [])

    #Tests de positions_BM
    print("\nTests de positions_BM \n")
    #print(positions_BM("","texte")) Encore
    print(positions_BM("a","cbazq") == [2])
    print(positions_BM("b","aa") == [])
    print(positions_BM("aa","b") == [])

    #Tests de bon_suffixe
    print("\nTests de bon_suffixe \n")
    print(bon_suffixe("") == {})
    print(bon_suffixe("anpanman") == {'n': 8, 'an': 3, 'man': 6, 'nman': 6, 'anman': 6, 'panman': 6, 'npanman': 6})

    #Tests de recherche_bm
    print("\nTests de recherche_bm \n")
    #print(recherche_bm("","texte.\n",[])) Pareil
    #print(recherche_bm("a","texte",[])) Pareil
    print(recherche_bm("a","cba.\nzq",[]) == "cba.\n\n")
    print(recherche_bm("b","aa.\n",[]) == "")
    print(recherche_bm("aa","b.\n",[]) == "")
