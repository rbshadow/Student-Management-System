import os
import platform
import csv
import time
from prettytable import from_csv
import header_design as design
import main
import preloader

tab = '\t'
operating_system = platform.system()


def id_generator():
    id_list = []
    default_student_id = 1001
    try:
        with open('student_database.csv', 'r') as fr:
            data = csv.reader(fr)
            for student_id in data:
                id_list.append(student_id[0])
            student_id = int(id_list[-1]) + 1
            return student_id
    except Exception:
        return default_student_id


# Adding New Student
def student_input():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    design.art('New Student Form')
    student_id = id_generator()
    first_name = input('[+] Enter first name: ')
    middle_name = input('[+] Enter middle name: ')
    last_name = input('[+] Enter last name: ')
    age = input('[+] Enter age: ')
    gender = input('[+] Enter gender: ')
    department = input('[+] Enter department: ')

    while True:
        confirm = input('\n[!] Do you want to save? (y/n): ').lower()
        if confirm == 'y':
            if middle_name:
                name = first_name + ' ' + middle_name + ' ' + last_name

                # Saving information
                with open('student_database.csv', 'a', newline='') as fs:
                    data = csv.writer(fs)
                    data.writerow([student_id, name, age, gender, department])
            else:
                name = first_name + ' ' + last_name

                # Saving information
                with open('student_database.csv', 'a', newline='') as fs:
                    data = csv.writer(fs)
                    data.writerow([student_id, name, age, gender, department])
            print()

            msg = '[!] Please wait. \n\n' + tab * 4 + 'Saving'
            for i in range(5):
                preloader.load(msg)
            print('\n[✔] Saved')
            time.sleep(.5)

            main.StartMain.main(self='self')
            break
        elif confirm == 'n':
            print()
            msg = tab * 4 + '[!] Please wait'
            for i in range(5):
                preloader.load(msg)
            time.sleep(.5)
            main.StartMain.main(self='self')
            break
        else:
            print()
            print('[X] Wrong Input!')
            time.sleep(.50)


# Show student database
def student_database():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')
    design.art('Student Database')

    try:
        with open('student_database.csv', 'r') as fr:
            data_table = from_csv(fr, field_names=['Student ID', 'Student Name', 'Age', 'Gender', 'Department'])

        # Show student database
        print(data_table)
    except Exception as e:
        print(e)
        print('\nNot data available. Please add some student first.\n')

    choice = input('\nPlease enter your choice:\n'
                   '[1] Main Menu\n'
                   '\n'
                   'admin@sms:~$ ')

    if choice == '1':
        main.StartMain.main(self='self')
    else:
        print()
        print('[X] Wrong Input!')
        time.sleep(.50)
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')
        student_database()


def search_student(search='id'):
    if search == 'id':
        print('[1] Searching by ID')
    elif search == 'first_name':
        print('[2] Searching by First Name')


def search():
    if operating_system == 'Linux':
        os.system('clear')
    elif operating_system == 'Windows':
        os.system('cls')

    choice = input('Please enter your choice:\n'
                   '[1] Search by ID\n'
                   '[2] Search by First Name\n'
                   '[3] Back to Main Menu\n'
                   '\n'
                   'admin@sms:~$ ')
    if choice is '1':
        search_student(search='id')
    elif choice is '2':
        search_student(search='first_name')
    elif choice is '3':
        pass
    else:
        print()
        print('[X] Wrong Input!')
        time.sleep(.50)
        search()
