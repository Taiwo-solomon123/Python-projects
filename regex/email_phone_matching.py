import pyperclip
import re


def find_phone_numbers(text):
    phone_pattern=re.compile(r"""(
                       (\(?\d{3}\)?)?           #Area code(Optional)
                       (\s|\.|-)?               #Seperator(Optional)
                       (\d{3})                  #First 3 digits
                       (\s|\.|-)                #Seperator
                       (\d{4})                  #Last 4 digits
                       )""", re.VERBOSE)
    phone_number_groups=phone_pattern.findall(text)
    extracted_phone_numbers=[]
    for group in phone_number_groups:
        phone_number=group[0]
        extracted_phone_numbers.append(phone_number)
    return extracted_phone_numbers

def find_emails(text):
    #username@domainname.domain
    email_pattern=re.compile(r"""(
                             ([a-zA-Z0-9._+%-]+)       #username
                             (@)                
                             ([a-zA-Z0-9.-]+)             #domain name
                             (\.)               #seperator
                             (\w+){2,4}        #Domain
                             )""", re.VERBOSE)
    email_groups=email_pattern.findall(text)
    extracted_emails=[]
    for group in email_groups:
        email=group[0]
        extracted_emails.append(email)
    return extracted_emails

def copy_emails_phones(email_list, phone_number_list):
    emails_and_phone_numbers=[]
    emails_and_phone_numbers.extend(email_list)
    emails_and_phone_numbers.extend(phone_number_list)
    
    result=("\n").join(emails_and_phone_numbers)
    clipboard_copy=pyperclip.copy(result)
    print(result)
    
def main():
    
    text="""
        Maths class is tehe dumbest.....092-722-2332
        solsdhdgw73n@gmail.com sdhkaffb
        my phone is: (344)-434-4211
        feddsw 343-3321
        new email: demiladetaiwo20@gmail.com
        """
    emails=find_emails(text)
    phone_numbers=find_phone_numbers(text)

    copy_emails_phones(email_list=emails, phone_number_list=phone_numbers)

if "__main__"==__name__:
    main()

