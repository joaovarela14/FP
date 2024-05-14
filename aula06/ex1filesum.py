from tkinter import filedialog

def main():
    
    name = input("File? ")                                  #A
    #name = filedialog.askopenfilename(title="Choose File") #B
    
    
    total = fileSum(name)
    
    
    print("Sum:", total)


def fileSum(filename):
    soma = 0
    with open (filename,'r') as ficheiro:
        for i in ficheiro:
            soma+=float(i)
    
    return soma

    


if __name__ == "__main__":
    main()

