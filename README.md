# RPC

## Overview of Application

This Simple RPC Client-Server-App implements a simple to-do list app for users. It allows users to add new tasks to their to-do list and to check the number of items in the list. The app is implemented using a client (echo-client.py) and a server (echo-server.py).

The server starts its connection and listens for other connections. The client also starts and connects with the server and prints that a connection has been established. The client then shows a welcome message to the user and asks what option they would like to take. Three options are given: 1. Add a task to the to-do list, 2: Check the size of the to-do list, and 3: Quit. The user has to enter either 1, 2 or 3 otherwise they will be prompted that their input is invalid and have to try again. 

When the user chooses to add a task, their choice is sent to the server which responds acknowledging receipt. The client then shows the server's acknowledgement and prompts the user to enter the task to be added. This task is sent back to the server which adds the task to the to do list and returns a message to the client whcih a success message and the updated to-do list. The client prints this out to the user. The user is then given the options again to either add a task, check the size of the list or quit.

When the user chooses to check the size of the list, their choice is sent to the server which responds acknowledging receipt. The server also responds with the size of the to-do list and the client prints out the server's responses for the user to see. The user is then prompted with the 3 options again to either add a task, check the size of the list or quit.

When the user chooses to quit, the request is sent to the server which responds with 'Goodbye!' The client and the server then stop executing.

Message Format
The client sends either 1, 2, or 3 to the server representing the 3 options the user can take after encoding. The server gets the options, decodes them and does the operations needed. The server then encodes its responses and sends them back to the client which decodes the messages and shows them to the user.

## Example Output:
### CLIENT
S-INF013241:Project1 smhanda$ python echo-client.py 
client starting - connecting to server at IP 127.0.0.1 and port 65432
connection established
This is the To-Do List App!
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 1
Request received, you want to add an item. Please add the item
Enter the task to add: Bake a cake
Task added, here is your task list: ['Bake a cake']
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 1
Request received, you want to add an item. Please add the item
Enter the task to add: Take a walk
Task added, here is your task list: ['Bake a cake', 'Take a walk']
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 1
Request received, you want to add an item. Please add the item
Enter the task to add: Watch TV
Task added, here is your task list: ['Bake a cake', 'Take a walk', 'Watch TV']
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 2
Request received, you want the length of your task list. The length of your task list is: 3
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: quit
Invalid choice. Please select a valid option.
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 1
Invalid request. Please choose 1 (Add), 2 (Check Length), or 3 (Quit).
Enter the task to add: Go fishing
Request received, you want to add an item. Please add the item
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 1
Task added, here is your task list: ['Bake a cake', 'Take a walk', 'Watch TV', 'Go fishing']
Enter the task to add: Listen to podcast
Request received, you want to add an item. Please add the item
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 2
Task added, here is your task list: ['Bake a cake', 'Take a walk', 'Watch TV', 'Go fishing', 'Listen to podcast']
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 2
Request received, you want the length of your task list. The length of your task list is: 5
Choose from these options:
1: Add a task
2: Check size of list
3: Quit
Enter your choice: 3
Request received, you want the length of your task list. The length of your task list is: 5
Client is done, exiting...
S-INF013241:Project1 smhanda$ 


### SERVER
S-INF013241:Project1 smhanda$ python echo-server.py 
server starting - listening for connections at IP 127.0.0.1 and port 65432

Connected established with ('127.0.0.1', 58191)
Request to add task received
Task added to list and sent back to client
Request to add task received
Task added to list and sent back to client
Request to add task received
Task added to list and sent back to client
Request to see length of task list received
Task list length calculated and sent back to client
Request to add task received
Task added to list and sent back to client
Request to add task received
Task added to list and sent back to client
Request to see length of task list received
Task list length calculated and sent back to client
Request to see length of task list received
Task list length calculated and sent back to client
server is done! exiting ....
S-INF013241:Project1 smhanda$ 


## Acknowledgements
I talked to Bridget Duah about the process of communication between the cleint and the server.
I utilized the starter code from the Professor.


