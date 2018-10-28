blockchain = []


def get_last_amount():
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


def get_user_input():
    return input('What is your transaction amount: ')


tx_amount = get_user_input()
add_val(tx_amount)
#add_val(get_last_amount(), 9.2)


#Creat a while loo to ask for user input
while True:
    tx_amount = get_user_input()
    add_val(tx_amount, get_last_amount())

    #Outputting the list in the blockchain
    for block in blockchain:
        print('Outputting block')
        print(block)

print('Done!')
