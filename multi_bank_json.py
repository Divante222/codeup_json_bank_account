import json
import datetime
from fastnumbers import isfloat
import re
def main_menu():
    choice = 'y'
    while choice == 'y':
        user_choice = input('=======================\n'
                            'Enter 1 to view balance\n'
                            'Enter 2 to add money\n'
                            'Enter 3 to withdraw\n'
                            'Enter 4 to add new account\n'
                            'Enter 5 to view transaction_history\n'
                            'Enter 6 to Exit\n'
                            'REMEMBER ENTER YOUR FULL NAME WITH A SPACE IN BETWEEN\n'
                            '=======================\n')
        if user_choice == '1':
            view_balance()
        elif user_choice == '2':
            add_money()
        elif user_choice == '3':
            withdraw_money()
        elif user_choice == '4':
            add_new_account()
        elif user_choice == '5':
            transaction_history()
        elif user_choice == '6':
            break
        
        else:
            print('You did not enter a proper selection')


def view_balance():

    while True:
        with open('my_accounts.txt') as f:
            data = json.load(f)

            search_name = input('Please enter your name or enter "1" to exit: ')
            if search_name.lower() in data[0]:
                print('You have', data[0].get(search_name),'dollars in your account')
                break
            elif search_name == '1':
                break
            else:
                print('Invalid username please try again or enter 1 to exit')


def add_money():
    with open('my_accounts.txt') as f:
        data = json.load(f)
    while True:
        search_name = input('Please enter your name or enter "1" to exit: ')
        if search_name.lower() in data[0]:
            correct_amount = 'n'
            while correct_amount == 'n':

                money_to_add = input('How much money do you wish to add: ')
                if isfloat(money_to_add) and round(float(money_to_add), 2) == float(money_to_add):
                    correct_amount = 'y'
                else:
                    print('You did no input the correct amount please try again')
                
            the_amount_to_append = float(data[0].get(search_name)) + float(money_to_add)
            print('You have', round(the_amount_to_append),'dollars in your account')
            data[0][search_name] = round(the_amount_to_append,2)

            x = '1'
            while x == '1':
                print('Do you want to name this transaction: yes or no')
                custom_identifier_choice = input('')

                if custom_identifier_choice in ['y','yes']:
                    print('input the custom identifying name: ')
                    custom_identifier = input('')

                    while True:
                        print('Is', custom_identifier, 'correct?')
                        confirmation = input('')
                        if confirmation in ['y', 'yes']:
                            x = 1
                            break
                        elif confirmation in ['n', 'no']:
                            break
                        else:
                            print('invalid input')

                elif custom_identifier_choice in ['n', 'no']:
                    custom_identifier = ''
                    break
                else:
                    print('invalid input')


            new_transaction = custom_identifier + ' Deposited ' + str(the_amount_to_append) + ' ' + str(datetime.datetime.now())
            data[1][search_name].append(new_transaction)


            with open('my_accounts.txt','w') as f:
                json.dump(data,f)
            break
        elif search_name == '1':
            break
        else:
            print('Invalid username please try again or enter 1 to exit')

def withdraw_money():
    with open('my_accounts.txt') as f:
        data = json.load(f)
    while True:
        search_name = input('Please enter your name or enter "1" to exit: ')
        if search_name.lower() in data[0]:
            correct_amount = 'n'
            while correct_amount == 'n':

                money_to_add = input('How much money do you wish to withdraw?')
                if isfloat(money_to_add) and round(float(money_to_add), 2) == float(money_to_add):
                    correct_amount = 'y'
                    
                else:
                    print('You did no input the correct amount please try again')
                
            the_amount_to_append = float(data[0].get(search_name)) - float(money_to_add)
            print('You have', round(the_amount_to_append),'dollars in your account')
            data[0][search_name] = round(the_amount_to_append,2)

            x = '1'
            while x == '1':
                print('Do you want to name this transaction: yes or no')
                custom_identifier_choice = input('')

                if custom_identifier_choice in ['y','yes']:
                    print('input the custom identifying name: ')
                    custom_identifier = input('')

                    while True:
                        print('Is', custom_identifier, 'correct?')
                        confirmation = input('')
                        if confirmation in ['y', 'yes']:
                            x = 1
                            break
                        elif confirmation in ['n', 'no']:
                            break
                        else:
                            print('invalid input')

                elif custom_identifier_choice in ['n', 'no']:
                    custom_identifier = ''
                    break
                else:
                    print('invalid input')


            new_transaction = custom_identifier + ' Withdrew ' + str(the_amount_to_append) + ' ' + str(datetime.datetime.now())
            data[1][search_name].append(new_transaction)

            with open('my_accounts.txt','w') as f:
                json.dump(data,f)
            break
        elif search_name == '1':
            break
        else:
            print('Invalid username please try again or enter 1 to exit')


def add_new_account():
    with open('my_accounts.txt') as f:
        data = json.load(f)

        while True:
            new_account_name_first = input('Enter your first name: ')
            new_account_name_last = input('Enter your last name: ')
            full_name = new_account_name_first + ' ' + new_account_name_last
            print('is',full_name,'correct?')

            correctly_entered = input('')
            if correctly_entered in ['yes', 'y']:
                break
            else:
                print('invalid entry please enter "y" or "yes" to verify the information is correct')
        the_list = ["account created"+ ' ' + str(datetime.datetime.now())]
        data[0][full_name] = "0"
        data[1][full_name] = the_list

        with open('my_accounts.txt','w') as d:
            json.dump(data, d)
        

def transaction_history():
    with open('my_accounts.txt') as f:
        data = json.load(f)
    while True:
        search_name = input('Please enter your name or enter "1" to exit: ')
        if search_name.lower() in data[0]:
            while True:
                print('Enter 1 to view all transactions\n'
                      'Enter 2 to view all Deposits\n'
                      'Enter 3 to view all Withdrawls \n'
                      'Enter 4 to use keyword search \n'
                      'Enter 5 to search for a date\n'
                      'Enter 6 to delete a transaction\n'
                      'Enter 7 to go back\n')
                user_input = input('')
                transaction_list = data[1][search_name]
                if user_input == '1':
                    trans_number = 1
                    for i in transaction_list:
                        print('Transaction number ' + str(trans_number) + ' \n' + i + '\n')
                        trans_number += 1
                        
                elif user_input == '2':
                    deposit_list = []
                    for i in transaction_list:
                        if "Deposited" in i:
                            deposit_list.append(i)
                    if len(deposit_list) != 0:
                        for k in deposit_list:
                            print(k)
                    else:
                        print("\nNo transaction history\n")

                elif user_input == '3':
                    deposit_list = []
                    for i in transaction_list:
                        if "Withdrew" in i:
                            deposit_list.append(i)
                    if len(deposit_list) != 0:

                        for k in deposit_list:
                            print(k)
                    else:
                        print("\nNo transaction history\n")
                    
                elif user_input == '4':
                    print('Enter a keyword to search for')
                    the_keyword = input('')
                    deposit_list = []
                    for i in transaction_list:
                        if i.find(the_keyword) == 0:
                            deposit_list.append(i)
                    if len(deposit_list) != 0:
                        for k in deposit_list:
                            print(k)

                    else:
                        print("\nNo transaction history with this keyword\n")

                elif user_input == '5':
                    print('Enter a date in format 9999-99-99')
                    the_keyword = input('')
                    print()
                    deposit_list = []
                    for i in transaction_list:
                        
                        day = re.search('\d{4}-\d{2}-\d{2}', i)
                        date = datetime.datetime.strptime(day.group(), '%Y-%m-%d').date()
                        
                        if str(date) == the_keyword:
                            deposit_list.append(i)
                    if len(deposit_list) != 0:
                        for k in deposit_list:
                            print(k)
                    
                    else:
                        print("\nNo transaction history with this date\n")
                    print()

                elif user_input == '6':
                    while True:
                        print('Enter the transaction number you wish to delete')
                        print()
                        
                        count = 0
                        for i in transaction_list:   
                                        
                            count += 1
                            print('Transaction number ' + str(count) + ' \n' + i + '\n')
                        print('Enter transaction keyword or number')

                        the_keyword = input('')
                        print('Is', the_keyword, 'correct: ')
                        is_correct = input('')
                        if is_correct in ['y','yes']:
                            break
                        elif is_correct in ['n','no']:
                            continue
                        else:
                            print('incorrect selection')
                    if the_keyword.isdigit():
                        if the_keyword != '1':
                            with open('my_accounts.txt') as f:
                                data = json.load(f)
                                data[1][search_name].pop(int(the_keyword) - 1)

                                with open('my_accounts.txt','w') as f:
                                    json.dump(data,f)    
                                    print('transaction deleted')
                                   
                        else: 
                            print('You can not delete the first transaction')
                    else: 
                        index_number = 0
                        for i in data[1][search_name]:
                            if the_keyword in i:
                                with open('my_accounts.txt') as f:
                                    data = json.load(f)
                                    data[1][search_name].pop(index_number)

                                with open('my_accounts.txt','w') as f:
                                    json.dump(data,f)    
                                    print('transaction deleted')
                            index_number+=1
                            
                    
                    
                                
                elif user_input == '7':
                    break


        elif search_name == '1':
            break
        else:
            print('Invalid entry')


main_menu()