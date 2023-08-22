import requests
from datetime import datetime
pixela_endp="https://pixe.la/v1/users"
USERNAME="YOUR USERNAME"
PASSWORD="YOUR PASSWORD"
user_params={
    "token":"PASSWORD",
    "username":"USERNAME",
    "agreeTermsOfService":"yes",
    "notMinor":"yes",
}
# response=requests.post(url=pixela_endp, json=user_params)
# print(response.text)

graph_endp=f"https://pixe.la/v1/users/{USERNAME}/graphs"
graph_params={
    "id":"work",
    "unit":"minutes",
    "name":"Work Tracker",
    "type":"float",
    "color":"ajisai"
}
HEADERS={
    "X-USER-TOKEN":PASSWORD
}
# response=requests.post(url=graph_endp, json=graph_params, headers=HEADERS)
# print(response.text)
today=datetime.now()
pixel_endp=f"https://pixe.la/v1/users/{USERNAME}/graphs/work"
pixel_params={
    "date":today.strftime("%Y%m%d"),
    "quantity":input("How many minutes did you work today?"),
}
response=requests.post(url=pixel_endp, json=pixel_params, headers=HEADERS)
print(response.text)
put_endp=f"{pixel_endp}/20230630"
put_params={
    "quantity":"250.9"
}
# response=requests.put(url=put_endp, json=put_params, headers=HEADERS)
# # print(response.text)
# requests.delete(url=put_endp, headers=HEADERS)

