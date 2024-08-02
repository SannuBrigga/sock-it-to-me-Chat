import threading
import socket

clientes = []

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        server.bind(('localhost', 7777))  # Vincula el servidor a la dirección y puerto
        server.listen()  # Escucha conexiones entrantes
        print("Servidor iniciado en localhost:7777 ✅")
    except Exception as e:
        return print(f"No fue posible iniciar el servidor⚠️\n{e}")
    
    while True:
        cliente, addr = server.accept()
        clientes.append(cliente)
        print(f"Cliente conectado desde {addr} 🚀")

        thread = threading.Thread(target=respMsg, args=(cliente,))
        thread.start()

def respMsg(cliente):
    while True:
        try:
            msg = cliente.recv(1024)
            if not msg:
                break
            broadcast(msg, cliente)
        except Exception as e:
            print(f"Error al recibir mensaje: {e}")
            deleteClient(cliente)
            break

def broadcast(msg, cliente):
    for clientItem in clientes:
        if clientItem != cliente:
            try:
                clientItem.send(msg)
            except Exception as e:
                print(f"Error al enviar mensaje: {e}")
                deleteClient(clientItem)

def deleteClient(cliente):
    if cliente in clientes:
        clientes.remove(cliente)
        print(f"Cliente desconectado 🔌")

if __name__ == "__main__":
    main()
