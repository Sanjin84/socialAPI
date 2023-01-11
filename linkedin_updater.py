import requests                 # To deal with REST APIs
import json
import os
from dotenv import load_dotenv
load_dotenv()


# Get the ClientID and ClientSecret to get the access token
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
person_id = os.getenv("person_id")
access_token = os.getenv("li_access_token")

# Get LinkedIn user ID
url = "https://api.linkedin.com/v2/me"

header = {
    'Authorization' : f'Bearer {access_token}'
}

response = requests.get(url=url, headers=header)
response_json_li_person = response.json()
print(response_json_li_person)
#person_id = response_json_li_person['id']

'''
url = "https://api.linkedin.com/v2/shares"

headers = {
    'Authorization' : f'Bearer {access_token}',
    'Content-Type' : 'application/json'
}

payload = {
    "content": {
        "contentEntities": [
            {
                "entityLocation": "https://www.redhat.com/en/topics/api/what-is-a-rest-api",
                "thumbnails": [
                    {
                        "resolvedUrl": "https://images.pexels.com/photos/2115217/pexels-photo-2115217.jpeg"
                    }
                ]
            }
        ],
        "title": "What is a REST API?"
    },
    'distribution': {
        'linkedInDistributionTarget': {}
    },
    'owner': f'urn:li:person:{person_id}',
    'text': {
        'text': f'Learn more about REST APIs in details.  \n#restapi #api'
    }
}

response = requests.post(url=url, headers=headers, json = payload)

print(response.json())
'''