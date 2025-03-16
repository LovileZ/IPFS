import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    
    # Convert dictionary to JSON string
    json_data = json.dumps(data)
    
    # Define the Pinata API endpoint for adding data
    pinata_add_url = "https://api.pinata.cloud/pinning/pinJSONToIPFS"
    
    # Define the headers with your Pinata API key and secret
    headers = {
        "Content-Type": "application/json",
        "pinata_api_key": "14d1fb98dc31bbddfc7f",
        "pinata_secret_api_key": "5c6e2d40ff55115e2a16b8823b953c62404867383be34454a1921911f7584b3c"
    }
    
    # Send the data to Pinata
    response = requests.post(pinata_add_url, headers=headers, data=json_data)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the CID from the response
        cid = response.json()["IpfsHash"]
    else:
        raise Exception(f"Failed to pin data to Pinata: {response.text}")
    
    return cid

def get_from_ipfs(cid, content_type="json"):
    assert isinstance(cid, str), f"get_from_ipfs accepts a cid in the form of a string"
    
    # Define the IPFS API endpoint for getting data
    ipfs_cat_url = f"https://ipfs.io/ipfs/{cid}"
    
    # Get the data from IPFS
    response = requests.get(ipfs_cat_url)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the JSON content
        data = response.json()
    else:
        raise Exception(f"Failed to get data from IPFS: {response.text}")
    
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data