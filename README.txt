## Descrpition
1. Run the server.py specifiying number of clients
2. Clients have initiate the connection and get an id.
3. after each iteration the model gets upload to server, the server aggreate each client model and return the global model
4. once a client leave, the server initalise closing

## Usage demo
example shown in 
	Server side
		python3 server.py --clients 2 # 2 clients participating

	clients side
		from client import client
		obj=client()
		..... After each iteration ....
			  ON=obj.merge(model)
			  #if ON is False is server side is closed so stop training.
		...............................	  
		
		del obj # onces training is finished in any client ,
		#this will initiate server closing and stops training in clients

