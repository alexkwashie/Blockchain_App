blockchain = []

def get_last_amount():
    return blockchain[-1]
# '-1' used to select last element in an array

def add_val(val, last_num = 1):
    blockchain.append([last_num, val]) #2 !important - last_num is set to defult [1]

def get_user_input():
    return  input('What is your transaction amount: ')


tx_amount = get_user_input()
add_val(tx_amount)

#add_val(get_last_amount(), 9.2)

tx_amount = get_user_input()
add_val(last_num=get_last_amount(), val = tx_amount)

tx_amount = get_user_input()
add_val(tx_amount, get_last_amount())


print(blockchain)