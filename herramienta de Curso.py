import requests

menu = """

.__        ___.                        __               .__          __   .__       .__  __          
|  | _____ \_ |__   ________________ _/  |_  ___________|__| ____   |  | _|__|______|__|/  |_  ____  
|  | \__  \ | __ \ /  _ \_  __ \__  \\   __\/  _ \_  __ \  |/  _ \  |  |/ /  \_  __ \  \   __\/  _ \ 
|  |__/ __ \| \_\ (  <_> )  | \// __ \|  | (  <_> )  | \/  (  <_> ) |    <|  ||  | \/  ||  | (  <_> )
|____(____  /___  /\____/|__|  (____  /__|  \____/|__|  |__|\____/  |__|_ \__||__|  |__||__|  \____/ 
          \/    \/                  \/                                   \/                          


1- Herramienta de Fuzzer
2- Herramienta de Crawler
3- Herramienta Scraper
"""

option =input(menu)

def run():

    if option == '1':

        def lecturadic():

            with open("/home/kali/directory.txt") as dict_file:
            
                return dict_file.readlines()

            diccionario = lecturadic()
            url=input("de una direccion: ")

            for dicc in diccionario:

                respuestas = requests.get(url + dicc.strip())
                print("Testing with: %s --> [%s]" % (dicc.strip (),respuestas.status_code))


    if option == '2':
        pass

if __name__ == '__main__':
    run()


