def get_email_list(filename):
    with open("email_lists/labels/"+ filename) as email_list:
        return email_list.read().splitlines()


banking = (
    'business@email.com',
) + tuple(get_email_list('banking.txt'))

cloud = (
    'cloud@email.com',
) + tuple(get_email_list('cloud.txt'))