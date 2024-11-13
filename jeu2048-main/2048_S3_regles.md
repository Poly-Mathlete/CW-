# Fonctionnalité 4 : Gestion des déplacements des tuiles.



A ce stade du projet, on suppose que vous avez acquis une certaine autonomie dans la réalisation des différentes fonctionnalités et la suite du projet sera donc un peu moins guidée. 


## Etape 1 : déplacement d'une ligne de tuiles à gauche.

Pour gérer les déplacements des tuiles, une manière simple est de commencer par raisonner au niveau d'une ligne et de mettre en oeuvre le déplacement de cette ligne dans une direction horizontale donnée, par exemple le déplacement d'une ligne à gauche.

Nous allons donc écrire un test qui va permettre de tester le déplacement à gauche d'une ligne donnée. 



```PYTHON
def test_move_row_left():

    assert move_row_left([0, 0, 0, 2]) == [2, 0, 0, 0]
    assert move_row_left([0, 2, 0, 4]) == [2, 4, 0, 0]
    assert move_row_left([2, 2, 0, 4]) == [4, 4, 0, 0]
    assert move_row_left([2, 2, 2, 2]) == [4, 4, 0, 0]
    assert move_row_left([4, 2, 0, 2]) == [4, 4, 0, 0]
    assert move_row_left([2, 0, 0, 2]) == [4, 0, 0, 0]
    assert move_row_left([2, 4, 2, 2]) == [2, 4, 4, 0]
    assert move_row_left([2, 4, 4, 0]) == [2, 8, 0, 0]
    assert move_row_left([4, 8, 16, 32]) == [4, 8, 16, 32]
```

Dans quel module allez-vous écrire ce test et donc la ou les fonctions associées ?

La gestion des déplacements va concerner la grille de jeu et nous placerons donc les éléments correspondants à cette fonctionnalité dans le module `grid_2048`.



## Etape 2 : déplacement d'une ligne de tuiles à droite.


A l'aide de la fonction précédente `move_row_left(row)`, écrire la fonction `move_row_right(row)` qui permet de déplacer une ligne de tuiles à droite.

Un test correspondant pourrait être :

```PYTHON
def test_move_row_right():

    assert move_row_right([2, 0, 0, 0]) == [0, 0, 0, 2]
    assert move_row_right([0, 2, 0, 4]) == [0, 0, 2, 4]
    assert move_row_right([2, 2, 0, 4]) == [0, 0, 4, 4]
    assert move_row_right([2, 2, 2, 2]) == [0, 0, 4, 4]
    assert move_row_right([4, 2, 0, 2]) == [0, 0, 4, 4]
    assert move_row_right([2, 0, 0, 2]) == [0, 0, 0, 4]
    assert move_row_right([2, 4, 2, 2]) == [0, 2, 4, 4]
    assert move_row_right([2, 4, 4, 0]) == [0, 0, 2, 8]
    assert move_row_right([4, 8, 16, 32]) == [4, 8, 16, 32]
```

Regardez bien ces deux fonctions de tests. Cela devrait vous donner une astuce pour écrire la fonction `move_row_right` permettant de passer le test précédent.


## Etape 3 : déplacement de la grille selon une instruction `d`

Il s'agit d'écrire ici la fonction `move_grid(grid,d)` qui déplace l'ensemble des tuiles de la grille `grid` selon une direction donnée `d`.

Astuce : pour les déplacements verticaux, vous pouvez utiliser une transformation sur votre grille, qui vous permettra d'utiliser les fonctions précédentes.


Vous pourrez utiliser le test ci-dessous pour tester votre fonction de déplacement de la grille.


```PYTHON

def test_move_grid():
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"left") == [[4,0,0,0], [8, 0, 0, 0], [16, 0, 0, 0], [4, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [4, 4, 0, 0], [8, 0, 8, 0], [0, 2, 2, 0]],"right") == [[0,0,0,4], [0, 0, 0, 8], [0, 0, 0, 16], [0, 0, 0, 4]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"up") == [[4,8,4,2], [16, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    assert move_grid([[2,0,0,2], [2, 4, 0, 0], [8, 4, 2, 0], [8, 2, 2, 0]],"down") == [[0, 0, 0, 0], [0, 0, 0, 0],[4,8,0,0],[16, 2, 4, 2]]
```

Nous avons maintenant terminé cette fonctionnalité, il vous faut :

+ <span style='color:blue'>Faire un commit</span> 
+ <span style='color:blue'>Faire l'étape de revue et de synchronisation.</span> 


 Nous allons pouvoir maintenant nous intéresser à la suite de la conception de la logique du jeu en elle-même par le test de la fin du jeu.
Il s'agit de la [**Fonctionnalité 5** : Tester la fin du jeu](./2048_S3_Finjeu.md).






 







