from flask import Flask, request, Response
import os
import requests, json, random, os
import traceback 

app = Flask(__name__)
token = "EAAMPe2L0HigBOwDbZAUu0LCfMZALQibkiBkDvYlsuzvZCAbZCeajSRwaKkLVltLtUNQZBz1QZBANtsSL5QeCFvN2fZASV18dxGgXZBTFWMjXXGXbelbLJt4I5c5GZCAqa8dwhVkZCs9oBulGkQcUxmBowBlMb3VplHrJtKJcm5VuXfdY8p3zJ9trir4CGY2GtPSCZBjeJM9pDzcvT4hN3nR"
pageId = "108792698995147"
apiVersion = "v18.0"
verify_token = "OK"
HEARDER = {
    "Content-Type": "application/json"
}

#verify webhook url
@app.route('/demo', methods=['GET'])
def validate():
    if request.args.get('hub.mode', '') == 'subscribe' and request.args.get('hub.verify_token', '') ==   verify_token:
        print("Validating webhook")
        return request.args.get('hub.challenge', '')
    else:
        return 'Failed validation. Make sure the validation tokens match.'
    

@app.route('/demo', methods=['POST'])#สำหรับรับ event
def webhook():
    print(request.json)

if __name__ == '__main__':
    app.run(host='127.0.0.1', debug=True, port=int(os.environ.get('PORT','5000')))
