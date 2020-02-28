# Tic-Tac-Toe API using Flask and Ngrok 

Start server locally: 
```
python -m flask run 
```
To run on ngrok server:
```
./ngrok http 5000
```
The new address will look something like this: 
```
Forwarding                    https://938e2094.ngrok.io -> http://localhost:5000
```

Ngrok reference: <https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment>

Browser access: 
```
"localhost:.../tic_tac_toe/{user_moves}/{comp_moves}" 
```

Example board: 
```
     |     |     
  X  |  -  |  -  
_____|_____|_____
     |     |     
  -  |  O  |  X  
_____|_____|_____
     |     |     
  -  |  O  |  X  
     |     |     
```
Example input (boards are 1-indexed): 
```
"localhost:.../tic_tac_toe/{1_6_9}/{5_8}" 
```

## Resources: 

See the API in action here: <https://bubble.io/site/swetafirstapp/>
