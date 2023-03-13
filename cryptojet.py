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

#Attaquant Man-in-the-middle
#Attaquant lecture server
#Attaquant administrateur du serveur

#on a le droit de stocker les clés dans le client. Sachant que le client est spécifique au serveur, on peut enlever l'attaquant 1 (man in the middle)
#Solutution: chiffrement asymetrique, dans le client se trouve la clé publique du serveur

""""
Man in the middle peut voir le clair, enjeu est l'échange de cle.
Fichier AES... sans tiers de confiance.
"""