import requests                 # To deal with REST APIs
import json
import os
from dotenv import load_dotenv
load_dotenv()


# Get the ClientID and ClientSecret to get the access token
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
person_id = os.getenv("person_id")

person_id = "477007202"
access_token = 'AQUlpzxhEMivyNDCEnuRU2V6T7uBYBItvON0hVdL3CzlJnccYg1AnWY4OgZ06uO4d4Fe5SJ41BiAbsQcE2swSDsTfweRvz-KrIjNl9JKbwbaUD-fysdnTEGBrWNyU-1fAeDPzSoBUFSeHGK8n6oDH51EfTx4W9IHiuUQBNMInsJbPCNa1E2oiiGmBkcPA1IpOJQPk9m5e64bdi-KRxcMAHs8m4q58ZaHOGcdQMN1f7keRxcTBMuuodGveaj-V5bXZ5WFkiGysAS23ZPdw1SGhmlkDDh0cMTaWpE3ErkzZ2WAjv5S5E-FH9fRdUBwbwuwcAFs0AF2FFVsCXghfz7fMWlWdch-2A'

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
'''
curl --request POST \
--url ' https://api.linkedin.com/v2/me' \
--header 'content-type: application/x-www-form-urlencoded' \    
--data access_token='AQUlpzxhEMivyNDCEnuRU2V6T7uBYBItvON0hVdL3CzlJnccYg1AnWY4OgZ06uO4d4Fe5SJ41BiAbsQcE2swSDsTfweRvz-KrIjNl9JKbwbaUD-fysdnTEGBrWNyU-1fAeDPzSoBUFSeHGK8n6oDH51EfTx4W9IHiuUQBNMInsJbPCNa1E2oiiGmBkcPA1IpOJQPk9m5e64bdi-KRxcMAHs8m4q58ZaHOGcdQMN1f7keRxcTBMuuodGveaj-V5bXZ5WFkiGysAS23ZPdw1SGhmlkDDh0cMTaWpE3ErkzZ2WAjv5S5E-FH9fRdUBwbwuwcAFs0AF2FFVsCXghfz7fMWlWdch-2A' \
'''