import requests

def data_file():
    data = requests.get('https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1677753416732&signature=y_0rdtrNS6DKjc6r6ygR70M1GcqVFb5QYsNe5QnJC-c&downloadName=operations.json')
    data_json = data.json()
    return data_json


