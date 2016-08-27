import requests


def main():
	request = requests.post("http://challenge.code2040.org/api/register", json = {"key":"value"})
	print request.status_code

if __name__ == "__main__":
	main()
