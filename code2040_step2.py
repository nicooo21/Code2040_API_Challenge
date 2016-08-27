import requests
import json

def main():

	url = 'http://challenge.code2040.org/api/reverse'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89' }
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	reg_string = r.content
	string_reversed = ""
	string_len = len(reg_string)
	for x in range(string_len - 1 , -1, -1):
		string_reversed += reg_string[x]
	url = 'http://challenge.code2040.org/api/reverse/validate'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89' , 'string':string_reversed}
	r = requests.post(url, data = json.dumps(m_data), headers = headers)



if __name__ == "__main__":
	main()
