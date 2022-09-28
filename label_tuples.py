from email.errors import InvalidMultipartContentTransferEncodingDefect


def get_email_list(filename):
    with open("email_lists/labels/"+ filename) as email_list:
        return email_list.read().splitlines()


banking = (
    'business@email.com',
) + tuple(get_email_list('banking.txt'))

cloud = (
    'cloud@email.com',
) + tuple(get_email_list('cloud.txt'))

crypto = (
    'crypto@email.com',
) + tuple(get_email_list('crypto.txt'))

design = (
    'design@email.com',
) + tuple(get_email_list('design.txt'))

development = (
    'development@email.com',
) + tuple(get_email_list('development.txt'))

etransfer = (
    'etransfer@email.com',
) + tuple(get_email_list('etransfer.txt'))

investing = (
    'investing@email.com',
) + tuple(get_email_list('investing.txt'))

security = (
    'security@email.com',
) + tuple(get_email_list('security.txt'))