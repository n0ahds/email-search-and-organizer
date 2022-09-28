def get_email_list(filename):
    with open("email_lists/folders/"+ filename) as email_list:
        return email_list.read().splitlines()


business = (
    'business@email.com',
) + tuple(get_email_list('business.txt'))

entertainment = (
    'entertainment@email.com',
) + tuple(get_email_list('entertainment.txt'))

finance = (
    'finance@email.com',
) + tuple(get_email_list('finance.txt'))

friends_family = (
    'friends_family@email.com',
) + tuple(get_email_list('friends_family.txt'))

gaming = (
    'gaming@email.com',
) + tuple(get_email_list('gaming.txt'))

government = (
    'government@email.com',
) + tuple(get_email_list('government.txt'))

health = (
    'health@email.com',
) + tuple(get_email_list('health.txt'))

learning = (
    'learning@email.com',
) + tuple(get_email_list('learning.txt'))

my_emails = (
    'my@email.com',
) + tuple(get_email_list('my_emails.txt'))

product = (
    'product@email.com',
) + tuple(get_email_list('product.txt'))

provider = (
    'provider@email.com',
) + tuple(get_email_list('provider.txt'))

service = (
    'service@email.com',
) + tuple(get_email_list('service.txt'))

shopping = (
    'shopping@email.com',
) + tuple(get_email_list('shopping.txt'))

social = (
    'social@email.com',
) + tuple(get_email_list('social.txt'))