blockchain = []

def get_last_amount():
    return blockchain[-1]
# '-1' used to select last element in an array

def add_val(val, last_num = 1):
    blockchain.append([last_num, val])


add_val(10)
add_val(1.9, get_last_amount())
add_val(6.8,get_last_amount())


print(blockchain)