import os

def check_file():
    # Prompt the user for a valid file name until it exists.
    exit = 12
    while exit != 10:
        filename = input('Enter the name of the headline file you want to analyze:')
        if os.path.isfile(filename):
            return filename
            exit = 10
        else:
            print('Error: File does not exist. Please try again.')

def read_file(filename):
    # Read the file into a list of strings
    file_lines = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                file_lines.append(line.strip())
    except:
        print('Error reading file')
    return file_lines

def menu():
    # Display the menu and get a valid input from the user
    menu_display = [
        '1. Determine how many headlines have a particular word.',
        '2. Write headlines containing a specific word to a new file.',
        '3. Determine the average number of characters per headline.',
        '4. Output the longest and shortest headline.',
        '5. Read in a new file to analyze.',
        '6. Quit.'
    ]
    print('Menu \n')
    for i in menu_display:
        print(i)

    exit = 0
    while exit != 1:
        try:
            user_choice = int(input('Enter your choice (1-6): '))
            if 1 <= user_choice <= 6:
                return user_choice
                exit = 1
            else:
                print('Invalid choice. Please enter a number between 1 and 6.')
        except:
            print('Invalid input. Please enter a number between 1 and 6.')

def count_word_in_headlines(headlines, word):
    # Count headlines containing a specific word.
    count = 0
    for headline in headlines:
        if word.lower() in headline.lower():
            count += 1
    return count
    
def write_headlines(headlines, word, output_filename):
    # Write headlines containing a specific word to a new file
    with open(output_filename, 'w') as file:
        for headline in headlines:
            if word.lower() in headline.lower():
                file.write(headline + '\n')

def average_headline_characters(headlines):
    # Calculate the average number of characters per headline
    total_characters = 0
    headlines_count = 0
    for headline in headlines:
        total_characters += len(headline)
        headlines_count += 1
    if total_characters != 0:
        average_characters = total_characters / headlines_count
    return average_characters

def find_max_and_min_headlines(headlines):
    # Find the longest and shortest headlines by character length
    if len(headlines) >= 0:
        max_headline = headlines[0]
        min_headline = headlines[0]
        for headline in headlines:
            if len(headline) > len(max_headline):
                max_headline = headline
            if len(headline) < len(min_headline):
                min_headline = headline
        return max_headline, min_headline
    else:
        print('Nothing is available to check. Please try again')
        
def main():
    print('Welcome to the ABC Headline Analyzer!')
    print('This program allows you to analyze headlines from a file.')
    print('Choose from the available options to perform different analyses.')

    file_name = check_file()
    headlines = read_file(file_name)
    
    exit = 0
    while exit == 0:
        choice = menu()

        if choice == 1:
            word = input('Enter the word you want to search for: ')
            count = count_word_in_headlines(headlines, word)
            print('There are', count, 'headlines containing the word', word,'.')

        elif choice == 2:
            word = input('Enter the word to search for: ')
            output_filename = input('Enter the name of the output file: ')
            write_headlines(headlines, word, output_filename)
            print('Headlines containing the word', word, 'have been written to', output_filename,'.')

        elif choice == 3:
            average = average_headline_characters(headlines)
            print(f'The average number of characters per headline is {average:.2f}.')

        elif choice == 4:
            max_min = find_max_and_min_headlines(headlines)
            print('Longest headline is', max_min[0])
            print('Shortest headline is', max_min[1])

        elif choice == 5:
            file_name = check_file()
            headlines = read_file(file_name)
            print('New file has been updated.')

        elif choice == 6:
            print('Thank you for using my program!')
            exit = 1


main()
    
