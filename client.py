import pickle
import requests
import json
import time

class client:
    def __init__(self,url='127.0.0.1:5000'):
        self.url=url

        response = requests.post(f'http://{self.url}/getid')
        if response.status_code == 200:
            self.ids = int(response.content)
            print("connection id ",self.ids)
        else:
            raise Exception("invalid connection to server !!!!")


    def merge(self,model):
        model_state_dict = model.state_dict()

        # Print the state dictionary
        # print(model_state_dict)
        a=pickle.dumps((self.ids,model_state_dict))
        response = requests.post(url = f'http://{self.url}/upload', data=a,headers = {'Content-Type': 'application/octet-stream'})
        # print(response.content)
        if response.status_code!=200:
            return False
        model.load_state_dict(pickle.loads(response.content))
        return True
        # return pickle.loads(response.content)
    def __del__(self,):
        response = requests.post(f'http://{self.url}/close')
        if response.status_code ==200:
            print("closing initiated")



        
        
# obj1=client()
# time.sleep(6)
# obj1.merge(model)
