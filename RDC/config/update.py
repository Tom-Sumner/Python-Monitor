import json
import requests

def getData() -> dict:
	with open("info.json", "r") as file:
		return json.loads(file.read())

version = getData["version"]
