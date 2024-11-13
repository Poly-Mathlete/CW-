# Fonctionnalité 3 : Faire jouer le joueur.


L'objectif de cette fonctionnalité est de rendre le jeu interactif en permettant à un joueur de donner ses instructions de jeu. Pour ce MVP, nous nous contenterons d'instructions textuelles que l'utilisateur donnera via l'entrée standard.

On peut prendre, ici, un peu le temps de réflechir à la conception de notre jeu. Dans le **Sprint 1**, nous avons défini dans le module `grid_2018` de notre projet, un ensemble de fonctions qui vont nous permettre de manipuler notre grille de jeu. Ce module a été conçu sans prendre en compte l'aspect interaction du jeu et on peut donc penser que ce module a un caractère générique, quelles que soient les modalités d'interaction.

Ici, pour cette fonctionnalité, nous cherchons à mettre en place les interactions avec le joueur et selon que l'on utilise des interactions textuelles ou une interface graphique et les évènements associés, on risque donc d'avoir une solution spécifique au type d'interaction. 

Cette reflexion doit donc vous amener à définir un nouveau module pour cette partie du projet. Nous appelerons ici ce module `textual_2048` et il s'agit donc de rajouter un fichier `textual_2048.py`à votre projet. Dans une démarche de qualité logicielle, vous pouvez aussi tout de suite ajouter un fichier `test_textual_2048.py`dans lequel vous définirez les tests associés.

Nous vous rappelons que dans le jeu 2048, le joueur doit et ne peut uniquement choisir que entre 4 directions (haut, bas, gauche, droite). 

Cette fonctionnalité est donc très simple à mettre en place, avec la fonction prédéfinie `input` de python mais, à nouveau, nous vous proposons de le faire de manière itérative.




## Etape 1 : Demander à l'utilisateur son choix de direction.

Pour cette étape, nous n'allons pas appliquer la démarche TDD car écrire un test qui teste une fonction faisant appel à `input`n'est pas facile à écrire.

Supposons que vous ayez donc écrit dans le fichier `textual_2048.py` la fonction `read_player_command` qui est la solution la plus simple (mais pas la plus robuste) pour la fonctionnalité demandée.

```PYTHON
def read_player_command():
    move = input("Entrez votre commande (g (gauche), d (droite), h (haut), b (bas)):")
    return move
```

Pour tester cette fonction avec `pytest`ou tout autre utilitaire de test python, il est nécessaire de pouvoir faire un **mock** de la fonction prédéfinie `input`. En programmation, il s'agit d'un principe qui consiste à définir des fonctions qui ont comme objectif d'imiter le comportement d'autres objets que nous ne voulons pas tester (comme par exemple une requête à une API externe).

Pour bien comprendre, l'intérêt des **mocks** pour le test, vous pouvez prendre le temps de regarder le [tutorial d'OpenClassRooms](https://openclassrooms.com/fr/courses/4425126-testez-votre-projet-avec-python/4435224-utilisez-des-mocks) à ce sujet. D'autres tutoriaux peuvent aussi vous aider ici à ecrire ce test comme [ici](https://codefellows.github.io/sea-python-401d7/lectures/mock.html) ou plus généralement [ici](https://changhsinlee.com/pytest-mock/).

Pour tester notre fonction `read_player_command()` avec pytest il faut donc :

+ Utiliser le helper [`monkeypatch`](https://docs.pytest.org/en/latest/monkeypatch.html) de pytest.
+ Définir une fonction  `mock_input_return(obj)`  qui prendra en paramètre l'objet sur lequel nous allons appeler la méthode
+ Utiliser la méthode `monkeypatch.setattr()`pour simuler un joueur entrant son choix de direction sur l'invite de commande.

Avec ce principe, ecrivez le test permettant de tester la fonction `read_player_command()`.

#### <span style="color: #26B260">A ce stade du projet, vous avez atteint le JALON 7 : Savoir faire un mock pour le test </span> 

## Etape 2 : Demander à l'utilisateur et vérifier son choix de direction.

Dans l'étape précédente, nous n'avons pas évoqué le cas où l'utilisateur rentre une commande de jeu qui n'est pas valide. 

Dans cette étape, il faut donc améliorer la fonction `read_player_command()`de telle sorte que si la commande donnée n'est pas correcte, il sera demandé à l'utilisateur de re-saisir son choix de jeu.


## Etape 3 : Permettre à l'utilisateur de choisir la taille de la grille de jeu ainsi que le thème du jeu.

La dernière étape pour cette fonctionnalité est de permettre à l'utilisateur de choisir aussi une taille pour la grille de jeu ainsi que le thème d'affichage.

Une première question à vous poser pour cette étape concerne la conception de votre programme.

Faut-il définir de nouvelles fonctions pour permettre ces deux choix ou est-ce qu'une modification de la fonction `read_player_command()` suffit ?


Dans le déroulé du jeu, la fonction `read_player_command()` va être appelée à chaque coup du joueur. Alors, que proposez-vous ?

Nous allons bien évidemment définir deux autres fonctions qu'il faudra  pour saisir la taille de la grille voulue par le joueur (`read_size_grid()`) et le thème choisi (`read_theme_grid()`).


Comme à chaque fin de sprint de fonctionnalité, il vous faut :

+ <span style='color:blue'>Faire un commit</span> 
+ <span style='color:blue'>Faire les étapes de revue et de synchronisation </span> 



 Nous allons pouvoir maintenant nous intéresser à la conception de la logique du jeu en elle-même par la gestion du déplacement des différentes tuiles.
Il s'agit de la [**Fonctionnalité 4** : Gestion des déplacements](./2048_S3_regles.md)






