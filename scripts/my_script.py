"""Script to prompt user for story choice and print the final story."""

# This adds the directory above to our Python path
#   This is so that we can add import our custom python module code into this script
import sys
sys.path.append('../')

# Imports
from my_module.functions import tell_story

# Intro blurb and prompt user for story choice
print('Welcome to Mad Libs!')
story = input('What story would you like?\nYour options are: An Awkward '\
    'Encounter (1), How to Cross a Piranha Infested River (2), The\nPower'\
    ' of the Force (3), Vacations (4), and Lucy in the Sky with Diamonds (5).\n')

# Tell story chosen by user
while story.lower() != 'quit':
    if story.lower() == 'an awkward encounter' or story == '1':
        print(tell_story('awkward'))
    elif story.lower() == 'how to cross a piranha infested river' or story == '2':
        print(tell_story('piranha'))
    elif story.lower() == 'the power of the force' or story == '3':
        print(tell_story('force'))
    elif story.lower() == 'vacations' or story == '4':
        print(tell_story('vacation'))
    elif story.lower() == 'lucy in the sky with diamonds' or story == '5':
        print(tell_story('lucy'))
    elif story == 'test':
        print(tell_story('test'))
    # Input not recognized
    else:
        story = input('Please make sure your choice is one of the options:'\
        ' An Awkward Encounter (1), How to\nCross a Piranha Infested River (2)'\
        ', The Power of the Force (3), Vacations (4), and Lucy\nin the Sky with'\
        ' Diamonds (5).\n')
        continue

    # Continue by choosing a story or exit with 'No'
    story = input('If you would you like to try another mad lib, enter'\
        ' your story choice.\nYour options are: An Awkward Encounter (1), How'\
        ' to Cross a Piranha Infested River (2), The\nPower of the Force'\
        ' (3), Vacations (4), and Lucy in the Sky with Diamonds (5).\nIf not,'\
        ' enter \'quit\'.\n')

# Outro blurb
print('Thanks for playing Mad Libs!\n')
