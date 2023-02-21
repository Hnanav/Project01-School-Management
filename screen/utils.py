# tool box for general use
import os
#Print screen's title
def printHeader(title: str):
    header = f'*****{title}*****'
    print(header)
    print('-'*len(header))

def printMenu(funcs: list):
    print('\n'.join(funcs))  #Hàm join nối các phần tử trong list bằng kí tự
    
#Clear content in terminal/cmd
def clearScreen():
    os.system('cls||clear')

def printAllofList(lst: list):
    for item in lst:
        print(f"{item['Code']}\t{item['FullName']}\t{item['Birthday']}\t{item['Address']}\t{item['Phone']}\t{item['Email']}")