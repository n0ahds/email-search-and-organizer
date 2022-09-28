try:
    import win32com.client
    from dotenv import load_dotenv
except:
    print('Could not import some pywin32.')


import os
from pathlib import Path
import json

import folder_tuples as ft
import label_tuples as lt

try:
    # Set path for environment variable
    BASE_DIR = Path(__file__).resolve()

    # Setup the environment variables.
    load_dotenv()
    ENV_PATH = os.path.join(BASE_DIR, '.env')
    load_dotenv(dotenv_path=ENV_PATH)

    # Retrieve environment variable.
    EMAIL_ADDRESS = str(os.getenv("EMAIL_ADDRESS"))
except:
    print('dotenv was not imported.')


#
# Look for a json file in the directory.
#
def search_for_json_file():
    json_data = []
    # Go through each file in the directory.
    for file in os.listdir():
        # If it ends with .json, we will import it.
        if file.endswith('.json'):
            json_data = json.load(open(file, "r", encoding="utf-8"))
            print('Found a json file: ' + file)
            # Return the file data.
            return json_data
    # If we couldn't find a file, return an empty list.
    print('Could not find a json file.')
    return []


#
# Retrieve all folders from email client.
#
def get_email_folders():
    # Setup connection to email client (outlook in this case).
    outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
    root = outlook.Folders[EMAIL_ADDRESS]
    folder_root = root.Folders["Folders"]

    all_folders = []    # Initiate folders list.

    # Go through all folders under the root directory.
    for i in root.Folders:
        all_folders.append(i)
    # Go through sub folders inside the 'folders' directory.
    for i in folder_root.Folders:
        all_folders.append(i)

    return all_folders  # Return list of all folder names.


#
# Pull the data from every email in the email client.
#
def extract_email_data(all_folders):
    inbox_data = [] # Initialize list of messages.
    
    # Go through every folder.
    for folder in all_folders:
        # In each folder, go through every message.
        for message in folder.Items:
            recipients = [] # Initialize recipient list.
            # Add each recipient in message to the list.
            for recipient in message.Recipients:
                recipients.append(recipient.Address)
            
            inbox_data.append({ # Format list entry for json print-out.
                    'Name': str(message.SenderName),
                    'Sender': str(message.SenderEmailAddress),
                    'Recipients': str(recipients),
                    'Date': str(message.ReceivedTime),
                    'Subject': str(message.Subject),
                })
    # Export data to json file.
    json.dump(inbox_data, open("inbox_data.json", "w"))
    # Return data in json format.
    return json.dumps(inbox_data)


#
# Sorting function.
# NOTE: Here we set our preferred sorting conditions.
# We will divide the needed keyworks into libraries.
#
def sort_mail_into_folders(json_data):
    sorted_data = []    # Initialize our sorted email list.
    unsorted_data = []  # Initialize our unsorted email list.
    sent_data = []
    
    # Conditional list
    gaming_data = []
    finance_data = []
    entertainment_data = []
    shopping_data = []
    social_data = []
    government_data = []
    cloud_data = []
    health_data = []
    development_data = []
    friends_family_data = []
    learning_data = []
    service_data = []
    product_data = []
    business_data = []
    provider_data = []

    # NOTE: Sorting emails into
    # Loop through every entry in json file.
    for i in json_data:
        if i['Sender'].endswith(ft.my_emails):
            sent_data.append(i)
            continue
        # If the sender's email includes:
        if i['Sender'].endswith(ft.gaming):
            gaming_data.append(i)
        elif i['Sender'].endswith(ft.finance):
            finance_data.append(i)
        elif i['Sender'].endswith(ft.entertainment):
            entertainment_data.append(i)
        elif i['Sender'].endswith(ft.shopping):
            shopping_data.append(i)
        elif i['Sender'].endswith(ft.social):
            social_data.append(i)
        elif i['Sender'].endswith(ft.government):
            government_data.append(i)
        elif i['Sender'].endswith(ft.cloud):
            cloud_data.append(i)
        elif i['Sender'].endswith(ft.health):
            health_data.append(i)
        elif i['Sender'].endswith(ft.development):
            development_data.append(i)
        elif i['Sender'].endswith(ft.friends_family):
            friends_family_data.append(i)
        elif i['Sender'].endswith(ft.learning):
            learning_data.append(i)
        elif i['Sender'].endswith(ft.service):
            service_data.append(i)
        elif i['Sender'].endswith(ft.product):
            product_data.append(i)
        elif i['Sender'].endswith(ft.business):
            business_data.append(i)
        elif i['Sender'].endswith(ft.provider):
            provider_data.append(i)
        else:
            unsorted_data.append(i)

    sorted_data = {
        'gaming': gaming_data,
        'finance': finance_data,
        'entertainment': entertainment_data,
        'shopping': shopping_data,
        'social': social_data,
        'government': government_data,
        'development': development_data,
        'health': health_data,
        'friends_family': friends_family_data,
        'learning': learning_data,
        'service': service_data,
        'product': product_data,
        'business': business_data,
        'provider': provider_data,
    }
    # Export data to json file.
    json.dump(sorted_data, open("data_output/sorted.json", "w"))
    json.dump(unsorted_data, open("data_output/unsorted.json", "w"))
    json.dump(sent_data, open("data_output/sent.json", "w"))
    # Return sorted data in json format.
    return json.dumps(sorted_data)


def sort_mail_into_labels(json_data):
    pass

#
# Main function
#
def main():
    try:
        all_folders = get_email_folders()
        json_data = extract_email_data(all_folders=all_folders)
    except:
        print('There was a problem getting your email client data. Looking for json file...')
        json_data = search_for_json_file();

    foldered_data = sort_mail_into_folders(json_data=json_data)
    labeled_data = sort_mail_into_labels(json_data=json_data)


# Run the program.
if __name__ == '__main__':
    main()