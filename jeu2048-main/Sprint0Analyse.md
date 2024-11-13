# 2048 - Sprint 0 : Analyse du problème

Une des premières étapes de tout travail de programmation et de développement logiciel, quelque soit la méthodologie de développement utilisée, consiste à réaliser une rapide **analyse des besoins**, avant toute phase d'implémentation.

Cette analyse a pour objectif d'identifier les principales fonctionnalités à developper pour avoir le comportement souhaité du système développé. Cette première liste de fonctionnalités n'a pas besoin d'être exhaustive ni figée mais elle vous permettra de construire vos premiers développements.


## Analyse des besoins : les principales fonctionnalités

L'objectif ici est de permettre à un joueur (vous !) de **jouer le plus rapidement possible** au 2048 et il s'agira donc de concevoir un logiciel permettant de jouer au 2048 en mode console, sans interface graphique, sans gestion des joueurs. 

Le **[MVP (Minimum Viable product)](https://medium.com/creative-wallonia-engine/un-mvp-nest-pas-une-version-simplifi%C3%A9e-de-votre-produit-89017ac748b0)** de ce projet consistera à livrer une première version du jeu en mode console. Votre solution

+  **Permettra d'afficher proprement une grille de 4 x 4 dans laquelle seront placées aléatoirement 2 tuiles portant le nombre 2 ou 4 ainsi que les tuiles résultant du jeu**.
+  **Permettra de gérer plusieurs thèmes de jeux.** En particulier, nous considérerons les 3 thèmes ci-dessous et qui seront fournis sous la forme d'un dictionnaire python

```PYTHON
THEMES = {"0": {"name": "Default", 0: "", 2: "2", 4: "4", 8: "8", 16: "16", 32: "32", 64: "64", 128: "128", 256: "256", 512: "512", 1024: "1024", 2048: "2048", 4096: "4096", 8192: "8192"}, "1": {"name": "Chemistry", 0: "", 2: "H", 4: "He", 8: "Li", 16: "Be", 32: "B", 64: "C", 128: "N", 256: "O", 512: "F", 1024: "Ne", 2048: "Na", 4096: "Mg", 8192: "Al"}, "2": {"name": "Alphabet", 0: "", 2: "A", 4: "B", 8: "C", 16: "D", 32: "E", 64: "F", 128: "G", 256: "H", 512: "I", 1024: "J", 2048: "K", 4096: "L", 8192: "M"}}
```


+ **Permettra à l'utilisateur de jouer en lui demandant une direction parmi (bas, haut, droite, gauche)**. 
+ **Modifiera la grille de jeu en prenant en compte l'instruction du joueur et en effectuant les transformations nécessaires**. 
+  **Permettra de passer au coup suivant en faisant apparaitre aléatoirement un 2 ou un 4 dans une case vide**.
+  **Testera la fin du jeu  (gagné ou perdu) et affichera, dans tous les cas, le score obtenu**.

 
 D'autres fonctionnalités pourront bien sûr être ajoutées ensuite pour améliorer le jeu après avoir fini ce MVP mais en permettant le jeu, vous pourrez donc confronter rapidement votre produit à ses utilisateurs.

On peut donc esquisser à partir de cette analyse une première maquette comme ci-dessous.

![Vue du jeu 2048](./Images/2048_maquette.png)

Vous pouvez maintenant continuer par le [Sprint 0 : Reflexion autour de la conception](./Sprint0Conception.md).