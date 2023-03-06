# Un client à utiliser avec le serveurSimple.py
import socket

# 1- Construire un objet qui représente la socket
#    vers laquelle le client veut se connecter
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2- ouvrir la connection vers la socket
s.connect(('127.0.0.1', 2003))

# 3- lire 15 octet sur la socket (augmenter pour lire plus...)
data = s.recv(150)

# 4 - Message de bienvenue
# Convertir le tableau de 15 octets en une chaine de caractère
#    et l'afficher.
print("> " + data.decode('utf-8'))

print("\n<FIN> pour terminer la connexion\n\n")

# Réception du serveur
data = s.recv(150)
print("> " + data.decode('utf-8'))

# 5 - Echanges avec le serveur
while 1:

    # Lecture du message à envoyer
    ch = input()

    # Si le clienht veut mettre FIN
    if ch.upper() == 'FIN':
        s.send("FIN".encode('UTF-8'))
        break
    else:
        # Envoi du message
        s.send(ch.encode('UTF-8'))

        # Reception de l'ECHO du serveur
        data = s.recv(150)
        print("> " + data.decode('utf-8'))

    # Réception du prompt serveur
    data = s.recv(150)
    print("> " + data.decode('utf-8'))

# Fin de la connexion
data = s.recv(150)
print("> " + data.decode('utf-8'))

s.close()