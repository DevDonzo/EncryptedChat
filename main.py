import socket
import threading
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

# AES Encryption and Decryption class for secure communication
class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, plaintext):
        cipher = AES.new(self.key, AES.MODE_CBC)
        ciphertext = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
        return cipher.iv + ciphertext

    def decrypt(self, ciphertext):
        iv = ciphertext[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertext[AES.block_size:]), AES.block_size)
        return plaintext.decode('utf-8')

# Function to handle client communication for the server
def handle_client(client_socket, aes_cipher):
    try:
        while True:
            encrypted_message = client_socket.recv(1024)
            if not encrypted_message:
                print("Client disconnected.")
                break
            message = aes_cipher.decrypt(encrypted_message)
            print(f"Client: {message}")

            response = input("You: ")
            client_socket.send(aes_cipher.encrypt(response))
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client_socket.close()

# Server initialization
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("0.0.0.0", 9999))
    server.listen(5)
    print("Server is running on port 9999...")

    while True:
        client_socket, addr = server.accept()
        print(f"Connection established with {addr}")
        aes_cipher = AESCipher(get_random_bytes(16))
        client_socket.send(aes_cipher.key)
        threading.Thread(target=handle_client, args=(client_socket, aes_cipher), daemon=True).start()

# Function to handle server communication for the client
def receive_messages(client, aes_cipher):
    try:
        while True:
            encrypted_message = client.recv(1024)
            if not encrypted_message:
                print("Server disconnected.")
                break
            message = aes_cipher.decrypt(encrypted_message)
            print(f"Server: {message}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.close()

# Client initialization
def start_client(server_ip):
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, 9999))
    print("Connected to the server.")

    key = client.recv(16)
    aes_cipher = AESCipher(key)

    threading.Thread(target=receive_messages, args=(client, aes_cipher), daemon=True).start()

    try:
        while True:
            message = input("You: ")
            if message.lower() == "exit":
                print("Exiting chat.")
                break
            client.send(aes_cipher.encrypt(message))
    except KeyboardInterrupt:
        print("Closing chat.")
    finally:
        client.close()

# Entry point of the application
if __name__ == "__main__":
    print("Welcome to the Secure Chat Application!")
    choice = input("Start as server (s) or client (c): ").strip().lower()

    if choice == 's':
        start_server()
    elif choice == 'c':
        server_ip = input("Enter the server's IP address: ").strip()
        start_client(server_ip)
    else:
        print("Invalid choice. Please restart and choose 's' or 'c'.")
