import os
def filesize(folder_dir="./"):
     for ficheiro in os.listdir(folder_dir):
        a = os.stat(ficheiro).st_size
        print(f"Tamanho do ficheiro {ficheiro} é igual a {a}")

   

    


def main():
    
    filesize()
main()
