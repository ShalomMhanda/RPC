#!/usr/bin/env python3

import socket

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

todo_list = []
def run_server():
    print("server starting - listening for connections at IP", HOST, "and port", PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"\nConnected established with {addr}")
            while True:
                request = conn.recv(1024).decode('utf-8')

                if not request:
                    break

                if request == '1':  # Add task
                    print("Request to add task received")
                    conn.send("Request received, you want to add an item. Please add the item".encode('utf-8'))
                    task = conn.recv(1024).decode('utf-8')
                    add_task(task)
                    conn.send(f"Task added, here is your task list: {todo_list}".encode('utf-8'))
                    print("Task added to list and sent back to client")
                elif request == '2':  # Add task
                    print("Request to see length of task list received")
                    conn.send(f"Request received, you want the length of your task list. The length of your task list is: {len(todo_list)}".encode('utf-8'))
                    print("Task list length calculated and sent back to client")
                elif request == '3':  # Quit
                    conn.send("Goodbye!".encode('utf-8'))
                    break
                else:
                    conn.send("Invalid request. Please choose 1 (Add), 2 (Check Length), or 3 (Quit).".encode('utf-8'))
                
def add_task(task):
    todo_list.append(task)
    return todo_list
                     

if __name__ == "__main__":
    run_server()
    print("server is done! exiting ....")


