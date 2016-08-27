import requests
import json
import re

def main():

	url = 'http://challenge.code2040.org/api/prefix'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89'}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	array = r.content
	data = json.loads(array)
	prefix = data["prefix"]
	strings = data["array"]
	arr_len = len(strings)
	myList = []
	for x in range(0, arr_len):
		match = re.search(r"^%s" % prefix, strings[x])
		if not match:
			myList.append(strings[x])
	url = 'http://challenge.code2040.org/api/prefix/validate'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89', 'array':myList }
	r = requests.post(url, data = json.dumps(m_data), headers=headers)
if __name__ == "__main__":
	main()
