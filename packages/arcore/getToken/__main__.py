from google.oauth2 import service_account
from google.auth.transport.requests import Request

def main(args):
    SCOPES = ['https://www.googleapis.com/auth/arcore.management']
    SERVICE_ACCOUNT_FILE = './causal-bison-440316-s9-11a019a91062.json' # creds.json

    credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    request = Request()
    credentials.refresh(request)
    return {"body": credentials.token}
