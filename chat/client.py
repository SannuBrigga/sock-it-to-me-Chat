import threading
import socket

def main():
    # Crear el socket del cliente con IPv4 y TCP
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

    try: 
        cliente.connect(('localhost', 7777))
    except:
        return print("\n⚠️No fue posible conectarse al servidor⚠️\n") 

    # Solicitar nombre de usuario
    username = input("Ingrese un nombre de usuario 👤: ")
    print("Conectado✅")

    # Crear y empezar los hilos para enviar y recibir mensajes
    thread1 = threading.Thread(target=receiveMsg, args=(cliente,))
    thread2 = threading.Thread(target=sendMsg, args=(cliente, username))
    thread1.start()
    thread2.start()

def receiveMsg(cliente):
    while True:
        try:
            msg = cliente.recv(1024).decode('utf-8')
            print(msg)
        except:
            print("\nNo está conectado⚠️")
            print("Presione <enter> para continuar▶️")
            cliente.close()
            break

def sendMsg(cliente, username):
    while True:
        try:
            msg = input()
            cliente.send(f"{username}: {msg}".encode('utf-8'))
        except:
            return

if __name__ == "__main__":
    main()
