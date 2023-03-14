import requests

#code goes here.

#CSPN = ?
#Jeremy.beaume@protonmail.com + Discord Guardia
#Fontion de HASH
#Ranbow Table stock data ayant créee les HASH, reverse-engineer entry data vi hash collisions
#Chffrer & Déchiffrrer vs Décrypter.
#Bon chiffrage = cle pas obtenable depuis un clair ni un chiffré
#RSA => 65 537 is convenient
#RSA + Sha256 = signature électronique
#Transmettre clé = Diffie-Hellman
#tiers de confiance
#poivre (code source) + sel + mot de passe

#LOGICIEL = message to person + message to group + users need password before acessing server info + is OPEN SOURCE

#CONDITIONS = http client/server comms + SSL/TLS non authorized for for comms encryption
# + Un logiciel de BDD arbitraire peut être utilisé (SQLite par exemple) + Le client doit permettre de configurer un serveur proxy (Burp), utilisé pour tester des attaques réelles.

#Attaquant Man-in-the-middle (done)
#Attaquant lecture server
#Attaquant administrateur du serveur

#Clés sont AES, trensmises via RSA.

"""Comment résoudre man-in-the-middle?"""
#On a le droit de stocker les clés dans le client. Sachant que le client est spécifique au serveur, on peut enlever l'attaquant 1 (man in the middle)
#Solutution: chiffrement asymetrique, dans le client se trouve la clé publique du serveur.
#Peu importe que l'attaquant voie la clé, puisque elle est publique. Clé privée du serveur pas transmise.

"""Comment résoudre lorsque l'attaquant peur lire le serveur?"""
#Lire serveur = lire clé privée?
#Serveur doit-être ignorant des messages clients.
#Créer une clé PUB pour chaque utilisateur, ils peuvent la partager sur le server mais C ne gagne rien a la voir puisque c'est une clé pub.
#Est-ce viable? / Clé publique pour groupes = identifient?

"""Comment résoudre lorsque l'attaquant est administrateur du serveur?"""
#Attacker 3 peut substituer les clés, ce qui rend la solution 2 inutile
#On nécessite d'un moyen d'authentification.
#Diffie Hellman? Charlie peut modifier les peinures publiques mais pas les privées.


"""
Man in the middle peut voir le clair, enjeu est l'échange de cle.
Attacker 2 peut lire le server, décripter dans le server es hors-question.
Attacker 3 peut substituer des clés, on nécessite d'un moyen d'authentification
Fichier AES... sans tiers de confiance.
"""

#ATTACKERS 1 & 2

# serveur transmet a A & B un client, le client inclu une clé pub pour communiquer avec C.
# ceci coupe l'attaquant 1 de la conversation
# A traver les canaux securisés, A transmet une Kpub(A) a B et B transmet une Kpub(B) à A.
# Attaquant 2 peut lire Kpub(A) et Kpub(B) mais ne peut rien faire avec
# Chaque user/groupe a sa propre Kpub