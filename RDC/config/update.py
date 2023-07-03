import json
import requests

def getData() -> dict:
	with open("info.json", "r") as file:
		return json.loads(file.read())

def compare_versions(version1, version2):
	# Split the versions into their components
	v1 = list(map(int, version1.split(".")))
	v2 = list(map(int, version2.split(".")))

	# Compare each component of the versions
	for i in range(len(v1)):
		if v1[i] > v2[i]:
			return version1
		elif v1[i] < v2[i]:
			return version2

	# If all components are equal, the versions are the same
	return version1

recent = requests.get("https://raw.githubusercontent.com/Tom-Sumner/Python-Monitor/main/RDC/config/info.json").json()
print(recent["version"])