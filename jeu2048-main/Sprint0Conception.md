# 2048 - Sprint 0 : Réflexion autour de la conception

Après cette phase d'analyse, nous pouvons avoir une première démarche de conception et essayer d'identifier les principaux objets de notre MVP. 

En lisant la [description du jeu sur Wikipedia](https://fr.wikipedia.org/wiki/2048_(jeu_vid%C3%A9o)), on identifie notamment le concept de **grille**, de **tuile** et de **déplacement**. On se contentera de ces trois objets dans cette phase.

## Vers un langage commun

Dans cette phase de réflexion sur la conception, pour favoriser le travail collaboratif et une compréhension commune entre tous les membres du projet, il est important de définir, dès le début du projet, un **vocabulaire commun** autour des termes métier. Dans le jargon du développement de logiciel, on parle de [**ubiquitous language**](http://referentiel.institut-agile.fr/ubiquitous.html) ou **langage omniprésent**. C'est un principe issu de l'approche *Domain Driven Design* décrite dans l'[ouvrage](https://github.com/p0w34007/ebooks/blob/master/Eric%20Evans%202003%20-%20Domain-Driven%20Design%20-%20Tackling%20Complexity%20in%20the%20Heart%20of%20Software.pdf) du même nom et qui consiste à identifier et à définir un langage commun autour des termes métiers.


Le déroulé consiste à produire ce que l'on appelle des [**User Stories**](https://en.wikipedia.org/wiki/User_story) (avec l'ensemble des parties prenantes du projet) qui représentent les besoins des utilisateurs à implémenter. Ce travail permet aussi de définir le langage partagé.

Une **user story** ce n'est rien d'autre qu'une phrase simple, en language naturel, qui permet de décrire le contenu d'une fonctionnalité à développer en précisant le *Qui?*, le *Quoi?* et le *Pourquoi?*

 `En tant que <qui>, je veux <quoi> afin de <pourquoi>`

Ici, typiquement par exemple: 

+ En tant qu'utilisateur, je veux pouvoir **initier un jeu** et **jouer avec mon clavier**
+ En tant que joueur, je veux pouvoir **revenir en arrière** dans le jeu.
+ En tant que joueur, je veux pouvoir **sauvegarder une partie** et la **recharger ensuite**
+ ...



Dans le cas du jeu 2048, c'est un travail qui peut vous sembler fastidieux et très certainement inutile mais qui vous sera très utile pour de nombreux autres projets.

Concernant le langage partagé, dans le cas du jeu 2048, plusieurs termes sont utilisés pour parler de la grille de jeu : *plateau*, *grille*, *puzzle*... 

Pour la suite du projet, on choisit le nom de **grille** pour désigner le plateau de jeu et que nous définirons comme le conteneur de l'ensemble des tuiles du jeu.

Une **tuile** est un élement de jeu qui peut prendre une valeur comprise entre 2 et 2048 et telle que sa valeur est une puissance de 2 et qui peut être déplacée selon 4 directions dans la grille de jeu.

Un **déplacement** est une indication de la direction donnée par le joueur pour déplacer l'ensemble des tuiles de la grille de jeu.


Nous allons maintenant créer ces trois objets du point de vue informatique.

#### <span style="color: #26B260"> :clap: A ce stade du projet, vous avez atteint le JALON 2 : Analyse et Conception de mon produit </span> 

Vous pouvez maintenant passer à la [**Fonctionnalité 1** : Représenter une grille de jeu](./2048_S1_Grille.md)