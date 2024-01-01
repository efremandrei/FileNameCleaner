import os
import datetime
import myConstants

words_to_remove = myConstants.WORDS_TO_REMOVE
path_to_process = myConstants.PATH_TO_PROCESS

def create_log_file():
    """

    :return:
    """
    # Get current date and time
    current_datetime = datetime.datetime.now()
    log_file_name = current_datetime.strftime("%Y-%m-%d_%H-%M-%S") + "_log.txt"

    # Create log file
    with open(log_file_name, 'w') as log_file:
        log_file.write(f"{current_datetime} - Log file created\n")

    return log_file_name


def add_log_entry(log_file_name, entry):
    """

    :param log_file_name:
    :param entry:
    :return:
    """
    # Append entry to the log file
    with open(log_file_name, 'a') as log_file:
        try:
            log_file.write(entry + '\n')
        except UnicodeEncodeError:
            print("Encountered a character that can't be saved into the log file - log entry will be skipped.")
            # Skip entry that cannot be encoded
            pass


# print("pre-def print!")
def remove_words_from_path(path, words_to_remove):
    """

    :param path:
    :param words_to_remove:
    :return:
    """
    # Iterate over all items in the current directory
    for item in os.listdir(path):
        # print(f'the item we are working on is: {item}')
        item_path = os.path.join(path, item)
        # print(f'the item_path we are working on is: {item_path}')

        # If it's a directory, recursively call the function
        if os.path.isdir(item_path):
            # print(f'the item_path: {item_path} is a FOLDER!')
            remove_words_from_path(item_path, words_to_remove)

        # Remove specified words from the item's name
        new_name = item
        for word in words_to_remove:
            # print(f'checking if the word: {word} is in {new_name}')
            new_name = new_name.replace(word, '')
        # print(f'the new_name is: {new_name}')

        # Rename the item if necessary
        if new_name != item:
            # print(f'it would appear that new_name: {new_name} is not the same as item: {item}')

            new_path = os.path.join(path, new_name)
            # print(f'new_path: {new_path} is made of: {path} and {new_name}')

            os.rename(item_path, new_path)
            msg = f'Renamed: {item_path}  To:  {new_path}'
            print(msg)
            entry = f"{datetime.datetime.now()} - {msg}"
            add_log_entry(log_file_name, entry)


if __name__ == '__main__':
    while True:
        userChoise = input(f'What would you like to do:\n'
                           f'1. Run auto-cleanup of {path_to_process}\n'
                           f'2. Run auto-cleanup of another folder?\n'
                           f'3. How many values in the search list?\n'
                           f'4. How many unique values in the search list?\n'
                           f'5. Exit\n'
                           )
        # print("pre-run print")
        if userChoise == '5':
            break
        elif userChoise == '4':
            print(f'The total amount of unique values in the search list is: {len(set(words_to_remove))}')
            pass
        elif userChoise == '3':
            print(f'The total amount of values in the search list is: {len(words_to_remove)}')
            pass
        elif userChoise == '2':
            path_to_process = input("What is the full folder path you wish to run auto-clean on?\n")
        elif userChoise == '1':
            pass
        log_file_name = create_log_file()
        remove_words_from_path(path_to_process, words_to_remove)
        print("Finished running DUDE!")