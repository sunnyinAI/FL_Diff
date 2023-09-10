from flask import Flask, request, make_response
import pickle
import time
import argparse

app = Flask(__name__)

class flask:
    c=0
    state_list = {}
    state = None
    clients=0
    ids = 0
    def __init__(self,args):
        flask.clients = int(args.clients)
        flask.ids=int(args.clients)

def add(flask):
    while flask.c<flask.ids:
        time.sleep(0.05)
        if flask.state is not None:
            break
    if flask.state is  None:
        for key in flask.state_list[0]:
            # flask.state_list[1][key]=sum(flask.state_list[x][key] for x in range(1,flask.ids))/flask.ids
            for x in range(1,flask.ids):
                flask.state_list[0][key]=(flask.state_list[0][key]+flask.state_list[x][key])#/(flask.ids)
            flask.state_list[0][key]/=flask.ids
        flask.state = flask.state_list[0]

        

@app.route('/getid', methods=['POST'])
def getid():
    if flask.clients!=0:
        ids=flask.clients
        flask.clients-=1
        # flask.state_list[flask.ids] = None
        return str(flask.clients),200
    else:
        return "None",400

    


@app.route('/upload', methods=['POST'])
def upload():
    while flask.state is not None:
        time.sleep(0.05)

    
    file = pickle.loads(request.data)
    # print(file[0],"aaaaa")
    if file[0]  in flask.state_list:
        print(f"already exists id {file[0]}")
        return f"already exists id {file[0]}", 400

    flask.state_list[file[0]]=file[1]
    flask.c+=1
    add(flask)
    # print(file)
    response=make_response(pickle.dumps(flask.state))
    response.headers['Content-Type'] = 'application/octet-stream'
    flask.c-=1
    # print(flask.state)
    if flask.c==0:
        flask.state_list = {}
        flask.state = None


    return response, 200 


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("--clients",help="number of clients particiapting")
    args=parser.parse_args()
    # pritn(args)
    obj=flask(args)
    app.debug = True
    app.run(host="0.0.0.0")