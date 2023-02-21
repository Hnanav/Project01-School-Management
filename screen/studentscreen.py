# Các màn hình cho module quản lý Học viên

import datetime
from turtle import clearscreen
from dbprovider import *
from utils import *
#from tasks.studenttask import writeStudent
# Màn hình hiển thị menu của module QL Học viện
def studentMenuScreen():
    clearScreen()
    printHeader('QUẢN LÝ HỌC VIÊN')
    funcs = [
        '1. Insert',
        '2. Delete',
        '3. Edit',
        '4. Search ',
        '0. Exit',
    ]
    printMenu(funcs)

    cmd = None
    while cmd not in ['1','2','3','4','0']:
        cmd = input('Choose function: ')
    if cmd == '1':
        #Chuyển sang màn hình add Student management
        addStudentScreen()
        studentMenuScreen()
        
    elif cmd =='2':
        deleteStudentScreen()

    elif cmd == '3':
        editStudentScreen()


    elif cmd == '4':
        searchStudentsScreen()

    elif cmd == '0':
        exit()
        

# Màn hình nhập thông tin học viên
def addStudentScreen():
    clearScreen()
    printHeader('THÊM HỌC VIÊN')

    while True:
        code = input('Mã sinh viên: ')
        if len(code) != 6:
            print('Mã học viên phải có 6 ký tự')
            continue
        else: break
    while True:
        fullname = input('Họ tên đầy đủ: ')
        if fullname[0] != fullname[0].upper():
            print('Họ tên phải viết hoa chữ cái đầu')
            continue
        else: break
    while True:
        birthday = input('Birthday(dd/mm/yyyy): ')
        try:
            t1 = datetime.datetime.strptime(birthday, '%d/%m/%Y')
            t2 = datetime.datetime.now()
            if(t1 >= t2):
                print('Ngày sinh không được lớn hơn ngày hiện tại')
                continue
        except ValueError:
            print('Date invalid')
            continue
        break
        
    while True:
        sex = input('Giới tính (0-Nam, 1-Nữ): ')
        if sex not in ['0','1']:
            print('Giới tính phải là 0 hoặc 1')
            continue
        else: break
    address = input('Địa chỉ: ')
    while True:
        phone = input('Điện thoại: ')
        if phone is None:
            print('Số điện thoại không được để trống')
            continue
        else: break

    email = input('Email: ')

    pupil = {
        'Code': code,
        'FullName': fullname,
        'Birthday': birthday,
        'Sex': sex,
        'Address': address,
        'Phone': phone,
        'Email': email
    }
    if pupil is not None:
        writeStudent(pupil)
        print(f'Thêm học viên {code} vào danh sách thành công' )
    
        ans = input('Bạn có muốn tiếp tục thêm học viên không (Y/N)? ')
        if ans.upper() == 'Y':
            addStudentScreen()

    

# Chỉnh sửa thông tin học viên
def editStudentScreen():
    clearScreen()
    printHeader('CHỈNH SỬA THÔNG TIN HỌC VIÊN')

    while True:
        code = input('Ma HV: ')
        if len(code) != 6:
            print('Mã học viên phải có 6 ký tự')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print('Mã học viên không tồn tại')
            continue
        else :
            break
    print('Mã học viên hợp lệ')
    # Lấy thông tin học viên theo code
    st = getStudentByCode(code)

    fullName = st['FullName']
    print('Họ tên: ', fullName)
    ans = input('Bạn có muốn thay đổi họ tên không (Y/N)? ')
    if ans.upper() == 'Y':
        while True:
            fullName = input('Họ tên mới: ')
            if fullName[0] != fullName[0].upper():
                print('Họ tên phải viết hoa chữ cái đầu')
                continue
            else: break
    st['FullName'] = fullName
    birthday = st['Birthday']
    print('Ngày sinh: ', birthday)
    ans = input('Bạn có muốn thay đổi ngày sinh không (Y/N)? ')
    if ans.upper() == 'Y':
        while True:
            birthday = input('Ngày sinh mới(dd/mm/yyyy): ')
            try:
                t1 = datetime.datetime.strptime(birthday, '%d/%m/%Y')
                t2 = datetime.datetime.now()
                if(t1 >= t2):
                    print('Ngày sinh không được lớn hơn ngày hiện tại')
                    continue
            except ValueError:
                 print('Date invalid')
            continue
            break
    st['Birthday'] = birthday
    writeStudent(st)
    print('Thay doi thong tin sinh vien thanh cong')
    #studentMenuScreen()




#Xóa học viên theo mã
def deleteStudentScreen():
    clearscreen()
    printHeader('XÓA HỌC VIÊN')
    while True:
        code = input('Mã học viên: ')
        if len(code) != 6:
            print('Mã học viên phải có 6 ký tự')
            continue
        isExists = checkExistsStudent(code)
        if isExists == False:
            print('Mã học viên không tồn tại')
            continue
        else:
            break
        
    sts = readStudents()
    idx = None
    for i, st in enumerate(sts):
        sts = readStudents()
        if st['Code'] == code:
            sts.pop(i)
            break
    writeStudents(sts)
    print('Xóa học viên thành công')
    printAllofList(sts)
    nextStep = input('Bạn có muốn tiếp tục xóa học viên không (Y/N)? ')
    if(nextStep.upper() == 'Y'):
        deleteStudentScreen()
    studentMenuScreen()

#Tìm kiếm học viên
def searchStudentsScreen():
    clearScreen()
    printHeader('TÌM KIẾM HỌC VIÊN')
    sts = readStudents()
    while True:
        st_name = input('Nhập tên học viên: ')
        if(st_name[0] != st_name[0].upper()):
            print('Họ tên phải viết hoa chữ cái đầu')
            continue
        else: break

    isFind = False
    for st in sts:
        if st['FullName'] == st_name:
            isFind = True
            print('\n'.join([f'{k}: {v}' for k,v in st.items()]))
            break
    
    if(isFind == False):
        print('Không tìm thấy học viên')
    
    ans = input('Bạn có muốn tiếp tục tìm kiếm học viên không (Y/N)? ')
    if ans.upper() == 'Y':
        searchStudentsScreen()
    studentMenuScreen()
