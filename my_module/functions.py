"""A function for creating a story."""

# Story templates
# Source: https://www.pinterest.com/pin/510595676490471936/?lp=true
awkward = 'After [verb ending in \'ing\'] shotguns at the range, drinking '\
    '[type of liquid] by the pool, and a big [type of food] dinner, this is '\
    'turning out to be a/an [adjective] night. I\'m at some bar called the '\
    '[noun] Lounge, and I am [adverb] smashed right now. We have [noun] '\
    'service in a/an [adjective] VIP area, but there are no girls here. Well, '\
    'I\'m the groom, so I think I\'ll go [verb] some up. I can\'t [adverb] '\
    'see anything with all the flashing [plural noun] in this club, but I '\
    'think there\'s a group of [plural noun] in that corner. Hmmm... there\'s '\
    'a brunette over there... I can\'t see her face, but boy does she have a '\
    'great [part of the body]. I\'ll ask her if she and her friends want to '\
    'join us for a round of [plural noun]. \"Excuse me, but we have '\
    '[adjective] booze and no one to share it with. Want to join us?\" I say. '\
    'She turns around and smiles at me. \"Yes, [male name], we\'d love to '\
    'join you.\" She says. [exclamation]! I must be the only groom in the '\
    '(the) [place] to hit on his own fiancee during his bachelor party.\n'

# Source: https://www.pinterest.com/pin/524036106631978610/
force = 'The Force is a mystical, [adjective] power. As Jedi Master Obi-Wan '\
    'Kenobi once said, \"The Force is an energy field, created by all living '\
    '[plural noun] that surrounds us, penetrates us, and binds the [noun] '\
    'together.\" Using the power of the Force, a Jedi can do many [adjective] '\
    'things, like using the Force to exercise [part of the body] control '\
    'over [adjective]-minded [plural noun]. A Jedi can also use the Force to '\
    'move objects with his or her [part of the body]. It doesn\'t matter how '\
    '[adjective] these objects are; it only matters how [adverb] the Jedi '\
    'believes in the Force. Most importantly, the Force teaches a Jedi to '\
    'rely on his or her feelings. As Obi-Wan Kenobi told his student, Luke '\
    '[noun].\n'

# Source: https://www.pinterest.com/pin/131800726577837614/?lp=true
piranha = 'If you are traveling in [foreign country] and find yourself '\
    'having to cross a\npiranha-filled river, here\'s how to do it [adverb]:\n'\
    '- Piranhas are more [adjective] during the day, so cross the river at'\
    ' night.\n- Avoid areas with netted [animal] traps--piranhas may be'\
    ' [verb ending in \'ing\'] there\n  looking to [verb] them!\n- When [verb'\
    ' ending in \'ing\'] the river, swim [adverb]. You don\'t want to wake them'\
    '\n  up and make them [adjective]!\n- Whatever you do, if you have an open'\
    ' wound, try to find another way\n  to get back to the [place]. Piranhas are'\
    ' attracted to fresh [type of liquid]\n  and will most likely take a bite out'\
    ' of your [part of body] if you [verb] in the\n  water!\n'

# Source: http://www.madlibs.com/
vacation = 'A vacation is when you take a trip to some [adjective] place with'\
    ' your [adjective] family. Usually you go to some place that is near a/an'\
    ' [noun] or up on a/an [noun]. A good vacation place is one where you can'\
    ' ride [plural noun] or play [game] or go hunting for [plural noun]. I'\
    ' like to spend my time [verb ending in \'ing\'] or [verb ending in'\
    ' \'ing\']. When parents go on a vacation, they spend their time eating'\
    ' three [plural noun] a day, and fathers play golf, and mothers sit '\
    'around [verb ending in \'ing\']. Last summer, my little brother fell in '\
    'a/an [noun] and got poison [plant] all over his [part of the body]. My '\
    'family is going to go to (the) [place], and I will practice [verb ending '\
    'in \'ing\']. Parents need vacations more than kids because parents are '\
    'always very [adjective] and because they have to work [number] hours '\
    'every day all year making enough [plural noun] to pay for the vacation.\n'

# Source: https://www.madtakes.com/libs/173.html
lucy = 'Picture yourself in a [noun] on a river,\nWith [food] trees and [food]'\
    ' skies\nSomebody calls you, you [verb] quite [adverb],\nA girl with'\
    ' [adjective] eyes.\nCellophane [plural noun] of [color] and green,\n'\
    '[verb] over your head.\n[verb] for the girl with the [noun] in her eyes,\n'\
    'And she`s gone.\n[female name] in the sky with [plural noun]...\n'\
    '[female name] in the sky with [plural noun]...\n[female name] in the sky'\
    ' with [plural noun]...\nFollow her down to a [noun] by a fountain\nWhere'\
    ' rocking horse [plural noun] eat [noun] pies,\nEveryone [verb ending in'\
    ' \'s\'] as you [verb] past the flowers,\nThat [verb] so incredibly high.\n'\
    'Newspaper [plural noun] appear on the shore,\nWaiting to take you away.\n'\
    'Climb in the back with your [part of the body] in the clouds,\nAnd you\'re'\
    ' gone.\nPicture yourself on a train in a [place],\nWith [adjective]'\
    ' porters with looking glass [plural article of clothing],\nSuddenly'\
    ' someone is there at the turnstile,\nThe girl with [adjective] eyes.\n'\
    '[female name] in the sky with [plural noun]...\n[female name] in the sky'\
    ' with [plural noun]...\n[female name] in the sky with [plural noun]...\n'

# A short template for testing the tell_story function
test = 'This should be an adjective: [adjective]. This should be a noun: [noun].'\
    ' This should be a verb: [verb].'

def tell_story(story_choice):
    """Chooses story template based off of user input, prompts user for words,
    and creates final story.

    Parameters
    ----------
    story_choice : string
        String to determine story template to choose, either title or number.

    Returns
    -------
    final_story: string
        String containing the story complete with user chosen words.
    """
    # Choose template
    if story_choice == 'awkward':
        story = awkward
    elif story_choice == 'force':
        story = force
    elif story_choice == 'piranha':
        story = piranha
    elif story_choice == 'vacation':
        story = vacation
    elif story_choice == 'lucy':
        story = lucy
    elif story_choice == 'test':
        story = test

    final_story = ''
    i = 0
    while i < len(story):
        # Get word to prompt user for
        if story[i] == '[':
            prompt = ''
            i = i + 1
            while story[i] != ']':
                prompt = prompt + story[i]
                i = i + 1
            # Add user input to final story
            final_story = final_story + input('Give a ' + prompt + '\n')
        else:
            # Add characters from template to final story
            final_story = final_story + story[i]
        i = i + 1

    return final_story
