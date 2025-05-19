from google.oauth2 import service_account
import google.auth.transport.requests
import os
import requests
import json
from Specto.settings import app_settings


def get_fcm_access_token():
    firebase_service_account = os.path.join(os.path.dirname(__file__), app_settings.GOOGLE_APPLICATION_CREDENTIALS)
    print("firebase_service_account", firebase_service_account)
    scopes = ["https://www.googleapis.com/auth/firebase.messaging"]
    credentials = service_account.Credentials.from_service_account_file(
        firebase_service_account, scopes=scopes
    )

    request = google.auth.transport.requests.Request()
    credentials.refresh(request)
    return credentials.token


def send_fcm_notifications(device_token, payload):
    fcm_url = 'https://fcm.googleapis.com/v1/projects/specto-13dfd/messages:send'
    print("payload", payload)
    message = {
                "message":{
                    "token" : device_token,
                    "notification": {
                        "title": payload.get("title"),
                        "body": payload.get("body", "This is a test notification"),
                    },
                    "data": {
                        "due_time": payload.get("due_time")
                    }
                }
            }
    
    headers = {
        'Authorization': 'Bearer ' + get_fcm_access_token(),
        'Content-Type': 'application/json'
    }

    response = requests.post(fcm_url, headers=headers, data=json.dumps(message))
    if response.status_code == 200:
        print("Notification sent successfully")
    else:
        print("Failed to send notification:", response.status_code, response.text)
