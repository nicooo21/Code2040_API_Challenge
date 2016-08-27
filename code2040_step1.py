import requests
import json

def main():

	url = 'http://challenge.code2040.org/api/register'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89', 'github':'https://github.com/nicooo21/Code2040_API_Challenge' }
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	

if __name__ == "__main__":
	main()
