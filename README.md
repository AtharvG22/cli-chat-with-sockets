# cli-chat-with-sockets

This project is a simple command-line interface (CLI) chat application built using Python, socket programming, and threading. It allows multiple clients to connect to a server and communicate with each other in real-time via WebSockets. The project consists of a server that manages client connections and clients that send/receive messages to/from the server.

Features
Multiple Clients: Supports multiple clients connecting to the server simultaneously.
Real-Time Messaging: Clients can send and receive messages in real-time.

Project Structure
server.py: Manages the WebSocket server, listens for client connections, and broadcasts messages to all connected clients.
client.py: Allows individual clients to connect to the server and communicate with other clients via the server.

Requirements
Ensure that you have Python installed on your system. You can download Python from here.

Installation and Setup
Follow these steps to run the project on your local machine:

1. Clone the Repository
Clone the repository to your local machine using the following command:
git clone <repository-url>

2. Navigate to the Project Directory
cd cli-chat-app

4. Running the Server
Run the server by executing the server.py file in :
python server.py
This will start the server on localhost (127.0.0.1) and port 12345.

4. Running the Client(s)
Run the client.py file to start the client instance:
python client.py
Each client needs to enter a username to join the chat. Multiple clients can be run on different terminal windows.
