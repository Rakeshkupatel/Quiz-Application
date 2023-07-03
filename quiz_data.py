import requests
parameters={
    "amount":50,
    "type":"multiple"
}
response=requests.get(url="https://opentdb.com/api.php?amount=40&difficulty=medium&type=multiple",params=parameters)
question_data=response.json()["results"]
