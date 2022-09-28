# email-search-and-organizer
Python application to search and organize your emails.

## Running the program
Create a .env file in the program's directory.

You'll need to insert:
```EMAIL_ADDRESS = "<your_email_address>"```
Where 'your_email_address' is the root folder of your outlook email directory.

Alternatively,

You can forgo the email client, and use an already exist json file formatted as such:

```
[
    {
        "Name": "GitHub",
        "Sender": "noreply@github.com",
        "Recipients": "['first@email.com','second@email.com']",
        "Date": "2022-02-12 12:33:14+00:00",
        "Subject": "[GitHub] A third-party OAuth application has been added to your account"
    },
    ...
    {
        "Name": "Microsoft account team",
        "Sender": "account-security-noreply@accountprotection.microsoft.com",
        "Recipients": "['only@email.com']",
        "Date": "2022-07-23 14:56:16+00:00",
        "Subject": "New app(s) connected to your Microsoft account"
    }
]
```