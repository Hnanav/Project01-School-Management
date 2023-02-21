"""from dbprovider import writeStudents

sts =[ {
    'Code': 'PY03031',
    'FullName':'Vũ Thanh Vân',
    'Birthday' :'01/02/2000',
    'Sex':0,
    'Address':'Hà Nội',
    'Phone':'0977999777',
    'Email':'vvuthanhvan@gmail.com'
},
{'Code': 'PY0302',
    'FullName':'Vũ Thanh Vân',
    'Birthday' :'01/02/2000',
    'Sex':0,
    'Address':'Hà Nội',
    'Phone':'0977999777',
    'Email':'vvuthanhvan@gmail.com'}
]
writeStudents(sts) 

from dbprovider import readStudents
sts = readStudents()
print(sts)  

import dbprovider
st = dbprovider.checkExistsStudent('PY03031')
#print(st)
st1 = dbprovider.getStudentByCode('PY0304')
#print(st1)

newSub = {
    'Code':'INT 4001',
    'Subject': 'Interns'
}
dbprovider.writeSubject(newSub)

resList = dbprovider.readSubject()
#print(resList)

print(dbprovider.getSubjectByCode('INT3003'))
"""

#Main module của ứng dụng
from utils import printHeader, printMenu, clearScreen
from studentscreen import studentMenuScreen
#Màn hình menu chính của ứng dụng

def mainMenuScreen():
    clearScreen()
    printHeader('CHƯƠNG TRÌNH QUẢN LÝ ĐIỂM THI')

    funcs = [
        '1. Student Management',
        '2. Subject Management',
        '3. Score Management',
        '0. Exit',
    ]
    printMenu(funcs)

    cmd = None
    while cmd not in ['1','2','3','0']:
        cmd = input('Choose function: ')
    if cmd == '1':
        #Chuyển sang màn hình Student management
        studentMenuScreen()
        #Mở lại màn hình cũ
    elif cmd =='2':
        #Chuyển sang màn hình Subject management
        pass
        #TODO
    elif cmd == '3':
        #Chuyển sang màn hình Score management
        #TODO
        pass
    elif cmd == '0':
        print("Goodbye. See you soon!")
        exit()

if __name__ == '__main__':
    mainMenuScreen()