import requests
import json
import re
from datetime import datetime , timedelta
from dateutil import parser
import time

def main():

	url = 'http://challenge.code2040.org/api/dating'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89'}
	headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)
	array = r.content
	data = json.loads(array)
	date_string = data["datestamp"]
	seconds_str= data["interval"]
	seconds_int = int(seconds_str)
	original_datetime = parser.parse(date_string)
	print original_datetime
	print seconds_int
	new_time = original_datetime + timedelta(seconds = seconds_int)
	new_time1 = new_time.replace(tzinfo=None)
	print new_time1
	finaltime = new_time1.strftime('%Y-%m-%dT%H:%M:%SZ')
	url = 'http://challenge.code2040.org/api/dating/validate'
	m_data = { 'token':'4db4fe513b59797d9ed7b6841cfbbf89', 'datestamp':finaltime}
	r = requests.post(url, data=json.dumps(m_data), headers=headers)



	
if __name__ == "__main__":
	main()
