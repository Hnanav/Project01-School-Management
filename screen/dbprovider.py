#Interact data with txt file

studentPath = 'data/student.txt'
subjectPath = 'data/subject.txt'
scorePAth = 'data/score.txt'

def writeStudent(st: dict):
    """Write student to txt file
    {
    'Code': 'PY0301',
    'FullName':'Vu Thanh Van',
    ...
    }
    """
    with open (studentPath,'a', encoding="utf-8") as f:
        line: str = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"  #format string
        f.write(line)


def writeStudents(sts: list):
    with open (studentPath,'w',encoding='utf-8') as f:
        for st in sts:
            line: str = f"{st['Code']}|{st['FullName']}|{st['Birthday']}|{st['Sex']}|{st['Address']}|{st['Phone']}|{st['Email']}\n"  #format string
            f.write(line)
    
def readStudents():
    sts1 = []
    with open(studentPath,'r', encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            st = {
            'Code': value[0],
            'FullName': value[1],
            'Birthday': value[2],
            'Sex': value[3],
            'Address': value[4],
            'Phone': value[5],
            'Email': value[6]
            }
            sts1.append(st)
    return sts1

def getStudentByCode(code:str) :
    result = None
    with open(studentPath,'r', encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            if value[0] == code:
                result = {
                    'Code': value[0],
                    'FullName': value[1],
                    'Birthday': value[2],
                    'Sex': value[3],
                    'Address': value[4],
                    'Phone': value[5],
                    'Email': value[6]
                }
                break
    return result


def checkExistsStudent(code: str):
    result = False
    with open(studentPath,'r', encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            if value[0] == code:
                result = True
                break
    return result

def writeSubject(sub: dict):
    with open (subjectPath,'a', encoding="utf-8") as f:
        line: str = f"{sub['Code']}|{sub['Subject']}\n"  #format string
        f.write(line)

def readSubject():
    sublist = []
    with open (subjectPath,'r', encoding='utf-8') as f:
        for line in f:
            if line is None:
                break
            value = line.strip().split('|')
            sub = {
                'Code': value[0],
                'Subject': value[1]
            }
            sublist.append(sub)
    return sublist

def getSubjectByCode(code:str):
    target = None
    with open (subjectPath,'r',encoding='utf-8') as file:
        for line in file:
            if line is None:
                break
            value = line.strip().split('|')
            if(value[0] == code):
                target=(value[1])
                break
    return target


    