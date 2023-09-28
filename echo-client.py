#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server


"""
Building a simple RPC
Make a data structure that stores a to-do list and the client requests the server to add or remove tasks from there 
In the client, ask the user if they want to 1: Add a task, 2: Remove a Task, 3: Quit
If the client says quit, quit
If the client says add, send the request to the server which echoes a message to the client saying "Request received, you want to add an item. Please add the item"
    The client then allows the user to add a task and sends it to the server
    The server responds with a message "Task added, here is your task list" and prints the list of tasks
If the client says remove, send the request to the server which echoes a message to the client saying "Request received, you want to remove a task. Choose which task to remove"
    The client then shows the list of tasks from the server and the user can choose which task to remove
    The server get the message of what is to be removed and removes and echoes a message saying it has been removed and shows the new list
Keep going until quit is typed in

"""


def run_client():
    print("client starting - connecting to server at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        print(f"connection established")
        while True:
            # loop until the user asks to quit
            if not talk_to_server(s):
                break

        while True:
                
            if cmd == "1":
                string = input("\nEnter the String you want to add:\n")
                msg = "add " + string
            elif cmd == "2":
                string = input("\nEnter the string you want to delete:\n")
                msg = "delete " + string
            elif cmd == "3":
                msg = "returnAll Nothing"

            print(f"sending message '{msg}' to server")
            sock.sendall(msg.encode('utf-8'))
            print("message sent, waiting for reply")
            reply = sock.recv(1024)
            if not reply:
                return False
            else:
                print(f"received reply '{reply}' from server")
                return reply

def talk_to_server(sock):
    print("This is the To-Do List App!")
    while True:
        print("Menu:")
        print("1: Add a task")
        print("2: Remove a task")
        print("3: Quit")

        choice = input("Enter your choice: ")

        if choice == '3':
            print("Client quitting at operator request.")
            return False
        elif choice in ['1','2']:
            break
        else:
            print("Invalid choice. Please select a valid option.")

        
    sock.send(choice.encode('utf-8'))
    
    if choice == '1':
        task = input("Enter the task to add: ")
        response = sock.recv(1024).decode('utf-8')
        print(response)
        task = input("Enter the task to add: ")
        sock.send(task.encode('utf-8'))
        response = sock.recv(1024).decode('utf-8')
        print(response)
    elif choice == '2':
        response = sock.recv(1024).decode('utf-8')
        print(response)
        task_list = sock.recv(1024).decode('utf-8')
        print(task_list)
        task_to_remove = input("Enter the task to remove: ")
        sock.send(task_to_remove.encode('utf-8'))
        response = sock.recv(1024).decode('utf-8')
        print(response)
        task_list = sock.recv(1024).decode('utf-8')
        print(task_list)
        print("herrrrrrrreeeeeeee")
    elif choice == '3':
        response = sock.recv(1024).decode('utf-8')
        print(response)
        return False
    else:
        print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    run_client()
    print("Client is done, exiting...")

