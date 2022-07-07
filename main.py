from blessed import Terminal
import os # To get OS and clear terminal output
import pyperclip # Copy the hiragana to clipboard
import sys # Flush the terminal output to screen

# Converts a toki ponan syllable to hiragana-equivalent (ish) characters
def tpToHiragana(syllable):
    characters = ''

    # Syllable without ending nasal letter 'n' (if it exists)
    noNasal = syllable
    if len(syllable) > 1:
        if syllable[len(syllable)-1] == 'n': noNasal = syllable[:len(syllable)-1]

    if noNasal in latin:
        characters = '{}{}'.format(characters, hiragana[latin.index(noNasal)])
        # Adds the character for 'n' if it was at the end of the syllable
        if len(syllable) > 1:
            if syllable[len(syllable)-1] == 'n': characters = '{}{}'.format(characters, hiragana[latin.index('n')])
    else:
        characters = '? '
    return characters

# Clears the terminal output depending on the OS
def clear():
    if sys.platform.startswith('win32'):
        os.system('cls')
    elif sys.platform.startswith('darwin'):
        os.system('clear')
    elif sys.platform.startswith('linux'):
        os.system('clear')


# Two lists of corresponding hiragana and latin characters
hiragana = ['ん','あ','え','い','お','う','や','いぇ','よ','ゆ','か','け','き','こ','く','ら','れ','り','ろ','る','ま','め','み','も','む','な','ね','に','の','ぬ','ぱ','ぺ','ぴ','ぽ','ぷ','さ','せ','し','そ','す','た','て','と','つ','わ','ゑ','ゐ']
latin = ['n','a','e','i','o','u','ja','je','jo','ju','ka','ke','ki','ko','ku','la','le','li','lo','lu','ma','me','mi','mo','mu','na','ne','ni','no','nu','pa','pe','pi','po','pu','sa','se','si','so','su','ta','te','to','tu','wa','we','wi']

term = Terminal()
clear()

inputChars = ''
while True:
    clipboard = ''

    # Gets the character inputted
    with term.cbreak(): newChar = term.inkey()
    # If backscpace key is pressed, it removes a character from tp
    if newChar == '\x7f' and len(newChar) > 0:
        inputChars = inputChars[:len(inputChars)-1]
    elif newChar == '\x1b':
        break
    else:
        inputChars = '{}{}'.format(inputChars, newChar)

    clear()

    # Prints user's input
    print(inputChars)

    # Splits the user's input into individual syllables
    inputSyllables = inputChars.split(' ')
    for s in inputSyllables:
        if s != '':
            out = tpToHiragana(s)
            print(out,end=' ')
            clipboard = '{}{} '.format(clipboard, out)
    print('')

    # Flushes the terminal output to screen
    sys.stdout.flush()
    # Copies the hiragana to clipboard
    pyperclip.copy(clipboard)