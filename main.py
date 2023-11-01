import json
import os
from flask import Flask, request
app = Flask(__name__)

def search(searchQuery):
    if not os.path.exists("data.json"):
        print("No data.json file existing!")
        return
    
    result = []
    newData = []
    with open("data.json", mode="r", encoding="utf8") as data: newData = json.load(data)

    for i in newData:
        if searchQuery.lower() in i["name"].lower():
            result.append(i)
            continue
        if searchQuery.lower() in i["artist"].lower():
            result.append(i)
            continue
        if searchQuery.lower() in i["album"].lower():
            result.append(i)
            continue

    return result


@app.route("/search", methods=["GET"])
def getSearchRequest():
    if not request.headers["host"] == "mywebsite.com":
        return "Invalid host header!"
    if not "query" in request.args:
        return "Link missing 'query' parameter!"

    searchQuery = request.args.get("query")
    return search(searchQuery)


@app.errorhandler(404)
def returnError():
    return "There was an unknown error. Please try again later!"


app.run(debug=True)