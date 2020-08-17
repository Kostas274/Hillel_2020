import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
my_list = response.json()
with open("1.txt", "w") as file:
    for dict in my_list:
        title = dict["title"].capitalize()
        file.write("\n" + title)
        file.write("\n" + "=" * len(title))
        body = dict["body"].capitalize()
        file.write("\n" + body + ".")
        file.write("\n")