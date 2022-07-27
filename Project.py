import PySimpleGUI as sg
import time
import csv

def write_in_csv(Mail, Username, Password):

    List=[Mail, Username, Password]

    with open('Database.csv', 'a', newline='') as f_object:
        writer_object = csv.writer(f_object)
        writer_object.writerow(List)
        f_object.flush
        f_object.close()


def read_from_csv():
    Usernames = []
    Passwords = []
    Mailids = []
    with open('Database.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        count = 0
        for row in csv_reader:
            if count == 0:
                pass
            else:
                Mailids.append(row[0])
                Usernames.append(row[1])
                Passwords.append(row[2])
            count += 1

    return Mailids,Usernames,Passwords

def check_password(passwd):
    if len(passwd) > 5 and len(passwd) < 16:
        for x in '''-=[]\\;',./!@#$%^&*()_+{}|:"<>?~`''':
            if x in passwd:
                special = True
                break
        else:
            special = False

        if special:
            for x in '''1234567890''':
                if x in passwd:
                    number = True
                    break
            else:
                number = False

            if number:
                for x in '''QWERTYUIOPASDFGHJKLZXCVBNM''':
                    if x in passwd:
                        Upper = True
                        break
                else:
                    Upper = False

                if Upper:
                    for x in '''qwertyuiopasdfghjklzxcvbnm''':
                        if x in passwd:
                            Lower = True
                            break
                    else:
                        Lower = False

                    if Lower:
                        Proper_passwd = True
                    
                    else:
                        Proper_passwd = False
                else:
                    Proper_passwd = False
            else:
                Proper_passwd = False

        else:
            Proper_passwd = False
    else:
        Proper_passwd = False

    if Proper_passwd:
        return True
    else:
        return False

def registration(Mailids, Usernames, Passwords):
    column_to_be_centered = [ [sg.Button('Back')], [sg.Button('Register')]]
    column_to_be_right = [  [sg.Text('Email ID'), sg.InputText()],
                            [sg.Text('Username'), sg.InputText()],
                            [sg.Text('Password'), sg.InputText()]]

    layout = [  [sg.Column(column_to_be_right, vertical_alignment='right', justification='right')],
                [sg.Column(column_to_be_centered, vertical_alignment='center', justification='center',  k='-C-')]]
                

    window = sg.Window('Window Title', layout)  

    while True:             
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event == ('Back'):
            window.close()
            Main_Windows()
        mail = list(values[0])

        if values[0] not in Mailids:
            if "@" in mail and "." in mail:
                if mail.index("@")+1 <  mail.index("."):
                    if mail[0] not in '''1234567890-=[]\\;',./!@#$%^&*()_+{}|:"<>?~`''':
                        Proper_Mail = True
                    else:
                        Proper_Mail = False
                else:
                    Proper_Mail = False
            else:
                Proper_Mail = False
        else:
            sg.Popup('Email Already Exists', keep_on_top=True)
            Proper_Mail = False

        passwd = list(values[2])

        if len(passwd) > 5 and len(passwd) < 16:
            for x in '''-=[]\\;',./!@#$%^&*()_+{}|:"<>?~`''':
                if x in passwd:
                    special = True
                    break
            else:
                special = False

            if special:
                for x in '''1234567890''':
                    if x in passwd:
                        number = True
                        break
                else:
                    number = False

                if number:
                    for x in '''QWERTYUIOPASDFGHJKLZXCVBNM''':
                        if x in passwd:
                            Upper = True
                            break
                    else:
                        Upper = False

                    if Upper:
                        for x in '''qwertyuiopasdfghjklzxcvbnm''':
                            if x in passwd:
                                Lower = True
                                break
                        else:
                            Lower = False

                        if Lower:
                            Proper_passwd = True
                        
                        else:
                            Proper_passwd = False
                    else:
                        Proper_passwd = False
                else:
                    Proper_passwd = False

            else:
                Proper_passwd = False
        else:
            Proper_passwd = False

        username = list(values[1])

        if values[1] not in Usernames:
            if username != []:
                Proper_Username = True

            else:
                Proper_Username = False
        else:
            sg.Popup('Username Already Exists', keep_on_top=True)
            Proper_Username = False



        if event in ('Register'):
            if Proper_Username and Proper_passwd and Proper_Mail:
                sg.Popup('Registered Succesfully', keep_on_top=True)
                time.sleep(1)

                write_in_csv(values[0], values[1], values[2])
                window.close()
                Main_Windows()
            elif not Proper_Mail:
                sg.Popup('Incorrect Mail ID', keep_on_top=True) 
            elif not Proper_Username:
                sg.Popup('Incorrect Username', keep_on_top=True) 
            elif not Proper_passwd:
                sg.Popup('Incorrect Password', keep_on_top=True)


def Logged_In():
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Logged In')],
                [sg.Button('Exit')]]

    window = sg.Window('Logged In', layout, element_justification='c')

    while True:             
        event, values = window.Read()
        if event in (None, 'Exit'):
            break

    window.close()

def Forgot_Password(Mailids, Usernames, Passwords):
    sg.theme('DarkAmber')

    layout = [  [sg.Text('Email ID'), sg.InputText()],
                [sg.Text('Username'), sg.InputText()],
                [sg.Text('New Password'), sg.InputText()],
                [sg.Text('Confirm Password'), sg.InputText()],
                [sg.Button('Exit'), sg.Button('Login')]]

    window = sg.Window('Logged In', layout, element_justification='c')

    while True:             
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        
        email = values[0]
        username = values[1]
        new_password = values[2]
        confirm_password = values[3]

        for x in Mailids:
            if x == email:
                mail_found = True
                index = Mailids.index(x)
            else:
                mail_found = False
                

        if mail_found:
            if Usernames[index] == username:
                username_found = True
            else:
                username_found = False
        else:
            sg.Popup('Incorrect Mail ID', keep_on_top=True)
            username_found = False
            


        if username_found:
            if check_password(new_password) == False:
                sg.Popup('Incorrect Password', keep_on_top=True)

            elif new_password == confirm_password:
                Mailids, Usernames, Passwords = read_from_csv()
                window.close()
                Passwords[index] = new_password
                length = len(Mailids)
                n = 0
                List = ['Mail','Username','Password']
                with open('Database.csv', 'w', newline='') as f_object:
                    writer_object = csv.writer(f_object)
                    writer_object.writerow(List)
                    f_object.flush
                    f_object.close()
                while n < length:
                    List=[Mailids[n], Usernames[n], Passwords[n]]
                    n += 1

                    with open('Database.csv', 'a', newline='') as f_object:
                        writer_object = csv.writer(f_object)
                        writer_object.writerow(List)
                        f_object.flush
                        f_object.close()
                login(Mailids, Usernames, Passwords)
            else:
                sg.Popup('Passwords do not match', keep_on_top=True)
        else:
            sg.Popup('Incorrect Username', keep_on_top=True)


    window.close()



def login(Mailids, Usernames, Passwords):
    column_to_be_centered = [ [sg.Button('Login')], [sg.Button('Back')]]
    column_to_be_centered2 = [ [sg.Button('Forgot Password')],[sg.Button('Register')]]
    column_to_be_right = [  [sg.Text('Username'), sg.InputText()],
                            [sg.Text('Password'), sg.InputText()]]

    layout = [  [sg.Column(column_to_be_right, vertical_alignment='right', justification='right')],
                [sg.Column(column_to_be_centered, vertical_alignment='center', justification='center',  k='-C-')],
                [sg.Column(column_to_be_centered2, vertical_alignment='right', justification='right',  k='-R-')]]
                

    window = sg.Window('Login', layout)  

    while True:             
        event, values = window.read()

        if event == sg.WIN_CLOSED:
            break
        if event in ('Back'):
            window.close()
            Main_Windows()
        if event in ('Register'):
            window.close()
            Mailids, Usernames, Passwords = read_from_csv()
            registration(Mailids, Usernames, Passwords)
        
        if event in ('Login'):
            username = values[0]
            Password = values[1]

            Mailids, Usernames, Passwords = read_from_csv()

            for x in Usernames:
                if x == username:
                    username_found = True
                    username = x
                    break
                else:
                    username_found = False
                    

            if username_found:
                index = Usernames.index(x)
                passwd = Passwords[index]

                if passwd == Password:
                    window.close()
                    Logged_In()
                    break
                else:
                    sg.Popup('Login Failed Incorrect Password', keep_on_top=True)


            else:
                sg.Popup('Username not found you can register', keep_on_top=True) 
                 

        if event in ('Forgot Password'):
            window.close()
            Mailids, Usernames, Passwords = read_from_csv()
            Forgot_Password(Mailids, Usernames, Passwords)

    window.close()



def Main_Windows():

    sg.theme('DarkAmber')

    layout = [  [sg.Text('Welcome to Registration BOT')],
                [sg.Button('Registration'), sg.Button('Login')],
                [sg.Button('Exit')]]

    window = sg.Window('Window Title', layout, element_justification='c')

    while True:             
        event, values = window.Read()
        if event in (None, 'Exit'):
            break
        if event == 'Registration':
            window.close()
            Mailids, Usernames, Passwords = read_from_csv()
            registration(Mailids, Usernames, Passwords)
        if event == 'Login':
            window.close()
            Mailids, Usernames, Passwords = read_from_csv()
            login(Mailids, Usernames, Passwords)

    window.close()



Main_Windows()