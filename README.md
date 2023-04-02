# imageASCII
transformation d'images en ASCII

Code permettant de transformer des images en ASCII de 4 manières différentes:
- sous forme de chaine de caractères
- sous forme de chaine de caractères mais qui au lieu de convertir chaque pixel en caractère ASCII convertit un groupe de 16x16 pixel en un caractère ASCII
- sous forme d'image
- sous forme d'image mais qui au lieu de convertir chaque pixel en caractère ASCII convertit un groupe de 16x16 pixel en un caractère ASCII

Pour utiliser ce projet il faut, dans l'appel de fonction de la dernière ligne:
- mettre dans img l'image à modifier
- mettre l'echelle ASCII souhaite
	pour prendre l'option 1 ou 2, entrer une chaine de caractères, du caractère le plus sombre au moins sombre
	pour prendre l'option 3 ou 4, entrer une image contenant l'échelle de caractères choisie, tous les caractères doivent faire 16x16 et être mis en ligne toujours du plus sombre au moins sombre
	(il y a des échelles par défaut dans le programme)
- mettre l'option choisie (1, 2, 3, 4)

Pour choisir l'image à changer en ASCII:
- pour la solution 1, l'image apparaissant sous la forme d'une chaine de caractères dans la console, il y a de grandes chances qu'elle ne rentre pas dans la console et qu'elle n'aille pas à la ligne aux bons endroits
- pour la solution 2, étant donné que l'image met un caractère pour un groupe de 16x16 pixel il y a un risque de perdre de nombreux détails et de ne plus la reconnaitre. Si l'une de ses dimensions n'est pas un multiple de 16 alors la partie qui dépasse ne sera pas prise en compte
- pour la solution 3, étant donné que chaque pixel de l'image sera remplacé par un carré de 16x16 cela va être très très lent et pourait faire ramer l'ordinateur. Il faut donc éviter les images trop grandes. Il y a donc déjà une image à disposition ainsi que son résultat en exemple
- pour la solution 4, les problèmes seront les mêmes que pour la solution 2 mais ce sera aussi un peu plus lent
