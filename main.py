from utils import data_file


def main():
    DATA_JSON_URL = 'https://file.notion.so/f/s/d22c7143-d55e-4f1d-aa98-e9b15e5e5efc/operations.json?spaceId=0771f0bb-b4cb-4a14-bc05-94cbd33fc70d&table=block&id=f11058ed-10ad-42ea-a13d-aad1945e5421&expirationTimestamp=1678784967569&signature=wGexu_JMp-XTm19JXtaK4593ERu3RDSk5-zvzzYDhwg&downloadName=operations.json'
    operation = data_file(DATA_JSON_URL)
    print(operation)



if __name__ == '__main__':
    main()