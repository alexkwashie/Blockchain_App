blockchain = []


def get_blockchain_amount():
    """Returns last value in blockchain array"""
    return blockchain[-1]


def add_val(val, last_num=1):
    """Append a new value as well the last value in the blockchain

    Arguments:
        :val : Is the value that must be manually added
        : last_num: is the last amount in the blockchain  (defults to '1') to get it started
    """
    blockchain.append(
        [last_num, val])  # 2 !important - last_num is set to defult [1]


def get_transaction_val():
    return input('What is your transaction amount: ')

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input

def print_blockchain_element():
    #Outputting the list in the blockchain
    for block in blockchain:
        print('Outputting block')
        print(block)

tx_amount = get_transaction_val()
add_val(tx_amount)

#Creat a while loo to ask for user input
while True:
    print('Please choose option')
    print('1: Add transaction value')
    print('2: Output Block chain blocks')
    #put get_user_choice() input in  a variable
    user_choice = get_user_choice()
    if user_choice == 1:
        tx_amount = get_transaction_val()
        add_val(tx_amount, get_blockchain_amount())
    else:
        print_blockchain_element()
    break
print('Done!')
