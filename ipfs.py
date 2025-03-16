import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data, dict), f"Error pin_to_ipfs expects a dictionary"
    
    # Convert dictionary to JSON string
    json_data = json.dumps(data)
    
    # Define the IPFS API endpoint for adding data
    ipfs_add_url = "https://ipfs.io/ipfs/{cid}"
    
    # Send the data to IPFS
    response = requests.post(ipfs_add_url, files={"file": json_data})
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract the CID from the response
        cid = response.json()["Hash"]
    else:
        raise Exception(f"Failed to pin data to IPFS: {response.text}")
    
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