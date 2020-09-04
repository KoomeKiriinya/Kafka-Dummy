from random import choices, randint
from string import ascii_letters,digits

account_chars=digits+ ascii_letters

def _random_account_id():
    """ return a random number made of 12 characters """
    return "".join(choices(account_chars,k=12))
def _random_amount():
    """ return a random number between 1.00 and 1000.00"""
    return randint(100,1000000)/100
def _create_random_transaction():
    """ create a fake randomised transaction """
    return {
        "source":_random_account_id(),
        "target":_random_account_id(),
        "amount":_random_amount(),
        "currency":"EUR"
    }


