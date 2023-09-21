import json
import os

def main():
    if not os.path.exists("data.json"):
        print("No data.json file existing!")
        return
    searchQuery = input("Search field:")
    newData = []
    with open("data.json", mode="r") as data: newData = json.loads(data)
    

main()