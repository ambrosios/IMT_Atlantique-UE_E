# Hello World

## Explication de git et github

<span style="color:green">**Définition Git :**</span> logiciel de gestion de versions décentralisé.

<span style="color:blue">**Définition GitHub :**</span> service en ligne qui permet d'héberger des dépôts ou repo Git.

### Principe de git
- on réalise les modifications un peu comme un arbre : quand on souhaite apporter une modification majeure ou réaliser un test, on peut créer une nouvelle branche. Les modifications qui seront réalisées sur cette branche ne seront pas reportées sur les autres.
- On peut créer des branches de branches.
- Lorsque la modification est ok, on peut la fusionner avec la branche dont elle découle. On parle alors de *merge*.
- On travaille localement dans le working directory. Lorsqu’on fait des modifications, on doit les indexer (*add*) puis créer une version (*commit*). Finalement, on pourra mettre en ligne (*push*).

![Illustration relation git/github](https://user.oc-static.com/upload/2021/10/05/16334576106761_image27.png)

### Commandes utiles
- créer une nouvelle branche :
    
 		$ git branch <nom de la branche>
        
- Lister les branches :

		$ git branch
		
- Se placer sur une branche :
        
        $ git checkout <nom de la branche>
        
- Vérifier les indexations : 
        
        $ git status 
        
- Indexer un élément : 
        
        $ git add <nom élément>
        
- Indexer tous les éléments non indexés : 
        
        $ git add -A
        
- Créer une version : 
        
        $ git commit -m ”<description de la version”
        
- Envoyer le commit sur le repo distant : 
        
        $ git push
        
- Récupérer un repo distant : 
        
        $ git clone <url du repo distant>

- Voir les branches distantes
        
        $ git branch -r

- Changer de branche pour une branche distante
        
        $ git switch <nom branche distante>

- Fusionner une branche : 
        
        $ git branch <branche à fusionner sur la branche courante>
        
- Récupérer la maj de la branche depuis le repo distant : 
        
        $ git pull
        
- Revenir sur un commit passé (reset) : 
        
        $ git reset

