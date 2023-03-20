import re           # import llibrary Regex
from datetime import date
# input_patient = 0  
def inputpatient():

    global input_patient
    input_patient = input('{:<45} = '.format('Please Choose One of the Above Options Number'))
    if input_patient.isnumeric() == False:
        print('Error! Please Enter a Numerical Character!\n')
        return inputpatient()
    else:
        input_patient = input_patient
        return input_patient
def nodata ():
    print('ERROR! No Data Found. Please Insert the Right Option!\n')
def input_id (): # untuk filter ID yg dimasukkin in numeric form
    inputID = (input('{:<45} = '.format('Enter Patient ID [Numerics]')))
    if inputID.isnumeric() == False:
        print('Error! PATIENT ID Only Contains Numerical Characters\n')
        return input_id()
    else:
        inputID = int(inputID)
        return inputID
def input_id_existing ():
    inputID = input_id()
    if inputID not in patient_ID:
        print('PATIENT ID is Invalid. Please Enter Another ID\n')
        return input_id_existing()
    else:
        inputID = int(inputID)
        return inputID
def all_data ():
    order_ID = sorted(range(len(patient_ID)), key = lambda i: datapatient['PATIENT ID'] [i])
    header()
    for i in order_ID:
        print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [i]), (datapatient["FIRST NAME"] [i]), (datapatient["LAST NAME"] [i]), (datapatient["DOB"] [i]), (datapatient["AGE"] [i]), (datapatient["CITY"] [i])))


def input_existing_1name ():
    input_name = input('{:<45} = '.format('Enter Existing First Name')).title()
    if input_name not in first_name:
        print("FIRST NAME Isn't Available. Please Try Again\n")
        return input_existing_1name()
    else:
        input_name = str(input_name)
        return input_name
def input_existing_2name ():
    input_name = input('{:<45} = '.format('Enter Existing Last Name ')).title()
    if input_name not in last_name:
        print("LAST NAME Isn't Available. Please Try Again\n")
        return input_existing_2name()
    else:
        input_name = str(input_name)
        return input_name 
def input_existing_age ():
    input_age = (input('{:<45} = '.format('Enter Age')))
    if input_age.isnumeric() ==True:
        input_age =int(input_age)
        if input_age not in age2:
            print("AGE Isn't Available. Please Try Again\n")
            return input_existing_age()
        else:
            input_age = input_age
            return input_age  
    else:
        print('AGE should be in numerics')
        return input_existing_age()
def input_existing_dob ():
    input_dob = (input('{:<45} = '.format('Enter Date of Birth (YYYY-MM-DD)')))
    if input_dob not in age:
        print("Date of Birth Isn't Available. Please Try Again\n")
        return input_existing_dob()
    else:
        return input_dob   
def input_existing_city ():
    input_city = input('{:<45}= '.format('Enter City')).title()
    if input_city not in address:
        print("CITY Isn't Available. Please Try Again\n")
        return input_existing_city()
    else:
        input_city = str(input_city)
        return input_city
def header():
    PATIENT_ID = 'PATIENT ID'
    FIRST_NAME = 'FIRST NAME'
    LAST_NAME = 'LAST NAME'
    DOB = 'DOB'
    AGE = 'AGE'
    CITY = 'CITY'
    print()
    print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format(PATIENT_ID, FIRST_NAME, LAST_NAME,DOB,AGE,CITY))
    print('________________________________________________________________________________________________________________________')
def input_sure():
    input_sure_ans = input('{:<45} = '.format('Are You Sure?   [Y/N]')).capitalize()
    if input_sure_ans == 'Y':
        return input_sure_ans
    elif input_sure_ans == 'N':
        return input_sure_ans
    else:
        print('Error! Please Select "Y" or "N"\n')
        return input_sure()
def input_edit_again():
    input_sure_ans = input('{:<45}= '.format('Do You Want to Edit Another Data From This Patient?        [Y/N]')).capitalize()
    if input_sure_ans == 'Y':
        return input_sure_ans
    elif input_sure_ans == 'N':
        return input_sure_ans
    else:
        print('Error! Please Select "Y" or "N"\n')

def input_first_name():
    input_name1 = (input('{:<45} = '.format('Enter First Name'))).title() 
    empty = 0
    if re.match("^[A-Za-z\s\'\-\.]+$", input_name1):
    # for pattern matching 
    # ^ and $ marks start and ends with [] (a set of char)
    # + means one or more occurence
        input_name2 = list(input_name1)
        for i in input_name2:
            if i in (' ', "'" , '-', '.') or i.isalpha() == True:
                if i.isalpha() == True:
                    empty += 1
                else:
                    pass
            else:
                print('First Name Should Include At Least 1 Alphabet Character\n')
                return input_first_name()
        if empty >= 1:
            return str(input_name1)
        else:  
            print('First Name Should Include At Least 1 Alphabet Character\n')
            return input_first_name()
    else:
        print('First Name Should Only Contains Alphabet, Hyphen, or Apostrophe\n')
        return input_first_name()
    
def input_last_name():
    input_name1 = (input('{:<45} = '.format('Enter Last Name'))).title() 
    empty = 0
    if re.match("^[A-Za-z\'\-\.]+$", input_name1):
        input_name2 = list(input_name1)
        for i in input_name2:
            if i in ("'" , '-', '.') or i.isalpha() == True:
                if i.isalpha() == True:
                    empty += 1
                else:
                    pass
            else:
                print('Last Name Should Include At Least 1 Alphabet Character\n')
                return input_first_name()
        if empty >= 1:
            return str(input_name1)
        else:  
            print('Last Name Should Include At Least 1 Alphabet Character\n')
            return input_first_name()
    else:
        print('Last Name Should Only Contains Alphabet, Hyphen, and Apostrophe\n')
        return input_last_name()
def input_dob():            
    while True:
        user_input_dob = (input('{:<45} = '.format('Enter DOB   [YYYY-MM-DD]')))
        if re.match(r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[1-2]\d|3[0-1])$', user_input_dob):
            # \d means any number
            dob_input = date.fromisoformat(user_input_dob)
            # convert the DOB into a 'date' object
            today = date.today()
            if (today.year, today.month,today.day) > (dob_input.year , dob_input.month, dob_input.day) or (today.year, today.month,today.day) == (dob_input.year, dob_input.month, dob_input.day):
                return str(user_input_dob)
            else:
                print('Date of Birth Should not be in the Future. Please enter a Valid DOB')
                return input_dob()
        else:
            print("Invalid date format. Please enter DOB in YYYY-MM-DD format.")
            return input_dob()
        
def input_city():
    input_city1 = (input('{:<45} = '.format('Enter City'))).title()
    empty = 0
    if re.match("^[A-Za-z\s\-\'\.]+$", input_city1):
        input_city2 = list(input_city1)
        for i in input_city2:
            if i in ("'" , '-', '.', ' ') or i.isalpha() == True:
                if i.isalpha() == True:
                    empty += 1
                else:
                    pass
            else:
                print('City Should Include At Least 1 Alphabet Character\n')
                return input_city()
        if empty >= 1:
            return str(input_city1)
        else:  
            print('City Should Include At Least 1 Alphabet Character\n')
            return input_city()
    else:
        print('City Should Only Contains Alphabet, Hyphen, or Apostrophe\n')
        return input_city()
    
datapatient = { 
    'PATIENT ID' : [121, 122, 123, 124, 125],
    'FIRST NAME' : ['John', 'Taylor', 'John', 'Ady', 'Matthew'],
    'LAST NAME' : ['Kellen', 'Meijer', 'Kellen', 'Verwey', 'Meijer'],
    'DOB' : ['1999-11-15' , '1945-02-20' , '2021-04-12', '2021-07-23', '1986-11-11'],
    'AGE' : [],
    'CITY' : ['Utrecht', 'Utrecht', 'Zeewolde', 'Amsterdam', 'Warmond']
}
patient_ID = list(datapatient.values())[0]
keys_dict = list(datapatient.keys())
first_name = list(datapatient.values())[1]
last_name = list(datapatient.values())[2]
age = list(datapatient.values())[3]     # DOB
age2 = list(datapatient.values())[4]
address = list(datapatient.values())[5]

for i in range(len(age)):           # untuk cari age
    index_dob = age[i]
    birthdate = date.fromisoformat(index_dob)
    today = date.today()
    final_age = today.year -  birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    age2.append(final_age)

def reportmenu():
    print('''
-------------------- PATIENTS DATABASE REPORT --------------------
1. Preview All Database
2. Preview Certain Data
3. Back to Main Menu
------------------------------------------------------------------
''')   
    while True:
        input1 = int(inputpatient())
        if input1 == 1:
            if patient_ID == []:
                print('\n-----------------------------------  PATIENTS DATABASE -----------------------------------')
                print('There is No Data. Please Add a New Data')
                reportmenu()
            else:
                print('\n--------------------------------------------------  PATIENTS DATABASE --------------------------------------------------')      
                all_data()
                reportmenu()

        elif input1 == 2:
            if patient_ID == []:
                print('\n-----------------------------------  PREVIEW CERTAIN DATA -----------------------------------')
                print('There is No Data. Please Add a New Data')
                reportmenu()
            print('\n-------------------- PREVIEW CERTAIN DATA --------------------')
            while True:
                input_column = input('{:<45} = '.format('Enter Column [PATIENT ID / FIRST NAME / LAST NAME / DOB / AGE / CITY]')).upper()
                if input_column in keys_dict or input_column =='ID' or input_column =='NAME': 
                    if input_column =='PATIENT ID'  or input_column =='ID':
                        inputID1 = input_id_existing()
                        order_ke = patient_ID.index(inputID1)
                        header()
                        print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                    elif input_column == 'NAME':
                        input_name_choice = input('{:<45} = '.format('First Name or Last Name?   [FIRST/LAST]')).upper()
                        if input_name_choice == 'LAST':
                            input_2name = input_existing_2name()
                            header()
                            for order_ke in range(len(last_name)):
                                if datapatient['LAST NAME'][order_ke] == input_2name: # untuk match tiap index with the input
                                    print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                            reportmenu()
                        elif input_name_choice == 'FIRST':
                            input_1name = input_existing_1name()
                            header()
                            for order_ke in range(len(first_name)):
                                if datapatient['FIRST NAME'][order_ke] == input_1name:
                                    print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                            reportmenu()
                        else:
                            print('ERROR! Please Enter the Right Category\n')
                            continue
                    elif input_column == 'FIRST NAME':
                        input_1name = input_existing_1name()
                        header()
                        for order_ke in range(len(first_name)):
                            if datapatient['FIRST NAME'][order_ke] == input_1name:
                                print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                    elif input_column == 'LAST NAME':
                        input_2name = input_existing_2name()
                        header()
                        for order_ke in range(len(last_name)):
                            if datapatient['LAST NAME'][order_ke] == input_2name:
                                print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                    elif input_column == 'DOB':
                        input_dob1 = input_existing_dob()
                        header()
                        for order_ke in range(len(age)):
                            if datapatient['DOB'][order_ke] == input_dob1:
                                print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                    elif input_column == 'AGE':
                        input_age1 = int(input_existing_age())
                        header()
                        for order_ke in range(len(age2)):
                            if datapatient['AGE'][order_ke] == input_age1:
                                print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                    else:
                        input_city1 = input_existing_city()
                        header()
                        for order_ke in range(len(address)):
                            if datapatient['CITY'][order_ke] == input_city1:
                                print("{:^15} | {:^20} | {:^20} | {:^5} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                        reportmenu()
                else:
                    print("Category Isn't Available. Please Enter Category\n")
                    continue
        elif input1 ==3:
            mainmenu()
        else:
            nodata()
            continue
def addmenu():
   
    print('''
-------------------- ADD NEW PATIENT DATABASE --------------------
1. Add New Data
2. Back to Main Menu
------------------------------------------------------------------
''')
    while True:
        input2 = int(inputpatient())
        if input2 == 1:
            print('\n--------------------  ADD NEW DATA --------------------')
            if patient_ID == []: # to generate the first id
                id_first = print('{:<45} = {:<1}'.format('Patient ID', '121'))
                id_first = 121
            else:
                max_id = max(patient_ID) +1
                print('{:<45} = {:<1}'.format('Patient ID', max_id))
            while True:
                inputname1 = input_first_name()
                inputlastname1 = input_last_name()
                inputdob1= input_dob()
                
                # to calculate age from dob
                dob = date.fromisoformat(inputdob1)
                today = date.today()
                new_age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))

                inputcity1= input_city()
                if inputname1 in first_name and inputlastname1 in last_name and inputdob1 in age: # make sure there's already a previous data with the same info
                    order_ke = first_name.index(inputname1) and last_name.index(inputlastname1) and age.index(inputdob1)
                    while True:
                        same_sure = input(f'\nPatient with the Same Name and Date of Birth is Already Exist. \n(Patient ID = {patient_ID[order_ke]}) \nDo You Want To Continue?  [Y/N] = ').capitalize()
                        if same_sure == 'Y':
                            print(f'\nSUMMARY')
                            header()
                            if patient_ID ==[]:
                                print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format(id_first,inputname1,inputlastname1,inputdob1, new_age,inputcity1))
                            else:    
                                print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format(max_id,inputname1,inputlastname1,inputdob1, new_age,inputcity1))
                            print()
                            input_sure2 = input_sure()
                            if input_sure2 == 'Y':
                                if patient_ID == []:
                                    patient_ID.append(id_first)
                                else:
                                    patient_ID.append(max_id)
                                first_name.append(inputname1)
                                last_name.append(inputlastname1)
                                age.append(inputdob1)
                                age2.append(new_age)
                                address.append(inputcity1)
                                print('\nNew Data Added to the Patient Database')
                                addmenu()
                            elif input_sure2 == 'N':
                                print('\nCANCELLED!.')
                                addmenu()
                        if same_sure =='N':
                            addmenu()
                        else:
                            print("Please Enter 'Y' or 'N' ")
                            continue


                print(f'\nSUMMARY')
                header()
                if patient_ID ==[]:
                    print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format(id_first,inputname1,inputlastname1,inputdob1, new_age,inputcity1))
                else:    
                    print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format(max_id,inputname1,inputlastname1,inputdob1, new_age,inputcity1))
                print()
                input_sure2 = input_sure()
                if input_sure2 == 'Y':
                    if patient_ID == []:
                        patient_ID.append(id_first)
                    else:
                        patient_ID.append(max_id)
                    first_name.append(inputname1)
                    last_name.append(inputlastname1)
                    age.append(inputdob1)
                    age2.append(new_age)
                    address.append(inputcity1)
                    print('\nNew Data Added to the Patient Database')
                    addmenu()
                elif input_sure2 == 'N':
                    print('\nCANCELLED!.')
                    addmenu()
        elif input2 == 2:
            mainmenu()
        else:   
            nodata()
            continue
def editmenu():
    print('''\n
-------------------- EDIT PATIENT DATABASE --------------------
1. Edit Patient Database
2. Back to Main Menu
---------------------------------------------------------------

''')
    while True:
        input3 = int(inputpatient())
        if input3 == 1:
            if patient_ID == []:
                print('\n-----------------------------------  EDIT PATIENT DATA -----------------------------------')
                print('There is No Data. Please Add a New Data')
                editmenu()
            print('\n--------------------  EDIT PATIENT DATA --------------------')
            all_data()
            print()
            input3_ID = int(input_id_existing())
            order_ke = patient_ID.index(input3_ID)
            header()
            print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]),(datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
            print()
            input_sure3 = input_sure()
            if input_sure3 == 'Y':
                while True:
                    input_column = input('{:<45} = '.format('Enter column to edit [FIRST NAME/LAST NAME/DOB/CITY]')).upper()
                    if input_column in keys_dict or input_column == 'ID' or input_column == 'NAME':
                        if input_column == 'PATIENT ID' or input_column == 'ID':
                            print("You Can't Change Patient ID\n")
                            continue
                        elif input_column == 'AGE':
                            print("You Can't Edit Age\n")
                            continue
                        elif input_column =='NAME':
                            input_choice_name = input('{:<45} = '.format('First Name or Last Name? [FIRST/LAST]')).upper()
                            if input_choice_name == 'LAST':
                                 input_edit = str(input_last_name())
                                 input_column = 'LAST NAME'
                            elif input_choice_name == 'FIRST':
                                input_edit = str(input_first_name())
                                input_column = 'FIRST NAME'
                            else:
                                print('ERROR! Please Enter the Right Category to Edit!\n')
                                continue
                        elif input_column == 'FIRST NAME':
                            input_edit = str(input_first_name())
                        elif input_column == 'LAST NAME':
                            input_edit = str(input_last_name())
                        elif input_column == 'DOB':
                            input_edit = str(input_dob())
                        else :
                            input_edit = str(input_city()) 

                        while True:    
                            input_sure2 = input_sure()
                            if input_sure2 == 'Y':
                                print('\nDATA UPDATED!\n')
                                datapatient[input_column][order_ke] = input_edit    # change the value into the edited value
                                if input_column == 'DOB': # change the patient's age if the edited column is dob
                                    dob_edit = date.fromisoformat(input_edit)
                                    today = date.today()
                                    new_edit_age = today.year - dob_edit.year - ((today.month, today.day) < (dob_edit.month, dob_edit.day))
                                    datapatient['AGE'][order_ke] = new_edit_age
                                header()
                                print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]),(datapatient["CITY"] [order_ke])))
                                print()
                                input_edit_more = input_edit_again() # edit more column
                                if input_edit_more == 'Y':
                                    break
                                else:
                                    editmenu()
                            else:
                                editmenu()  
                    else:
                        print("Column Isn't Available!\n")
                        continue  

            elif input_sure3 == 'N':
                editmenu()
        elif input3 ==2:
            mainmenu()
        else:
            nodata()
            continue
def deletemenu():
    print('''
-------------------- DELETE PATIENT DATABASE --------------------
1. Delete Patient Database
2. Back to Main Menu
-----------------------------------------------------------------

''')
    while True:
        input4 = int(inputpatient())
        if input4 == 1:
            if patient_ID == []:
                print('\n-----------------------------------  DELETE PATIENT DATA -----------------------------------')
                print('There is No Data Left')
                deletemenu()
            print('\n--------------------  DELETE PATIENT DATA --------------------')
            all_data()
            print()
            while True:
                input4_ID = int(input_id_existing())
                order_ke = patient_ID.index(input4_ID)
                header()
                print("{:^15} | {:^20} | {:^20} | {:^10} | {:^20}| {:^20}".format((datapatient["PATIENT ID"] [order_ke]), (datapatient["FIRST NAME"] [order_ke]), (datapatient["LAST NAME"] [order_ke]), (datapatient["DOB"] [order_ke]), (datapatient["AGE"] [order_ke]), (datapatient["CITY"] [order_ke])))
                input_sure4 = input_sure()
                if input_sure4 == 'Y':
                    print('\nData Has Been Successfully Deleted\n')
                    del datapatient["PATIENT ID"] [order_ke]
                    del datapatient["FIRST NAME"] [order_ke]
                    del datapatient["LAST NAME"] [order_ke]
                    del datapatient["AGE"] [order_ke]
                    del datapatient["CITY"] [order_ke]
                    deletemenu()
                elif input_sure4 == 'N':
                    deletemenu()
                else:
                    nodata()
                    continue
        elif input4 == 2:
            mainmenu()
        else:
            nodata()
            continue
def mainmenu():
    print('''
-------------------- HOSPITAL DATABASE --------------------
1. Patients Database Report
2. Add New Patient Data
3. Edit Existing Patient Data
4. Delete Existing Patient Data
5. Exit
-----------------------------------------------------------
''')
    while True: 
        input_main_menu = int(inputpatient())
        if input_main_menu == 1:
            reportmenu()
        elif input_main_menu ==2:
            addmenu()
        elif input_main_menu ==3:
            editmenu()
        elif input_main_menu ==4:
            deletemenu()
        elif input_main_menu ==5:
            sure_exit = input_sure()
            if sure_exit == 'Y':
                print('GOOD BYE!')
                exit()     
            else:
                mainmenu()
        else:
            nodata()
            continue
        
mainmenu()
        





 



