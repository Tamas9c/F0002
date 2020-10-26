'''
F0002b: Mi lesz kiírva a program kimenetének utolsó sorában?

Válasz: tyúk
Mivel a kutya változó értéke a cica változójáé lesz és a cica
változó értéke 'tyúk'.
'''

cica = 'kutya'
print(cica)
kutya = 'egér'
egér = 'cica'
print('kutya')
cica = 'tyúk'
print(egér)
kutya = cica
print('kutya')
print(kutya)