import json
import os

def main():
    if not os.path.exists("data.json"):
        print("No data.json file existing!")
        return
    
    searchQuery = input("Search field:")
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

    with open("results.json", mode="w", encoding="utf8") as newFile:
        newFile.write(json.dumps(result, indent=4))
        newFile.close()

    print("Results printed!")

main()