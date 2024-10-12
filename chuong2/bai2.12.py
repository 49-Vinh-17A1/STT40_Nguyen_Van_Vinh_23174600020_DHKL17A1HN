import requests
response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    json_data= response.json()
    for post in json_data:
        print("Userid: ",post["userId"])
        print("id: ", post["id"])
        print("title: ",post["title"])
        print("body: ",post["body"])
        print("============================")
else:
    print("yeu cau kh thanh cong, ma trang thai:", response.status_code)