from pyngrok import conf,ngrok
from threading import Thread
from configparser import ConfigParser
import requests
import base64
import time
import json
import sys
import re
import os


#Suppress error messages
sys.stderr = open(os.devnull, "w")

#Create log file
log_file = open("/tmp/webexOOO.log", "w")
log_file.close()

#Import Authorization token(s) from config.cfg
config = ConfigParser()
config.read('config.cfg')
webex_personal_token=config.get('webex','webex_personal_token')
webex_bot_token=config.get('webex','webex_bot_token')

#Define email to keep track of repeat senders
customer_email = "abc@x.com"


def log_event_callback(log):
    with open('/tmp/logFile.log', 'a') as f:
        print(log, file=f)
conf.get_default().log_event_callback = log_event_callback

def func0():
    url = "https://webexapis.com/v1/messages/direct?personEmail=" + customer-email
    headers = {
    'Authorization': 'Bearer ' + webex_personal_token,
    'Authorization': 'Bearer ' + webex_bot_token,
    'Content-Type': 'application/json'
    }
    response = requests.request("GET", url, headers=headers)
    r_json = response.json()
    message = r_json["items"][1]["html"]
    TAG_RE = re.compile(r'<[^>]+>')
    message_parsed = TAG_RE.sub('', message)

def func1():
    print("\n| --> Create ngrok tunnel")
    ngrok.connect(5000, bind_tls=True)
    tunnels = ngrok.get_tunnels()
    tunnel_IP = re.findall(r'\"(.+?)\"', str(tunnels))[0]
    # Create webex webhook
    print("| --> Create webex webhook")
    url = "https://webexapis.com/v1/webhooks"
    payload = json.dumps({
    "resource": "messages",
    "event": "created",
    "filter": "roomType=direct",
    "targetUrl": tunnel_IP,
    "name": "Webex OOO"
    })
    headers = {
    'Authorization': 'Bearer ' + webex_personal_token,
    'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    r_json = response.json()
    print("| --> Listening...")

def func2():
    while True:
        time.sleep(5)
        # Check webhook for new messages
        with open("/tmp/logFile.log", "r+") as file:
            result = (list(file)[-1])
            print(result)
            if "127.0.0.1:5000" in result:
                file.truncate(0)
                file.write(str('rolloverLine'))
                print("passed")
                url = "http://localhost:4040/api/requests/http?limit=1"
                response = requests.request("GET", url)
                r_json = response.json()

                for i in range(0, len(r_json['requests'])):
                    encrypted_response = r_json["requests"][i]["request"]["raw"]
                    base64_bytes = encrypted_response.encode("ascii")
                    sample_string_bytes = base64.b64decode(base64_bytes)
                    sample_string = sample_string_bytes.decode("ascii")
                    match = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', sample_string)
                    if str(match).strip("[']") == customer_email:
                        print("again")
                        func0()
                    elif str(match).strip("[']") in open('/tmp/webexOOO.log').read():
                        continue
                    else:
                        log_file = open("/tmp/webexOOO.log", "a")
                        log_file.write(str(match).strip("[']")+ "\n")
                        log_file.close()

                        with open("/tmp/webexOOO.log") as f:
                            personEmail = f.readlines()[-1]
                            print(personEmail)

                        url = "https://webexapis.com/v1/messages"
                        payload = json.dumps({
                        "toPersonEmail": "" + str(personEmail) + "",
                        "markdown": "** Webex OutOfOffice Auto Reply **\n\n Hi, \n I am currently out of office for the weekend and testing an OOO bot. \n Matt"
                        })
                        headers = {
                        'Authorization': 'Bearer ' + webex_personal_token,
                        'Authorization': 'Bearer ' + webex_bot_token,
                        'Content-Type': 'application/json'
                        }
                        response = requests.request("POST", url, headers=headers, data=payload)
                        print(response)
            else:
                pass

if __name__ == '__main__':
    print("start")
    Thread(target = func1).start()
    Thread(target = func2).start()
    print("done")
