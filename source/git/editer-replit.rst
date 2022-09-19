.. _git/editer-replit.rst:

Éditer sur repl.it
##################

..  
    Vidéo Youtube qui montre comment forker un dépôt

    id = HzFDzYofxlI

Il s'avère que l'environnement gitpod pose certains problèmes, notamment au
niveau de la collaboration en temps réel. En effet, lorsque deux personnes
éditent un même fichier en même temps, chaque personne travaille ensuite dans
des versions différences qui ne sont plus synchronisées.

Créer un compte sur repl.it
===========================

Assurez-vous d'être connecté avec Github avec le navigateur Web que vous
utilisez.

#.  Rendez-vous ensuite sur le site https://repl.it et créez-vous un nouveau compte
    à l'aide de votre compte Github (cliquer sur le bouton **Start coding**).

    ..  figure:: signup-replit.png
        :align: center
        :width: 90%

        Création d'un compte sur repl.it avec GitHub

#.  Cliquez ensuite sur **Continue with Github**

    ..  figure:: signup-replit-with-github.png
        :align: center
        :width: 90%

        Utilisation du compte Github pour créer un compte sur repli.it

Créer un nouveau workspace (REPL) sur repl.it
=============================================

Créez ensuite un nouveau REPL (espace de travail en important le dépôt git que
vous voulez éditer):

..  admonition:: Procédure

    #.  Cliquez sur le bouton **+ Create**
    #.  Cliquez sur le bouton **import from GitHub**
    #.  Collez l'URL du dépôt Github que vous voulez importer dans REPL.it
    #.  Cliquez sur le bouton **Import from GitHub**
    
..  figure:: replit-import-github-repo.png
    :align: center
    :width: 90%

    Importation d'un dépôt Github dans https://repl.it


..  admonition:: Présentation en vidéo

    ..  youtube:: N4mWgWzNQzM
        :width: 635
        :height: 360
        :divid: import-repo-in-replit

Obtenir le rendu de la page Web
===============================

Pour pouvoir observer le rendu de la page, il faut tout d'abord que la page
``index.html`` soit accessible, ce qui implique de démarrer un serveur HTTP qui
sert le fichier ``index.html``.

Lancer le serveur de développement
==================================

Pour pouvoir éditer des pages Web avec REPL.it, il faut appliquer le même
principe que pour gitpod.io, à savoir démarrer un serveur HTTP de développement.
Pour cela, il faut aller dans la partie **Console** et insérer la commande

::

    python -m http.server

..  admonition:: Présentation en vidéo

    ..  youtube:: O1RLg4fSJPQ
        :width: 635
        :height: 360
        :divid: start-dev-http-server

Enregistrer les modifications sur GitHub
========================================

Une fois que vous avez fait vos modifications, il faut les "committer" et les
pousser sur GitHub. Pour ce faire, il y a deux manières de faire.

..  admonition:: La manière simple avec l'interface graphique

    Pour pousser les modifications sur GitHub, on peut utiliser l'interface
    graphique.

    ..  youtube:: U5d-o_N-b4Q
        :width: 635
        :height: 360
        :divid: push-changes-to-github-repository

..  admonition:: La manière "pro" avec les commandes ``git``

    Il est également possible de pousser les modifications sur GitHub avec les
    commandes suivantes, à saisir dans l'onglet **Shell**

    ::

        git add .
        git commit -m "description des modifications"
        git push

    ..  figure:: push-changes-to-github-with-git-commands.png
        :align: center
        :width: 90%




Collaborer à plusieurs personnes en temps réel
==============================================

Contrairement à gitpod, qui ne permet pas une réelle collaboration en temps
réel, l'environnement REPL.it gère beaucoup mieux la collaboration en temps
réel. Le principe est exactement le même que pour Gitpod : il suffit de partager
le workspace (REPL) et envoyer le lien de partage à l'autre personne.

..  admonition:: Explications en vidéo

    ..  youtube:: LIicXqwZ1cc
        :width: 635
        :height: 360
        :divid: replit-realtime-collaboration