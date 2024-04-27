import requests
import json

class NetworkController:
    def __init__(self) -> None:
        self.BASE_URL = "https://spinbin-trash-classifier-api-production.up.railway.app"
        self.HEADERS = {
            "Content-Type": "application/json"
        }

    def getRoute(self, route = "/"):
        response  = requests.get(f"{self.BASE_URL}{route}")
        return response.json()
    
    
    def classifyWaste(self, image):
        payload = {
            "img": image
        }

        payload = json.dumps(payload)
        # print(payload)
        try:
            response = requests.post(f"{self.BASE_URL}/classifybase64", payload, self.HEADERS)
            print(response.json()['classification'])
            return response.json()['classification']
        except Exception as e:
            print(f"Error: {e}")




if __name__ == "__main__":
    requestClass = NetworkController()
    print(requestClass.getRoute())
