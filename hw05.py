"""
Name: Linda Zhang
Peers: Worked independently
References: Lecture 14, Google search to understand assertion errors
"""

def get_letter():
    """ This function needs no input parameters but it returns a single character A, B, or C """
    # remove the default return and add your code
    while True:
        letter = input("Give an single uppercase letter: ")
        if len(letter) != 1:
            print("Error: it needs to be a single character.")
            continue
        if letter not in ["A", "B", "C"]:
            print("Error: You provided the wrong character.")
            continue
        return letter
    ""
# Use continue keyword to restart the loop
# != means "doesn't equal"

def get_digit():
    """ This function needs no input parameters but it returns a single digit character in the range [1,3] """
    # remove the default return and add your code
    while True:
        digit = input("Give an single number character: ")
        if not digit.isdigit():
            print("Error: your input should be only digits.")
            continue
            
        if digit not in ["1", "2", "3"]:
            print("Error: a single digit needs to be in [1,3].")
            continue
            
        return digit
    0
# Use "isdigit()" to check if a string character is a digit

def check_pattern(letter, digit, lst):
    """ This function checks if any of the words inside st_list contain the letter character and digit character (in that order) """
    # remove the default pass and add your code
    print("Strings with the pattern:")
    printed_words = set()

    for word in lst:
        idx_letter = word.find(letter)
        if idx_letter != -1:
            idx_digit = word.find(digit, idx_letter + 1)
            if idx_digit != -1 and word not in printed_words:
                print(word, end=" ")
                printed_words.add(word)

    print()
    
# Unlike a list, a set has no guaranteed order
# word.find(letter) locates the position of the first occurrence of a letter character
# word.find(digit, idx_letter + 1) searches for the digit character, ignoring any characters at or before word.find(letter)


#  The function main is INCOMPLETE, you must finish it
# before you submit
def main ():
    """ gets a letter-num pair and searches inside a list for matches"""

    # The list inside of which we will search the user pair (DO NOT MODIFY)
    # -------------------------------------------------
    st_list = ["@C@2", "@2B", "A3", "C2C2", "AA@1", "@B@33",
    "B@2@", "@@C1", "1B@", "A@@2", "@A3@", "@1@A", "2AA@",
    "1B1B", "333B", "1@CC", "3@@C", "333C"]

    # TODO: Add your calls to get_letter, get_digit, and check_pattern
    # Inside a loop so that:
    #     After printing the results, a prompt appears requiring an input
    #          with the text: "Try Again? (y/n): "
    #     AND
    #          IF the user replies with 'y', the loop continues
    #          IF the user replies with anything else, the loop ends
    # ADD YOUR CODE UNDER THIS LINE
    # -------------------------------------------------

    while True:
        letter = get_letter()
        digit = get_digit()
        check_pattern(letter, digit, st_list)
        user_choice = input("Try Again? (y/n): ")
        if user_choice != 'y':
            break
 # Ends if user_choice is 'n'       

    # -------------------------------------------------
    # No need to modify anything Below this line
    print("The End")
    

# Do not modify these two lines
if __name__ == "__main__":
    main()