import time
import os
import platform
import header_design as design
import student as st
import preloader

tab = '\t'
operating_system = platform.system()


class StartMain:

    # Main Function
    @staticmethod
    def main(self):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')

        design.art('Student Management System')

        choice = input('Please enter your choice:\n'
                       '[1] Add student\n'
                       '[2] Show student database\n'
                       '[3] Search student\n'
                       '[4] Exit the program\n'
                       '\n'
                       'admin@sms:~$ ')
        if choice is '1':
            st.student_input()
        elif choice == '2':
            st.student_database()
        elif choice is '3':
            st.search_student()
        elif choice is '4':
            print()

            msg = '[☺] Thanks for using this program. See you soon.\n\n' + tab * 4 + 'Exiting'
            for i in range(3):
                preloader.load(msg)
            time.sleep(1)
            exit()
        else:
            print()
            print('[✘] Wrong Input!')
            time.sleep(.50)
            StartMain().main(self)
