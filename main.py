print("Hi, this is Victor's text to morse code converter.\n")

valid_chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
               'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '.', ',', '?',
               "'", '!', '/', '(', ')', '&', ':', ';', '=', '+', '-', '_', '"',
               '$', '@', ' ']

converted_chars = ['. _', '_ . . .', '_ . _ .', '_ . .', '.', '. . _ .', '_ _ .',
                   '. . . .', '. .', '. _ _ _', '_ . _', '. _ . .', '_ _', '_ .',
                   '_ _ _', '. _ _ .', '_ _ . _', '. _ .', '. . .', '_', '. . _',
                   '. . . _', '. _ _', '_ . . _', '_ . _ _', '_ _ . .', '_ _ _ _ _',
                   '. _ _ _ _', '. . _ _ _', '. . . _ _', '. . . . _', '. . . . .',
                   '_ . . . .', '_ _ . . .', '_ _ _ . .', '_ _ _ _ .', '. _ . _ . _',
                   '_ _ . . _ _', '. . _ _ . .' '. _ _ _ _ .', '_ . _ . _ _', '_ . . _ .',
                   '_ . _ _ .', '_ . _ _ . _', '. _ . . .', '_ _ _ . . .', '_ . _ . _ .',
                   '_ . . . _', '. _ . _ .', '_ . . . . _', '. . _ _ . _', '. . _ _ . _',
                   '. _ . . _ .', '. . . _ . . _', '. _ _ . _ .', '       ']


def retry():
    new_msg = input('Would you like to convert another message? Type "yes" or "no"\n').lower()
    if new_msg == 'yes':
        convert_message()
    else:
        print("Thank you for using Victor's text to morse code converter.\nHave a great day!")


def convert_message():
    original_message = input('Please enter your message (use english characters only):\n').lower()
    if original_message == "":
        print('No message was entered')
        convert_message()
    else:
        message_in_morse = []
        invalid_chars = []
        for char in original_message:
            if char not in valid_chars:
                invalid_chars.append(char)
            # finds the index of the original character in valid_chars:
            else:
                i = valid_chars.index(char)
                # retrieves the morse code attributed to the character using the same index and adds three spaces
                # between them, per convention
                message_in_morse += converted_chars[i] + "   "
        if invalid_chars:
            print(f'Your message was not converted because it contains the following '
                  f'unsupported characters: {invalid_chars}\n')
            retry()
        else:
            print('Message converted successfully, here it goes:')
            # converts the result, which is a list, into a string:
            print("".join(message_in_morse))
            retry()


convert_message()
