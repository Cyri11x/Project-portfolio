AA = float(input("Max Menge Produkt A in Land 1: "))
AB = float(input("Max Menge Produkt B in Land 1: "))
BA = float(input("Max Menge Produkt A in Land 2: "))
BB = float(input("Max Menge Produkt B in Land 2: "))

    #Individual A

    #OCAA
OCAA = float(AB / AA)

    #OCAB
OCAB = float(AA / AB)

    #Individual B 

    #OCBA
OCBA = float(BB / BA)

    #OCBB
OCBB = float(BA / BB)

print("OCAA: ", OCAA)  