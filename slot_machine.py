import random

MIN_LINES = 1
MAX_LINES = 3
MIN_BET = 1
MAX_BET = 100
ROWS = 3
COLS = 3

dict_symbols = {
    'A' : 2,
    'B' : 3,
    'C' : 5,
    'D' : 4
}

symbol_values = {
    'A' : 5,
    'B' : 4,
    'C' : 3,
    'D' : 2
}

def converting_to_symbol_list(symbols):
    symbol_list = []
    for symbol,value in symbols.items():
        for i in range(value):
            symbol_list.append(symbol)
    return symbol_list

symbol_list = converting_to_symbol_list(dict_symbols)

def deposit():
    while True:
        amount = input("How much amount do you want to deposit? ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter valid input.")
    return amount
    
def get_num_of_lines_to_bet():
    while True:
        lines = input(f"How many Lines you want to bet between min line = {MIN_LINES} and max line = {MAX_LINES}? ")
        if lines.isdigit():
            lines = int(lines)
            if MIN_LINES <= lines <= MAX_LINES:
                break
            else:
                print("Enter valid input.")
        else:
            print("Enter valid input.")
    return lines

def bet_on_each_line():
    while True:
        amount = input(f"How much amount do you want to bet on each line, min bet = {MIN_BET} and max bet = {MAX_BET}? ")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter valid input.")
    return amount

def get_slot_machine_spin(rows,cols,symbols):
    systematic_symbols = [[] for i in range(rows)]

    temp_symbol_list = symbol_list.copy()
    for row in range(rows):
        for col in range(cols):
            random_symbol = random.choice(temp_symbol_list)
            systematic_symbols[row].append(random_symbol)
            temp_symbol_list.remove(random_symbol)

    return systematic_symbols,temp_symbol_list

chose_symbols,temp_symbols = get_slot_machine_spin(ROWS,COLS,symbol_list)

def printing_chose_symbols_transversely(symbols):
    # print((symbols[0][0]))
    for col in range(len(symbols[0])):
        for row in range(len(symbols)):
            if row==len(symbols)-1:
                print(symbols[row][col],end=" ")
            else:
                print(symbols[row][col],"|",end=" ")
        print()
            
def checking_match(symbols):
    line = []
    num = 0
    matched_symbols = []
    for col in range(len(symbols[0])):
        count = 0
        for row in range(len(symbols)):
            if symbols[0][col]==symbols[row][col]:
                count+=1
            else:
                break
        if count==len(symbols):
            line.append(col+1)
            num+=1
            matched_symbol.append(symbols[0][col])
    return num,line,matched_symbols

num,line,matched_symbol = checking_match(chose_symbols)

def calcuating_total_reward(matched_symbol,bet,symbol_value):
    reward = 0
    for symbol in matched_symbol:
        reward += symbol_value(symbol)*bet
    return reward

def game(balance):
    lines = get_num_of_lines_to_bet()
    while True:
        bet = bet_on_each_line()
        betted_amount = lines*bet
        if betted_amount>balance:
            print("You don't have enough balance.")
        else:
            break
    # print(converting_to_symbol_list(dict_symbols))
    # print(chose_symbols)
    printing_chose_symbols_transversely(chose_symbols)
    # print(f"{checking_rewards(chose_symbols)} line matched")
    if num>0:
        print(f"{num} lines matched at {line}")
    else:
        print("No line matched")
    reward = calcuating_total_reward(matched_symbol,bet,symbol_values)
    remaining_balance = balance-betted_amount+reward
    if reward>0:
        print(reward)
    print(f"Your total balance is : {remaining_balance}")
    return remaining_balance

def main():
    balance = deposit()
    while True:
        start = input("Enter 1 to Start And 0 to Stop the Game : ")
        if start.isdigit():
            start = int(start)
            if start==1:
                balance = game(balance)
                if temp_symbols==[]:
                    print("Game Over.")
            elif start==0:
                print(f"Your final balance : {balance}")
                break
            else:
                print("Enter valid input.")
        else:
            print("Enter valid input.")
        
main()
