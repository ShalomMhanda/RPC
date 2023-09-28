#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break


def talk_to_server(sock):
    choice = ''
    print("This is the To-Do List App!")
    while True:
        print("Choose from these options:")
        print("1: Add a task")
        print("2: Check size of list")
        print("3: Quit")

        choice = input("Enter your choice: ")
        
        sock.send(choice.encode('utf-8'))
        
        if choice == '1':
            response = sock.recv(1024).decode('utf-8')
            print(response)
            task = input("Enter the task to add: ")
            sock.send(task.encode('utf-8'))
            response = sock.recv(1024).decode('utf-8')
            print(response)
        elif choice == '2':
            response = sock.recv(1024).decode('utf-8')
            print(response)
        elif choice == '3':
            response = sock.recv(1024).decode('utf-8')
            print(response)
            return False
        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    run_client()
    print("Client is done, exiting...")

