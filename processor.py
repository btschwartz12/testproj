
"""curl -v "https://developer.api.autodesk.com/authentication/v1/gettoken" 
-X "POST" -H "Content-Type: application/x-www-form-urlencoded" 
-d "client_id=Ap9x3NhxgxSYAPcSwb8xfwdyAQ5mn2uu" 
-d "client_secret=ZCAW2dDJHHeB3cOJ" 
-d "grant_type=authorization_code" 
-d "code=RwU9vBLtGVnEgTQ4ycaFAYQqHLizPIQ6LlkeXMYq" 
-d "redirect_uri=http://localhost:8000/callback/"
"""
import json
from pprint import pprint
import requests

'''HERE run webserver, then click the button from test.py. WE have the access tokwn, but cannot get the right url for data

https://help.autodesk.com/view/PLM/ENU/?guid=FLC_RestAPI_v3_API_3_legged_Tutorial_html

'''

URL = "https://developer.api.autodesk.com/authentication/v1/gettoken"
CLIENT_ID = "Ap9x3NhxgxSYAPcSwb8xfwdyAQ5mn2uu"
CLIENT_SECRET = "ZCAW2dDJHHeB3cOJ"
REDIRECT_URI = "http://localhost:8000/callback/"

class Processor:
    def __init__(self, code):

        print("code: " + code)

        # self.process(code)


    def process(self, code):
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET,
            "grant_type": "authorization_code",
            "code": code,
            "redirect_uri": REDIRECT_URI
        }

        response = requests.post(URL, headers=headers, data=data).json()

        with open("my.txt", "a+") as f:
            f.write(json.dumps(response, indent=2))

        self.callAPI(response)


    def callAPI(self, response):
        access_token = response["access_token"]
        headers = {
            "Authorization": "Bearer " + access_token,
            "Content-Type": "application/json",
            "Accept": "application/json",
            "X-Tenant": "aclara"
        }      
        # TODO figure out how to get the right endpoint
        url = "https://aclara.autodeskplm360.net/workspace#workspaceid=57&dmsid=5158502"
        response = requests.get(url, headers=headers, verify=True)
        response = response.json()
        return response


