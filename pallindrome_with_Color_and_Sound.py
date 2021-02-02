from logzero import logger  as log
from winsound import Beep as beep
import time,os


start=time.time()
print('''
 Dhyan se padho isko aur samjho  ...
     "Wash your sins, not only your face"

    +---------------------------------------------+
    |                                             |
    |    1. Type 'done' when done.                |
    |    2. Type 'quit' when you wanna quit.      |
    |    3. Type 'exit' when you wanna exit.      |
    |                                             |
    +---------------------------------------------+

 Note : done, quit and exit are not pallindromes
''')

c=1
lop=[]
#I will make this code colorful and how much time spend on this programe
#store the list of pallindrome in a list and count them. (lop,LOP) List of all Pallindrome till now


while True: #After running this code for once you can check for infinite no. of word, numbers and phrase
    user_input=input(str(c)+'.'+'\tCheck for Pallindrome : ')  #Let's take the user input
    modified_user_input=user_input #This will be modified below hence stored in a separate variable
    if user_input.lower() in ['done','exit','quit']:print('\tThank you! Have a nice day ♥'); break  #This will terminate the programe on user input
    else:
        punctuation='!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~' 
        for i in user_input:
            if i in punctuation:
                modified_user_input=modified_user_input.replace(i,'') #removing punctuation from user_input and storing it in modified_user_input
        a=modified_user_input.replace(' ','') #modified_user_input with no space
        if a.isalpha(): #checking for alphabet only
            b=a.lower() #lowering the case to match
            if b==b[::-1]: 
                print('\t\033[32m"'+user_input+'"','is Pallindrome.\033[1;37;40m'); beep(4000,300)
                lop.append(user_input)
            else:
                print('\t\033[31m"'+user_input+'"','is not Pallindrome.\033[1;37;40m'); beep(1000,500)
        elif user_input=='': #code for no input and pressed enter key
            print('\n\t\033[33m"Kuch nahi ko kisi bhi tarah\n\t kuch nahi padha jaa sakta hai"\n \033[36m',' \t-Ajay Kisku\033[1;37;40m'.rjust(46))
            
        elif a==a[::-1]: #This will check digits and Hindi letters
            print('\t\033[32m"'+user_input+'"','is Pallindrome.\033[1;37;40m'); beep(4000,300)
            lop.append(user_input)
        else:
            print('\t\033[31m"'+user_input+'"','is not Pallindrome.\033[1;37;40m'); beep(1000,400)
        print()
        print('-'*os.get_terminal_size()[0]) ; c+=1 #Seperator line for clean looks and increment of 1 for serial no.
    

stop=time.time()
print()
print('>'*os.get_terminal_size()[0])
print('Your Pallindromes  :',list(set(lop))) #removing duplicates
print('\nTotal Pallindromes :',len(set(lop)))
print('Total Time Spend   :',time.strftime('%H:%M:%S',time.gmtime(round(stop-start))))
print()
print('>'*os.get_terminal_size()[0])


input('Press Enter Key to Close')