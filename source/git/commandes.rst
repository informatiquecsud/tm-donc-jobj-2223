..  :git/commandes.rst:

Principales commandes ``git``
#############################

Pour utiliser git en lignes de commandes, il faut maîtriser certaines commandes
de base absolument indispensables.

..  list-table:: Principales commandes ``git``
    :widths: 40 60
    :align: left
    :header-rows: 1

    * - Commande ``git``
      - Description et précisions

    * - ``git init``
      - Initialiser un nouveau dépôt git sur la machine locale

    * - ``git add .``
      - Ajouter toutes les nouvelles modifications dans la zone de transit
        (*staging area*)

    * - ``git log``
      - Listes les différents commits contenus dans le dépôt avec leurs
        métadonnées (date de création, message de commit, hash SHA-1 etc.)
    
    * - ``git status``
      - Affiche l'état du dépôt (clean, dirty, ... ). Un dépôt ``clean``
        signifie qu'il n'y a pas de modifications non committées. En revanche,
        s'll y a de nouvelles modifications ou si la version locale du dépôt est
        en retard (on dit *behind*) la version sur Github, ces informations sont
        affichées par la commande ``status``.
    
    * - ``git commit -m "message de commit"``
      - Créer un nouveau commit accompagné du message ``message de commit`` noté
        entre guillemets. Ces messages sont ensuite visibles publiquement sur
        Github. Veillez donc à écrire des messages descriptifs et respectant
        toutes les règles de conduite de la plateforme Github (pas de propos
        racistes, sexistes, discrimantoires, etc.)

    * - ``git push``
      - Pousser les nouveaux commits sur GitHub afin qu'ils soient sauvés pour
        toujours et accessibles à tous (publiquement ou aux membres du projet
        selon les réglages).

..  admonition:: Remarque

    Il existe des montagnes de commandes ``git`` supplémentaires utilisées par
    les professionnels. Les commandes exposés ici suffisent largement pour nos
    besoins.