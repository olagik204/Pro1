g = 5 
factorielle_for = 1
for i in range(1, g + 1):
    factorielle_for *= i

factorielle_while = 1
i = 1
while i <= g:
    factorielle_while *= i
    i += 1

print(f"Factorielle de {g} avec for: {factorielle_for}")
print(f"Factorielle de {g} avec while: {factorielle_while}")

nom = "KEKE"  
prenom = "Hervéola"  

for i in range(1, 51):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}: {nom} {prenom}")
    elif i % 3 == 0:
        print(f"{i}: {nom}")
    elif i % 5 == 0:
        print(f"{i}: {prenom}")
    else:
        print(i)
