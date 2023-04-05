#
#   PROJECT : Email Spam Filtering
# 
#   FILENAME : email_data.py
# 
#   DESCRIPTION :
#       ...
# 
#   FUNCTIONS :
#       main()
# 
#   NOTES :
#       - ...
# 
#   AUTHOR(S) : Noah Da Silva               START DATE : 2022.12.02 (YYYY.MM.DD)
#
#   CHANGES :
#       - ...
# 
#   VERSION     DATE        WHO             DETAILS
#   0.0.1a      2022.12.02  Noah            Creation of project.
#

import win32com.client
from email.parser import HeaderParser, Parser

import os
import json


class EmailData:
    #
    # NOTE:
    #
    def __init__(self):
        pass

    #
    # NOTE: 
    #
    def search_for_json_file(self):
        found_json = False
        for file in os.listdir():       # Go through each file in the directory
            if file.endswith('.json'):  # If it ends with .json, we will import it
                if found_json is False:
                    print(f'Found a json file: {file}', end='')
                    found_json = True
                else:
                    print(f', {file}', end='')

        if found_json is False:
            print('Could not find a json file.')
        else:
            print()

    #
    # NOTE: 
    #
    def send_mail(self, filename=None):
        if filename is None or not os.path.isfile(filename):    # Check if file exists
            print('There was a problem fetching your email data. Looking for json file...')
            self.search_for_json_file()
            return  # Exit the function if the filename does not exist
        
        # Read the data
        file = open(filename)
        data = json.load(file)

        outlook = win32com.client.Dispatch('Outlook.Application')    # Connect Python and Microsoft's email application

        for entry in data:  # Go through each email in the data
            outlook_mail_item = 0x0                             # Define the size of the new email
            new_mail = outlook.CreateItem(outlook_mail_item)    # Create a new email draft

            to = []
            for recipient in entry['recipients']['to']:
                if not recipient == "":
                    to.append(recipient)
            new_mail.To = ';'.join(to)

            cc = []
            for recipient in entry['recipients']['cc']:
                if not recipient == "":
                    cc.append(recipient)
                new_mail.CC = ';'.join(cc)

            new_mail.Subject = entry["subject"]

            for attachment in entry['attachments']:
                if not attachment == "":
                    new_mail.Attachments.Add(attachment)

            new_mail.Body = entry["body"]

            #new_mail.Display()  # Preview of your email in Outlook
            new_mail.Send()     # Send the email

        file.close()    # Close the file

    #
    # NOTE: 
    #
    def fetch_all_mail(self):
        outlook = win32com.client.Dispatch('Outlook.Application')    # Connect Python and Microsoft's email application
        mapi = outlook.GetNamespace("MAPI")

        messages = []
        for root_folder in mapi.Folders:
            for folder in root_folder.Folders:  # Iterate through each folders in mailbox
                for item in folder.Items:
                    # If item contains an email header
                    if item.PropertyAccessor.GetProperty("http://schemas.microsoft.com/mapi/proptag/0x007D001F"):
                        messages.append(item)   # Save message to list

        return messages

    #
    # NOTE: 
    #
    def save_mail_to_json(self, messages=None, location=None):
        if messages is None:
            print('No data was provided.')
            return
        elif location is None:
            print('No save location was provided.')
            return

        json_data = []
        counter = 0
        for mail in messages:
            if str(mail) == '<COMObject <unknown>>':
                continue
            counter += 1
            mail_data = {
                'Date': str(mail.ReceivedTime),
                'To': mail.To.strip().encode("ascii", "ignore").decode(),
                'CC': mail.CC.strip().encode("ascii", "ignore").decode(),
                'SenderName': mail.SenderName.strip().encode("ascii", "ignore").decode(),
                'SenderAddress': mail.SenderEmailAddress.strip().encode("ascii", "ignore").decode(),
                'Subject': mail.Subject.strip().encode("ascii", "ignore").decode(),
                'Attachments': len(mail.Attachments),
                'Body': " ".join(mail.Body.strip().encode("ascii", "ignore").decode().split()),
                'Header': dict(HeaderParser().parsestr(mail.PropertyAccessor.GetProperty("http://schemas.microsoft.com/mapi/proptag/0x007D001F").strip().encode("ascii", "ignore").decode()))
            }
            json_data.append(mail_data)

        with open(location, 'w') as f:
            json.dump(json_data, f)

        print(f'Saved {counter} emails to json file.')