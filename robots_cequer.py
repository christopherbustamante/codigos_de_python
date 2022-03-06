import requests

default_files = ["robots.txt", "sitemap.xml"]

target = "https://transparencia.vitacura.cl/"

def check_robots():
  results = []
  for default_file in default_files:
    response = requests.get(target + default_file)
    if response.status_code == 200:
      results.append(response.text)
  return results
    
data = check_robots()

for elemento in data:
  elemento_separado_por_lineas = elemento.split()
  for linea in elemento_separado_por_lineas:
    if "Allow" in linea or "Disallow" in linea:
      print(linea)