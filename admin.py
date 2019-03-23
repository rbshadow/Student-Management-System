import getpass
import os
import platform
import time
import header_design
from main import StartMain
import preloader

tab = '\t'
operating_system = platform.system()


class Admin:

    # Login System as Admin
    def authentication(self):
        if operating_system == 'Linux':
            os.system('clear')
        elif operating_system == 'Windows':
            os.system('cls')

        header_design.art('Login Page')
        print(tab + ' ' * 5 + '[!] Default username and password is "admin"\n')
        print(tab * 3 + 'Username: admin')
        password = getpass.getpass(tab * 3 + 'Password: ')

        chance = 3
        if password == 'admin':

            msg = '[!] Login In. \n\n' + tab * 4 + 'Please wait'
            for i in range(5):
                preloader.load(msg)

            time.sleep(.05)
            print('\n[!] Successfully Logged In')
            time.sleep(.5)
            if operating_system == 'Linux':
                os.system('clear')
            elif operating_system == 'Windows':
                os.system('cls')

            StartMain.main(self)

        else:
            while password != 'admin':
                chance -= 1

                if chance != 0:
                    print('[✘] Wrong password!. You have ' + str(chance) + ' chances left')
                    password = getpass.getpass()
                    if password == 'admin':

                        msg = '[!] Login In. \n\n' + tab * 4 + 'Please wait'
                        for i in range(5):
                            preloader.load(msg)

                        print('\n[✔] Successfully Logged In')
                        time.sleep(.5)
                        StartMain.main(self)

                else:
                    msg = '[✘] Failed to login!\n\n' + tab * 4 + 'Exiting'
                    for i in range(5):
                        preloader.load(msg)
                    time.sleep(2)
                    exit()
