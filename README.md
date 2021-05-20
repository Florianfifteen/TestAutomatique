##Repo TestAutomatique

FlorianRobache

## Avant de commencer ⚠

Il faut avoir :
- Python3
- Pip3

Une fois les outils acquis, exécutez cette commande (dans un terminal VS code):

```````````````````````````
pip3 install -r required.txt
```````````````````````````

## Création de la base de donnée

Créer maintenant la base de donnée MongoDB, en exécutant la commande suivante :
````````````
use apiperson
````````````

Ensuite vérifier la base de données actuellement sélectionnée, utilisez la commande :

```
db
```

Pour vérifier la liste des bases de données, utilisez la commande:

``````
show dbs
``````

Notre base de données créée « apiperson » ne figure pas dans la liste, insérez-y au moins un document pour afficher la base de données. Ensuite supprimez tous les documents

Retournez sur la liste des DB :

``````
show dbs
``````

Votre base de donnée est désormais active.

## Utiliser l'interface
Il suffit de se rendre dans le dossier racine de l'API et exécutez cette commande :
``````````````````
python3 api-person.py
``````````````````
L'API PERSON se lance, rejoignez la en ligne via l'adresse web donnée par la console python. Vous pourrez dont ajouter ou supprimer une ou plusieurs personne(s).

Pour observer les personnes disponibles, ajoutez "/personne" à l'url de base.
```````````````
127.0.0.1/personne
```````````````
ou
```````````````
localhost/personne
```````````````
