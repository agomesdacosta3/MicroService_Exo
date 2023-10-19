# PROJET MICROSERVICE (mi-parcours)

## Sujet :

Le but de ce projet est la mise à dispotion d'un système de management de clients. Ce système intégrera 3 options principales qui sont l'ajout d'un client et la consultation d'un client spécifique ou de la liste entière des clients. La page d'accueil du projet regroupera ces 3 options et redirigera vers la page spécifique à l'option sélectionnée.


L'archtecture est faite sous la forme de microservices conteneurisé qui communiqueront entre eux via 2 réseaux (db & app). L'architecture globale est décrite à travers le schéma ci-dessous :

## Architecture globale :

![image](https://github.com/agomesdacosta3/MicroService_Exo/blob/main/Architecture.png)

Le service pgadmin et la base de données sont fournis par : https://github.com/pthom/northwind_psql 

## Technologies :

Les technologies de ce projet pour le front, back et BDD sont :
- HTML/CSS
- Javascript
- Python
  
Ces technologies ont été choisies pour leur simplicité, leur polyvalence et leur efficacité pour le développement d'applications web, en particulier pour des projets de petite à moyenne taille comme celui-ci. Ils offrent un excellent point de départ pour la mise en place rapide de pages web fonctionnelles, tout en laissant la possibilité d'ajouter des fonctionnalités plus avancées si l'application en demande.

- Postgres
- Docker

Le choix de Postgres est dû à l'exploitation de la base de données utilisée dans le projet et le choix de Docker est lui dû à la facilité de déploiement de l'application et aussi pour offre une gestion des dépendances logicielles plus simplifié. 

## Lien & Schéma BDD utilisé :

![image](https://github.com/agomesdacosta3/MicroService_Exo/blob/main/projet/ER.png)

A noter que le projet se concentre exclusivement sur la table 'customers'

## Build des images Docker :

build à partir du docker-compose : docker-compose up --build

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/a13f5e3e-f341-4f2f-af2f-e009741e7285)

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/29f8a5a4-9ddf-402a-a9d3-914cd8049e83)

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/d43ec230-a20c-4d11-b739-92d0716f4ada)

## Docker-Hub :

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/b39ae89f-e4f3-4612-9637-adf83848d8de)

Commandes pour récupérer les images : 
- docker pull agomesdacosta3/app
- docker pull agomesdacosta3/db


## Lancement du projet :

Le projet fonctionne en local :

1- Cloner ce repository
2- Lancer à partir du dossier projet la commande docker compose up -d --build
3- Le projet tourne sur : https://localhost/

## Fonctionnement du projet :

Voici la page d'accueil regroupant les 3 options évoqués dans le sujet :

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/7fc27849-2440-4aa1-93e7-3b9f1b3e1b7e)

# Option Add :

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/2d3b4812-0e9a-4c87-b5cd-d1216cc13aa5)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/d6888c13-fe3c-43b1-8a1b-dc7548c7e565)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/2264fd89-c21b-4ec0-89a8-4b217158c224)

# Option Get One :

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/56a82ec9-57ad-41a7-841f-5faf8c8cf43b)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/3d25d6de-b565-4181-b4f2-3e68a6394db4)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/84328ef9-b4a5-4696-a387-615154ff4e4d)


# Option Get All : (Ici limité aux 20 premiers éléments) : 

![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/12e0602c-e369-4646-98a3-7c4a9c7f6647)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/a3c1f779-d8ed-42fe-8f4e-fbc0ad314cf2)
![image](https://github.com/agomesdacosta3/MicroService_Exo/assets/60485510/6dca96b5-bf9e-4086-b998-2e3d87174216)
