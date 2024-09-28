# import required modules
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext
from tkinter import messagebox

HOST = '127.0.0.1'
PORT = 12345

DARK_GREY = '#1C1C1C'
LIGHT_GREY = '#2C2C2C'
OCEAN_BLUE = '#007ACC'
WHITE = "white"
FONT = ("Helvetica", 16)
BUTTON_FONT = ("Helvetica", 14)
SMALL_FONT = ("Helvetica", 12)

# Creating a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def add_message(message):
    message_box.config(state=tk.NORMAL)
    message_box.insert(tk.END, message + '\n')
    message_box.config(state=tk.DISABLED)

def connect():
    try:
        client.connect((HOST, PORT))
        print("Successfully connected to server")
        add_message("[SERVER] Successfully connected to the server")
    except:
        messagebox.showerror("Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")

    username = username_textbox.get()
    if username != '':
        client.sendall(username.encode())
    else:
        messagebox.showerror("Invalid username", "Username cannot be empty")

    threading.Thread(target=listen_for_messages_from_server, args=(client, )).start()

    username_textbox.config(state=tk.DISABLED)
    username_button.config(state=tk.DISABLED)

def send_message():
    message = message_textbox.get()
    if message != '':
        client.sendall(message.encode())
        message_textbox.delete(0, len(message))
    else:
        messagebox.showerror("Empty message", "Message cannot be empty")

root = tk.Tk()
root.geometry("700x650")
root.title("Messenger Client")
root.config(bg=LIGHT_GREY)

# Layout configuration for better aesthetics
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=5)
root.grid_rowconfigure(2, weight=1)

# Top Frame (for username)
top_frame = tk.Frame(root, bg=DARK_GREY, pady=20)
top_frame.grid(row=0, column=0, sticky="ew", padx=10, pady=10)

username_label = tk.Label(top_frame, text="Enter username:", font=FONT, bg=DARK_GREY, fg=WHITE)
username_label.pack(side=tk.LEFT, padx=10)

username_textbox = tk.Entry(top_frame, font=FONT, bg=LIGHT_GREY, fg=WHITE, width=23, borderwidth=2, relief="solid")
username_textbox.pack(side=tk.LEFT, padx=10)

username_button = tk.Button(top_frame, text="Join", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=connect)
username_button.pack(side=tk.LEFT, padx=10)

# Middle Frame (for chat messages)
middle_frame = tk.Frame(root, bg=LIGHT_GREY)
middle_frame.grid(row=1, column=0, sticky="nsew", padx=10)

message_box = scrolledtext.ScrolledText(middle_frame, font=SMALL_FONT, bg=DARK_GREY, fg=WHITE, width=80, height=28, borderwidth=2, relief="solid")
message_box.config(state=tk.DISABLED)
message_box.pack(side=tk.TOP, padx=10, pady=10)

# Bottom Frame (for sending messages)
bottom_frame = tk.Frame(root, bg=DARK_GREY, pady=20)
bottom_frame.grid(row=2, column=0, sticky="ew", padx=10, pady=10)

message_textbox = tk.Entry(bottom_frame, font=FONT, bg=LIGHT_GREY, fg=WHITE, width=50, borderwidth=2, relief="solid")
message_textbox.pack(side=tk.LEFT, padx=10)

message_button = tk.Button(bottom_frame, text="Send", font=BUTTON_FONT, bg=OCEAN_BLUE, fg=WHITE, command=send_message)
message_button.pack(side=tk.LEFT, padx=10)

# Function to listen for incoming messages from the server
def listen_for_messages_from_server(client):
    while 1:
        message = client.recv(2048).decode('utf-8')
        if message != '':
            username = message.split("~")[0]
            content = message.split('~')[1]
            add_message(f"[{username}] {content}")
        else:
            messagebox.showerror("Error", "Message received from client is empty")

# Main function
def main():
    root.mainloop()

if __name__ == '__main__':
    main()
