##module to be imported to run to build and start honeypots.

import socket
import threading

def handle_connection(client_socket, client_address):
    print(f'Connection attempt from: {client_address[0]}:{client_address[1]}')
    response = 'Welcome to the honeypot!\n'
    client_socket.send(response.encode())
    client_socket.close()

def start_honeypot(port):
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('0.0.0.0', port))
        server_socket.listen(1)
        print(f'Honeypot listening on port {port}...')

        while True:
            client_socket, client_address = server_socket.accept()
            threading.Thread(target=handle_connection, args=(client_socket, client_address)).start()

    except Exception as e:
        print(f'Error occurred: {str(e)}')

if __name__ == '__main__':
    start_honeypot(8080)
