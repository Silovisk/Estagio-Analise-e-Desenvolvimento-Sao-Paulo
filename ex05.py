string = 'silas'
invertida = ""
for i in range(len(string)):
    # Teste mesa da logica utilizada
    #  = s +
    # s = i + s
    # is = l + is
    # lis = a + lis
    # alis = s + alis
    invertida = string[i] + invertida
print("A string invertida é:", invertida)
