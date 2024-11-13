# Programmation d'un 2048

L'**objectif** de ce mini-projet est de développer, de manière très incrémentale, le jeu 2048 afin de vous former aux bonnes pratiques de la programmation et à la culture de la qualité logicielle. En particulier, au travers de ce projet, vous allez découvrir plusieurs principes du mouvement dit du [*Software Craftmanship*](https://www.octo.com/fr/publications/20-culture-code). 


## A propos du jeu 2048

2048 est un jeu vidéo de type puzzle conçu en mars 2014 par le développeur indépendant italien Gabriele Cirulli et publié en ligne sous licence libre via Github [ici](http://gabrielecirulli.github.io/2048/). Si vous ne connaissez pas ce jeu, prenez 5 minutes pour faire quelques parties !

![Vue du jeu 2048](./Images/2048.jpg)

Les règles du jeu sont simples :

 + A chaque tour, un chiffre 2 ou 4 apparaît dans une case vide d’une grille 4x4. 
 + Le joueur peut choisir entre 4 directions (haut, bas, gauche, droite).
 + Les chiffres de la grille sont bougés comme s’ils tombaient dans la direction souhaitée par le joueur.
 + Deux chiffres identiques consécutifs qui rentrent en collision pendant le mouvement sont remplacés par leur somme. 
 	+ Toute case résultant d'une fusion dans ce tour ne peut intervenir dans une nouvelle fusion de ce tour.
 	+ Les fusions sont accomplies en commençant par celle la plus proche du bord (de la direction choisie) puis en remontant dans le sens inverse de la direction. 	

Par exemple, pour un déplacement vers la gauche, la ligne `2 2 4 4`deviendra la ligne `4 8 0 0` et pour ce même déplacement la ligne `4 2 2 0` deviendra `4 4 0 0` car le deuxième `4` venant d'être créé, il ne sera pas fusionné à ce tour. 

Le but du jeu est de faire glisser des tuiles sur la  grille pour créer une tuile portant **au moins** le nombre 2048. Le joueur peut toutefois continuer à jouer après cet objectif atteint pour faire le meilleur score possible. De même, par défaut la grille est de taille 4 x 4 mais nous pourrons aussi en faire un paramètre de notre programme, qui par défaut sera donc de 4 x 4.


## Organisation du mini-projet

Ce mini-projet est découpé en plusieurs objectifs, eux-même découpés en  **sprints** et **fonctionnalités**. La notion de sprint fait référence à la [méthode agile](https://fr.wikipedia.org/wiki/M%C3%A9thode_agile). Un sprint correspond à un intervalle de temps pendant lequel l’équipe projet va compléter un certain nombre de tâches.

Ce travail de découpage a été fait pour vous mais c'est une des premières étapes à faire pour tout projet de developpement logiciel, au moins de manière macroscopique. **Pensez-y la semaine prochaine !**

### Objectif 1 (MVP): Un 2048 minimum, sans interface graphique, sans gestion des joueurs

Le premier objectif est de constuire et d'implémenter une version simple du jeu 2048 que l'on pourrait qualifier de **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)**. C'est l'objectif minimal à atteindre pour cette première semaine.

Ce concept de MVP a été popularisé par Eric Ries, l'auteur de [The Lean Startup](http://theleanstartup.com/), une approche spécifique du démarrage d'une activité économique et du lancement d'un produit. La figure ci-dessous permet de bien expliquer ce concept.

<img src="./Images/mvp.png" alt="drawing" width="500"/>


 + **Sprint 0** :
	 + [Installation du socle technique.](./Sprint0Installbis.md)
	 + [Analyse des besoins.](./Sprint0Analyse.md) 
	 + [Refexion autour de la conception.](./Sprint0Conception.md)

 + **Sprint 1 : Mise en place des données du jeu**
 	+ [**Fonctionnalité 1** : Représenter une grille de jeu.](./2048_S1_Grille.md)
 	+ [**Fonctionnalité 2** : Afficher une grille de jeu.](./2048_S1_Display_Grille.md)
 		
 + **Sprint 2** : **Actions des joueurs**
 	+ [**Fonctionnalité 3** : Faire jouer le joueur -Donner une instruction de jeu.](./2048_S2_joueur.md)


 + **Sprint 3** : **Gestions des déplacements des tuiles**
 	+ [**Fonctionnalité 4** : Gestion des déplacements](./2048_S3_regles.md)
 	+ [**Fonctionnalité 5** : Tester la fin du jeu](./2048_S3_Finjeu.md)

 + **Sprint 4** : **Jouer !**	

 	+ [**Fonctionnalité 6** : Faire jouer un joueur](./2048_S4_Playing.md)


### Objectif 2 : Un 2048 avec une interface graphique (Amélioration du MVP)

Lors du test de votre MVP, vous avez dû trouver le jeu sans interface graphique assez pénible. Ce sont aussi les premiers retours utilisateurs. Votre travail consiste donc ici à faire évoluer votre produit en prenant en compte ces premiers retours, notamment en améliorant l'interface par l'ajout d'une interface graphique. 


+  **Sprint 5 : Montée en compétences sur les interfaces graphiques**
	+ [Montée en compétences : les interfaces graphiques en python](./2048_S5_GUI_Tutorial.md)
+  **Sprint 6 :Creation de l'interface pour la grille de jeu** 
	+ [**Fonctionnalité 8** : Affichage de la grille de jeu dans une fenêtre Tkinter](./2048_S6_affichagegrille.md)
	+ [**Fonctionnalité 9** : Permettre la configuration du jeu via l'interface graphique](./2048_S6_configgrille.md)


### Objectif 3 : Un 2048 avec la gestion des joueurs, de leur score, suggestions de coups et cie.

Vous avez, au travers des deux objectifs précédents, découvert des méthodes de développement et notamment les étapes d'analyse, de conception et de développement. Les étapes d'analyse et de conception doivent vous permettre  de découper un objectif en `Sprints` , eux-mêmes composés de différentes **fonctionnalités**. 

A nouveau, l'achèvement de l'objectif 2 a dû vous permettre de pouvoir avoir des premiers retours utilisateurs. Si vous êtes arrivés à cette étape du projet, vous pouvez appliquer tout cela pour réaliser l'objectif 3. Vous devrez déposer avec le code de votre projet, un fichier décrivant le découpage proposé et réalisé à l'instar de ce qui vous a été proposé pour les deux premiers exercices.

