#Package
import requests
import json
#define Header
HEADER = {
    "Content-Type": "application/json"
}
token = "EAAMPe2L0HigBO6sWr8x0QZBZC2JZBnxpSCwjDNO3FJ5weRumK8Bs5j2pVmhzj8JKL2kDiUZBP5vYuqUAbAn5q7jMdlI3ODGqNCfMwEohFmFdFHyFOqur4k0m4AVbeN36qyZAbjZAdrM6Y2YuiIHp9Wiec91qioKM2RvAJsZAV4hmjrTWsGnJYm7IM0LfuSfY0rKAcUejRH7oFefN6L2"

pageId = "108792698995147"
apiVersion = "v18.0"

def sent_message(msg,psid) :
    url = "https://graph.facebook.com/<API-VERSION>/<PAGE-ID>/messages?access_token=<ACCESS-TOKEN>"
    req = url.replace("<API-VERSION>",apiVersion).replace("<PAGE-ID>",pageId).replace("<ACCESS-TOKEN>",token)
    body = {
        "recipient":{
            "id":psid
        },
        "messaging_type": "RESPONSE",
        "message":{
            "text": msg
        }
    }
    r = requests.post(req, json=body,headers=HEADER)
    print(r.text)
    r.close()

def sent_picture(picUrl,psid) :
    url = "https://graph.facebook.com/<API-VERSION>/<PAGE-ID>/messages?access_token=<ACCESS-TOKEN>"
    req = url.replace("<API-VERSION>",apiVersion).replace("<PAGE-ID>",pageId).replace("<ACCESS-TOKEN>",token)
    body = {
        "recipient":{
            "id":psid
        },
        "messaging_type": "RESPONSE",
        "message":{
            "attachment":{
                "type":"image", 
                "payload":{
                   "url":picUrl , 
                   "is_reusable":True
                }
            }
        }
    }
    r = requests.post(req, json=body,headers=HEADER) #POST METHOD
    print(r.text)
    r.close() 

def sent_template(pictureUrl,url,psid) :

    pictureUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png"
    url = "https://graph.facebook.com/<API-VERSION>/<PAGE-ID>/messages?access_token=<ACCESS-TOKEN>"
    req = url.replace("<API-VERSION>",apiVersion).replace("<PAGE-ID>",pageId).replace("<ACCESS-TOKEN>",token)
    body = {
        "recipient": {
            "id": psid
        },
        "message":{
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"generic",
                        "elements":[{
                            "title":"",
                            "image_url":pictureUrl ,
                            "buttons":[{
                                "type":"web_url",
                                "url":url,
                                "title":"WEB SITE"
                                }             
                            ]
                        }]
                    }
                }
            }
        }
    
    r = requests.post(req, json=body,headers=HEADER)
    print(r.text)
    r.close()
############################# เพิ่มเติม(more) #############################
def addLabel(labelName) :
    createLabel ="https://graph.facebook.com/<API-VERSION>/me/custom_labels?access_token=<ACCESS-TOKEN>"
    req = createLabel.replace("<API-VERSION>",apiVersion).replace("<ACCESS-TOKEN>",token)

    body = {
        "page_label_name": labelName,
    }
    r = requests.post(req, json=body,headers=HEADER)
    r.close()

def getLabelById(label_id) :
    getLabelById = "https://graph.facebook.com/<API-VERSION>/<LABEL_ID>?fields=page_label_name&access_token=<ACCESS_TOKEN>"

    req = getLabelById.replace("<API-VERSION>",apiVersion).replace("<LABEL_ID>",label_id).replace("<ACCESS-TOKEN>",token)

    r = requests.get(req,headers=HEADER)
    jsonData = json.loads(r.text) #แปลงเป็น json Object

    label = {data["page_label_name"]:data["id"] for data in jsonData["data"]} #แปลงเป็น Dictionary -> labelName : labelId

    return label

def getAllLabel() :
    getAllLabel = "https://graph.facebook.com/<API-VERSION>/me/custom_labels?fields=page_label_name&access_token=<ACCESS-TOKEN>"
    req = url.replace("<API-VERSION>",apiVersion).replace("<ACCESS-TOKEN>",token)
    r = requests.get(req)
    jsonData = json.loads(r.text)#แปลงเป็น json Object
    listAllLabel = {data["page_label_name"]:data["id"] for data in jsonData["data"]}# labelName : labelId

    return listAllLabel

def deleteLabelFromUser(labelId,psid):
    deleteLabel = "https://graph.facebook.com/<API-VERSION>/<LABEL_ID>/label?user=<PSID>&access_token=<ACCESS-TOKEN>"
    req = url.replace("<API-VERSION>",apiVersion).replace("<LABEL_ID>",labelId).replace("<PSID>",psid).replace("<ACCESS-TOKEN>",token)
    
    r = requests.delete(req,headers=HEADER)
    print(r.status_code)
    print(r.text)


if __name__== "__main__":
    psid = "6583685558406580"
    #sent message
    sent_message("Hello mini world",psid)
    #sent picture  
    sent_picture("https://inwfile.com/s-di/0mrq2i.jpg",psid)
    #sent template
    pictureUrl = "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_2015_logo.svg/1200px-Google_2015_logo.svg.png"
    url ="https://www.google.com"
    sent_template(pictureUrl,url,psid)
