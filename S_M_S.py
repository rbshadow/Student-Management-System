import time
import os
import getpass
import sys
import csv
from prettytable import from_csv


class StudentInfo:

    @staticmethod
    def welcome_banner():
        print('''                        
                        ######################################
                        ##### Student Management System  #####
                        ######################################
            ''')

    @staticmethod
    def design(function_name='Default'):
        print('                    ######################################')
        print('                        ######## ' + function_name + ' #########')
        print('                    ######################################')

    @staticmethod
    def loader(string='###LOADING...###'):
        os.system('clear')
        print('\n\n\n\n\n\n')
        for char in string:
            print(char, end='')
            sys.stdout.flush()
            time.sleep(0.02)
        print()

    # Login System as Admin
    def authentication(self):
        os.system('clear')
        self.design('Login Page')
        print('Please enter password for "Admin"')
        password = getpass.getpass()

        chance = 3

        if password == 'password':
            print('\nLogin In...')
            time.sleep(1)
            self.loader('Loading...#######################################..Complete')
            self.main()
        else:
            while password != 'password':
                chance -= 1
                if chance != 0:
                    print('Wrong password!. You have ' + str(chance) + ' chances left')
                    password = getpass.getpass()
                    if password == 'password':
                        print('\nLogin In...')
                        time.sleep(1)
                        self.loader('Loading...#######################################...Complete')
                        self.main()
                else:
                    print('\nFailed to login!')
                    print('Exiting...')
                    time.sleep(2)
                    exit()

    @staticmethod
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
    def student_input(self):
        os.system('clear')
        self.design('Add Student')
        student_id = self.id_generator()
        first_name = input('Enter first name: ')
        middle_name = input('Enter middle name: ')
        last_name = input('Enter last name: ')
        age = input('Enter age: ')
        gender = input('Enter gender: ')

        while True:
            confirm = input('\nDo you want to save? (y/n): ').lower()
            if confirm == 'y':
                if middle_name:
                    name = first_name + ' ' + middle_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a') as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender])
                else:
                    name = first_name + ' ' + last_name

                    # Saving information
                    with open('student_database.csv', 'a') as fs:
                        data = csv.writer(fs)
                        data.writerow([student_id, name, age, gender])
                print()
                print('Saving...')
                time.sleep(.5)
                self.main()
                break
            elif confirm == 'n':
                print()
                print('Backing to the main menu...')
                time.sleep(.5)
                self.main()
                break
            else:
                print()
                print('[X] Wrong Input!')
                time.sleep(.50)

    # Show student database
    def student_database(self):
        os.system('clear')
        self.design('Student Database')

        try:
            with open('student_database.csv', 'r') as fr:
                data_table = from_csv(fr, field_names=['Student ID', 'Student Name', 'Age', 'Gender'])

            # Show student database
            print(data_table)
        except Exception:
            print('\nNot data available. Please add some student first.\n')

        choice = input('\nPlease enter your choice:\n'
                       '[1] Main Menu\n')
        if choice == '1':
            self.main()
        else:
            print()
            print('[X] Wrong Input!')
            self.student_database()

    @staticmethod
    def search_student(search='id'):
        if search == 'id':
            print('Searching by ID')
        elif search == 'first_name':
            print('Searching by First Name')

    def search(self):
        os.system('clear')
        self.design('Search')

        choice = input('Please enter your choice:\n'
                       '[1] Search by ID\n'
                       '[2] Search by First Name\n'
                       '[3] Back to Main Menu\n')
        if choice is '1':
            self.search_student(search='id')
        elif choice is '2':
            self.search_student(search='first_name')
        elif choice is '3':
            self.main()
        else:
            print()
            print('[X] Wrong Input!')
            time.sleep(.50)
            self.search()

    # Main Function
    def main(self):
        os.system('clear')
        self.welcome_banner()

        choice = input('Please enter your choice:\n'
                       '[1] Add student\n'
                       '[2] Show student database\n'
                       '[3] Search student\n'
                       '[4] Exit the program\n')
        if choice is '1':
            self.student_input()
        elif choice == '2':
            self.student_database()
        elif choice is '3':
            self.search()
        elif choice is '4':
            print()
            print('Thanks for using this program. See you soon.')
            print('Exiting...')
            time.sleep(1)
            exit()
        else:
            print()
            print('[X] Wrong Input!')
            time.sleep(.50)
            self.main()


if __name__ == '__main__':
    si = StudentInfo()
    si.authentication()
