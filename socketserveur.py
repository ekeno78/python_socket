# Définition d'un serveur simple
# Le serveur attend la connexion d'un client et fait un echo des messages reçu

import socket, sys

# Adresse ip et port de la socket sur laquelle va ecouter le serveur
# A ADAPTER A VOTRE MACHINE, vous pouvez mettre 0.0.0.0 pour écouter sur toutes les adresses IP du serveur
# quelle est la conséquence d'écouter sur 127.0.0.1 ?
HOST = '127.0.0.1'
PORT = 2003

# 1) Il faut créer la socket en indiquant les protocoles (ici IP et TCP)
mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2) puis effectuer la liaison (bind)
try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

# 3) Un serveur est souvent une boucle infinie qui attend des connexions.
while 1:
    # 4) Le serveur se bloque en attente de la requête de connexion d'un client
    print(" **** Serveur simple en attente... ****")
    mySocket.listen(5)

    # 5) Il est débloqué lors de l'établissement de la connexion
    connexion, adresse = mySocket.accept()
    print("Un client est connecté depuis l'adresse IP %s et le port %s" % (adresse[0], adresse[1]))

    # 6) Envoi d'un message de bienvenue au client
    # Attentionn la chaine de caractère DOIT etre convertie en un tableau d'octets
    #    le paramète 'UTF-8" indique l'encodage des caratère qui doit être utilisé.
    connexion.send(("Vous êtes connecté au serveur "+HOST+":"+str(PORT)+".\n").encode('UTF-8'))


    # Le serveur commence maintenant un echange avec le client connecté
    while 1:
        # envoi de la question au client
        connexion.send("Votre message ?\n".encode('UTF-8'))
        # attente de la reponse
        msgClient = connexion.recv(1024)
        # le message est converti d'une tableau d'octets en chaine de caractères
        msgClient = msgClient.decode("utf-8")

        # si la reponse est FIN ou un ligne vide, le dialogue d'arrête.
        if msgClient.upper().strip() == "FIN" or msgClient.strip() == "":
                break

        # traitement de la réponse
        # le serveur affiche sur sa console
        print("Reçu du client >"+msgClient+"<")
        # et envoi un echo au client
        connexion.send(("ECHO : "+msgClient).encode('UTF-8'))

    # 7) Si l'on est sorti de la boucle il faut terminer
    connexion.send("Good Bye.".encode('UTF-8'))
    print("Connexion interrompue.")

    # Le serveur ferme la connexion
    connexion.close()

    ch = input("Attendre un autre client ? <R>ecommencer <T>erminer ? ")
    if ch.upper() =='T':
            break