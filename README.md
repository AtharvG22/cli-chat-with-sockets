# CLI Chat Application with Sockets

This project is a simple **command-line interface (CLI) chat application** built using Python, socket programming, and threading. It allows multiple clients to connect to a server and communicate with each other in real-time. The server manages client connections, while clients send and receive messages via sockets.

## Features
- **Multiple Clients**: Supports multiple clients connecting to the server simultaneously.
- **Real-Time Messaging**: Clients can send and receive messages instantly, with updates broadcast to all connected users.

## Project Structure
- **`server.py`**: Manages the server-side operations, listens for client connections, and broadcasts messages to all connected clients.
- **`client.py`**: Each client connects to the server and interacts with other users by sending/receiving messages through the server.

## Requirements
Ensure you have **Python** installed on your system. You can download Python from the official site: [Python.org](https://www.python.org/downloads/).

### Required Python Modules
The project uses Python’s built-in modules:
- **socket**: For establishing network connections.
- **threading**: To manage multiple clients concurrently.

## Installation and Setup
Follow these steps to set up and run the project on your PC:

### 1. Clone the Repository
First, clone the repository to your local machine using the following command:
```bash
git clone <repository-url>
```

### 2. Navigate to the Project Directory
After cloning, navigate to the project directory:
```bash
cd cli-chat-app
```

### 3. Running the Server
To start the server, run the `server.py` file:
```bash
python server.py
```
This will start the server on `localhost (127.0.0.1)` and port `12345`.

### 4. Running the Client(s)
To start a client instance, run the `client.py` file:
```bash
python client.py
```
Each client needs to enter a username to join the chat. Multiple clients can be run on different terminal windows.

### Example
1. **Start the server** in one terminal window:
   ```bash
   python server.py
   ```
2. **Start multiple clients** by opening separate terminal windows for each client and running:
   ```bash
   python client.py
   ```

Clients will be prompted to enter a username, and once connected, they can start sending messages that will be broadcast to all other connected clients.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.
