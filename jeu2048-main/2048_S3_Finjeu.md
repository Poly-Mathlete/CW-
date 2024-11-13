# Fonctionnalité 5 : Tester la fin du jeu.


Il s'agit d'écrire ici les fonctions nécéssaires pour tester la fin du jeu c'est à dire que la grille est pleine ou qu'il n'y a plus aucun mouvement possible.




## Etape 1 : Tester si la grille est pleine.


Ecrire la fonction `is_grid_full(grid)` qui permet de tester si la grille est pleine ou non.

Ecrire le test unitaire pour cette fonction dans votre fichier de test.


## Etape 2 : Tester s'il y a encore des mouvements possibles.

Ecrire la fonction `move_possible(grid)` qui teste pour chacune des directions possibles si le mouvement est possible et qui renvoie une liste de booléens.

Votre fonction devrait permettre de passer le test ci-dessous

```PYTHON
def test_move_possible():
    assert move_possible([[2, 2, 2, 2], [4, 8, 8, 16], [0, 8, 0, 4], [4, 8, 16, 32]]) == [True,True,True,True]
    assert move_possible([[2, 4, 8, 16], [16, 8, 4, 2], [2, 4, 8, 16], [16, 8, 4, 2]]) == [False,False,False,False]
```

## Etape 3 : Tester la fin du jeu

Ecrire la fonction `is_game_over(grid)` qui permet de tester si le jeu est terminé ou non en fonction de l'état de la grille.

## Etape 4 : Tester si le jeu est gagnant ou pas.

Pour finir cette fonctionnalité, il faut maintenant pouvoir tester si le jeu obtenu est gagnant ou pas. Une configuration gagnante est une configuration telle qu'il y a dans la grille une tuile dont la valeur est supérieure ou égale à 2048.

Il faut donc doter votre programme d'une fonction `get_grid_tile_max()` qui renvoie la plus grande valeur des tuiles de la grille.



Nous avons maintenant terminé cette fonctionnalité, il vous faut :

+ <span style='color:blue'>Faire un commit</span> 
+ <span style='color:blue'>Faire l'étape de revue et de synchronisation</span> 



Nous avons maintenant tous les ingrédients pour jouer à notre jeu. Il s'agit de la **Fonctionnalité 6** : [Mettre en orchestre le jeu](./2048_S4_Playing.md)




