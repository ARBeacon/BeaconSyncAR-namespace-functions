# BeaconSyncAR Namespace Functions
Serverless functions for generating OAuth2 tokens to authenticate with Google ARCore API.

## 🔑 Function Overview

Location:  
`/packages/arcore/getToken` - Generates short-lived OAuth2 tokens for ARCore API access

## ⚙️ Configuration

1. Place your Google Cloud service account credentials file in: 
`BeaconSyncAR-namespace-functions/packages/arcore/getToken/creds.json`
2. Set the path in `getToken/__main__.py`:
```python
SERVICE_ACCOUNT_FILE = "creds.json"  # Path relative to function directory
```

## 🚀 Deployment (DigitalOcean)
1. Install prerequisites:
```bash
pip install google-auth
```

2. Setup DigitalOcean CLI
```bash
doctl serverless install
doctl auth init
```

3. Deploy functions:
```bash
doctl serverless deploy BeaconSyncAR-namespace-functions
```
## 🔒 Security Note
- The creds.json file contains sensitive credentials
- DigitalOcean Serverless automatically secures environment files
- Never commit credentials to version control

## 📄 Usage
The deployed function will be available at:
`https://faas-<region>.digitaloceanspaces.com/<namespace>/arcore/getToken`
