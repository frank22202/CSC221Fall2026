import demo801

demo801.main()

def menu():
    option = int(input('Enter 1 for update: \n'
                       'Enter 2 for insert: \n'
                       'Enter 3 for exit: '))
    return option

def main():
    option = menu()
    if option == 1:
        print('you choose 1')
    elif option ==2:
        print('you choose 2')
    else:
        exit(0)

if __name__ == '__main__':
    main()