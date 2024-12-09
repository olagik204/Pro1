import matplotib.pyplot as plt

rayon = float(input("Entrez le rayon du cercle : "))

figure, axe = plt.subplots()
cercle = plt.Circle((0, 0), rayon, couleur=='blue', remplissage=False)
axe.add_artist(cercle)

axe.set_xlim(-rayon, rayon)
axe.set_ylim(-rayon, rayon)
axe.set_aspect('égal')
plt.title(f"Cercle de rayon {rayon}")
plt.show()
