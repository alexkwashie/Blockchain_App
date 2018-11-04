#create  a Genesis block to start the blockchain
genesis_block = {
    'previous_hash': '',
    'index' : 0,
    'Transactions' : []
}

blockchain = [genesis_block]
open_transactions = []
owner = 'alex'

def get_blockchain_amount():
    """Returns last value in blockchain array"""
    if len(blockchain) <  1:
        return None
    return blockchain[-1]


def add_val(recipient, sender = owner, amount = 1.0):
    """Append a new value as well the last value in the blockchain

    Arguments:
        :send : The sender of the coins
        : recipient: The receiver of the coins
        : Amount: The amount of coins sent in the trasaction (def: 1.0)
    """
    transaction = {
        'sender': sender,
        'recipient': recipient,
        'amount': amount
    }
    open_transactions.append(transaction)


def mine_block():
    last_block = blockchain[-1]
    hashed_block = ' '
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block + str(value)

    block = {
        'previous_hash': hashed_block,
        'index' : len(blockchain),
        'Transactions': open_transactions
    }
    blockchain.append(block)


def get_transaction_val():
    #fetch the receipt info
    tx_recipient = input('Enter the recipient  of the transaction: ')
    tx_amount = input('What is your transaction amount: ')
    return (tx_recipient, tx_amount) #return a tuple i.e. values that can not be changed

def get_user_choice():
    user_input = input('Your Choice: ')
    return user_input

def print_blockchain_element():
    #Outputting the list in the blockchain
    for block in blockchain:
        print('Outputting block')
        print(block)
    else:
        print('-' * 30) #print '-' 30 times ------

#How to verify the block:  i.e. so you can not amend previous block
def verify_chain():
    block_index = 0 #2
    is_valid = True
    for block in blockchain: #1
        if block_index == 0:
            block_index += 1
            continue # use continue to carry on through the code below: its best used after an 'IF statement' with no 'else'
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid #always return the boolean

#create a variable to hold True or false value
waiting_input = True
#Create a while loop to ask for user input
while waiting_input:
    print('Please choose option')
    print('1: Add transaction value')
    print('h: Manipulate the blockchain')
    print('2: Output Block chain blocks')
    print('3: Mine new blockchain')
    print('q: Quit')

    #put get_user_choice() input in  a variable
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_val()
        recipient, amount = tx_data
        #Add the transaction to the blockchain
        add_val(recipient, amount = amount)
        print(open_transactions)
    elif user_choice == '3':
        mine_block()
    elif user_choice == '2' and len(blockchain) < 1:
        print('Blockchain is empty, enter valid amount')
    elif user_choice == '2':
        print_blockchain_element()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = [2]
    elif user_choice == "q":
        #break
        waiting_input = False
    else:
        print('Input was invalid, please choose number from list')
    print('Choice Registered')

#     if not verify_chain():
#         print('Invalid Blockchain!')
#         break
# else:
#     print('User Left!')

print('Done!')
