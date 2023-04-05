#
#   PROJECT : Email Spam Filtering
# 
#   FILENAME : main.py
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

from email_data import EmailData
from email_ml import EmailMachineLearning

#
# NOTE: 
#
def main():
    ed = EmailData()

    filename = 'test.json'
    ed.send_mail(filename=filename)
    messages = ed.fetch_all_mail()
    filename = 'messages.json'
    ed.save_mail_to_json(messages=messages, location=filename)

    eml = EmailMachineLearning()
    eml.json_to_csv(filename=filename, training=True)

# Run the program.
if __name__ == '__main__':
    main()