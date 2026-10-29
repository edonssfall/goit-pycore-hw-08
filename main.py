import sys

from colorama import Fore, init

from bot import Bot
from utils import load_data, save_data


def main():
    """
    chatbot entry point: load the address book from the file, run the request-response loop
    (also catches errors outside handlers: empty input, exit, EOF) and save the book on any exit
    """
    print("Welcome to the assistant bot!")
    bot = Bot(book=load_data())
    try:
        while True:
            try:
                user_input = input("Enter a command: ")
                print(bot(user_input))
            except EOFError:
                print('\nGood bye!')
                sys.exit()
            except Exception as e:
                print(Fore.RED + f'Error: {e}')
    finally:
        save_data(book=bot.book)


if __name__ == '__main__':
    init(autoreset=True)
    main()
