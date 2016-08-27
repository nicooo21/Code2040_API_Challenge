import requests
import json
import re

def main():

	url = 'http://challenge.code2040.org/api/haystack'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89' }
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	array = r.content
	data = json.loads(array)
	needle = data["needle"]
	index = 0
	haystack = data["haystack"]
	for x in range(0, len(haystack)): #iterate through 'haystack' array
		if haystack[x] == needle: #check if element in haystack has needle
			index = x 	  #assigns that index
	url = 'http://challenge.code2040.org/api/haystack/validate'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89' , 'needle':index}		
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	

if __name__ == "__main__":
	main()
