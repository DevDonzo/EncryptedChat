# Secure Chat Application

**Made by Donzo**

## Description
The Secure Chat Application is a Python-based project enabling secure, encrypted communication between a server and multiple clients. It uses the AES encryption algorithm to ensure end-to-end security.

## Features
- **End-to-End Encryption**: AES encryption in CBC mode protects all messages.
- **Multi-Client Support**: The server handles multiple clients concurrently using threading.
- **Interactive Console**: Real-time, interactive message exchange for server and client.
- **Cross-Platform**: Compatible with Windows, macOS, and Linux.

## Technologies Used
- **Programming Language**: Python
- **Libraries**:
  - `socket`: Network communication.
  - `threading`: Handling multiple clients.
  - `pycryptodome`: AES encryption and decryption.

## How to Run
### Prerequisites
- Install Python 3.6 or later.
- Install the `pycryptodome` library by running:
  ```bash
  pip install pycryptodome
  ```

### Steps to Run the Server
1. Open a terminal.
2. Navigate to the project directory.
3. Run:
   ```bash
   python3 chat.py
   ```
4. Select `s` to start as the server.
5. The server listens on port 9999.

### Steps to Run the Client
1. Open another terminal.
2. Navigate to the project directory.
3. Run:
   ```bash
   python3 chat.py
   ```
4. Select `c` to start as the client.
5. Enter the server's IP address (`localhost` if running locally).
6. Begin chatting securely.

### Exit the Chat
- Type `exit` to close the session.

## Project Structure
```
secure-chat-app/
├── chat.py          # Main application script
├── README.md        # Project documentation
├── requirements.txt # Python dependencies
```

## Dependencies
- Python 3.6+
- `pycryptodome` library

## Example
**Server**: Hello, how can I help you?  
**You**: Hi, I have a question about encryption.  
**Server**: Sure, go ahead!  

## Future Improvements
- Support for file transfers.
- GUI implementation using Tkinter or PyQt.
- User authentication for enhanced security.
- Deploy the server on a public cloud (AWS, Azure).

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

