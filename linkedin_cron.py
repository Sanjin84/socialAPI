# Imports
import os
from requests_oauthlib import OAuth2Session
import requests
from dotenv import load_dotenv
load_dotenv()

# Set environment variables
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

# Credentials you get from registering a new application
client_id = os.getenv("client_id")
client_secret = os.getenv("client_secret")
person_id = os.getenv("person_id")
print(client_id)
# LinkedIn OAuth2 requests require scope and redirect_url parameters.
# Ensure these values match the auth values in your LinkedIn App
# (see auth tab on LinkedIn Developer page)
scope = ["r_basicprofile,w_member_social"]
redirect_url = 'http://localhost:8000'

# OAuth endpoints given in the LinkedIn API documentation
authorization_base_url = 'https://www.linkedin.com/oauth/v2/authorization'
token_url = 'https://www.linkedin.com/oauth/v2/accessToken'

linkedin = OAuth2Session(client_id, redirect_uri='http://localhost:8000', scope=scope)

# Redirect user to LinkedIn for authorization
authorization_url, state = linkedin.authorization_url(authorization_base_url)
print(f"Please go here and authorize: {authorization_url}")

# Get the authorization verifier code from the callback url
redirect_response = input('Paste the full redirect URL here:')

# Fetch the access token
linkedin.fetch_token(token_url, client_secret=client_secret,include_client_id=True,authorization_response=redirect_response)

# Fetch a protected resource, i.e. user profile
#r = linkedin.get('https://api.linkedin.com/v2/me')
#id = r.json()['id']
#print(id)

post_data = {
    "author": person_id,
    "lifecycleState": "PUBLISHED",
    "specificContent": {
        "com.linkedin.ugc.ShareContent": {
            "shareCommentary": {
                "text": "This is a test post from the API"
            },
            "shareMediaCategory": "NONE"
        }
    },
    "visibility": {
        "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
    }
}

r = linkedin.post('https://api.linkedin.com/v2/ugcPosts', headers={'X-Restli-Protocol-Version': '2.0.0'}, json=post_data)

print(r.status_code)