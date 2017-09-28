import requests
import json

def access_condtions():

    API_KEY="f9caff179aa553f4"
    BASE_URL="http://api.wunderground.com/api/"
    STATE="PA"
    CITY="Philadelphia.json"
    FEATURE="conditions"
    REQ_URL= BASE_URL+API_KEY+"//"+FEATURE+"/q/"+STATE+"/"+CITY
    response = requests.get(REQ_URL)
    print(REQ_URL)
    parsed_json = json.loads(response.content.decode('utf-8'))
    temp_in_f=parsed_json['current_observation']['temp_f']
    temp_in_c=parsed_json['current_observation']['temp_c']
    print("Current temperature in fahrenheit:",temp_in_f)
    print("Current temperature in Celsius: ",temp_in_c)
    print("Conditions:",parsed_json)

if __name__ == '__main__':
    access_condtions()
