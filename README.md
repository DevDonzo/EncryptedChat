Secure Chat Application

Made by Donzo

Description

The Secure Chat Application is a Python-based project designed to facilitate secure, encrypted communication between a server and multiple clients. It leverages the AES encryption algorithm to ensure end-to-end security for transmitted messages.

Features

End-to-End Encryption: Messages are encrypted using AES (Advanced Encryption Standard) in CBC mode.

Multi-Client Support: The server can handle multiple clients concurrently using threading.

Interactive Console: Both server and client interfaces provide real-time, interactive message exchange.

Cross-Platform: Compatible with Windows, macOS, and Linux.

Technologies Used

Programming Language: Python

Libraries:

socket (Built-in): For network communication.

threading (Built-in): For handling multiple clients.

pycryptodome: For AES encryption and decryption.

How to Run

Prerequisites

Python 3.6 or later installed on your system.

pycryptodome library installed. To install it, run:
pip install pycryptodome

Steps to Run the Server

Open a terminal.

Navigate to the project directory.

Run the following command:
python3 chat.py

Select s when prompted to start as the server.

The server will start listening on port 9999.

Steps to Run the Client

Open another terminal.

Navigate to the project directory.

Run the following command:
python3 chat.py

Select c when prompted to start as the client.

Enter the server's IP address (use localhost if running on the same machine).

Start chatting securely!

Exiting the Chat

Type exit to close the chat session gracefully.

Project Structure

secure-chat-app/
├── chat.py          # Main application script
├── README.md        # Project documentation
├── requirements.txt # Python dependencies

Dependencies

Python 3.6+

pycryptodome library

Example

Server: Hello, how can I help you?
You: Hi, I have a question about encryption.
Server: Sure, go ahead!

Future Improvements

Add support for file transfers.

Implement a GUI using Tkinter or PyQt.

Add user authentication to enhance security.

Deploy the server on a public cloud (e.g., AWS, Azure).

License

This project is licensed under the MIT License. See the LICENSE file for more details.

