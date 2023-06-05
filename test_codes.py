import requests

pega_api_url = 'https://<YOUR_PEGA_INSTANCE>/prweb/api/v1'
username = '<YOUR_USERNAME>'
password = '<YOUR_PASSWORD>'

def get_access_token():
    auth_url = pega_api_url + '/auth/authentication'
    auth_data = {'userid': username, 'password': password}
    response = requests.post(auth_url, data=auth_data)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception('Failed to authenticate')

def make_api_request(endpoint, access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    response = requests.get(pega_api_url + endpoint, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception('API request failed')

def get_node_status_details():
    access_token = get_access_token()
    nodes_endpoint = '/system/nodes'
    nodes_data = make_api_request(nodes_endpoint, access_token)
    return nodes_data

if __name__ == '__main__':
    node_details = get_node_status_details()
    print(node_details)
