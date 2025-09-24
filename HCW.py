import random

game3 = input('Do you want to play game 3?: ')

if (game3 == 'no'):
    print ('Click clear to restart')
else:
    print('Get ready for hardcore wordle')
    score3 = 0
    guesses = 14
    words = ['aback', 'abaft', 'abase', 'abate', 'abbey', 'abbot', 'abhor', 'abide', 'abler', 'abode', 'about', 'above', 'abuse', 'abyss', 'ached', 'aches', 'acids', 'acorn', 'acres', 'acrid', 'acted', 'actor', 'acute', 'adage', 'adapt', 'added', 'adder', 'adept', 'adieu', 'admit', 'adobe', 'adopt', 'adore', 'adorn', 'adult', 'aegis', 'aeons', 'affix', 'afire', 'afoot', 'after', 'again', 'agape', 'agate', 'agent', 'aging', 'aglow', 'agony', 'agree', 'ahead', 'aided', 'aides', 'ailed', 'aimed', 'aired', 'aisle', 'alarm', 'album', 'alder', 'alert', 'alias', 'alibi', 'alien', 'alike', 'alive', 'allay', 'alley', 'allot', 'allow', 'alloy', 'aloes', 'aloft', 'alone', 'along', 'aloud', 'amass', 'amaze', 'amber', 'amble', 'amend', 'amigo', 'amiss', 'amity', 'among', 'amour', 'ample', 'amply', 'amuse', 'angel', 'anger', 'angle', 'angry', 'angst', 'annoy', 'anvil', 'apace', 'apart', 'aping', 'appal', 'apple', 'apply', 'aptly', 'areas', 'avert', 'avoid', 'avows', 'await', 'awake', 'award', 'aware', 'awful', 'awoke', 'axiom', 'axles', 'azure', 'cabal', 'cabby', 'cabin', 'cable', 'cacao', 'cache', 'cadet', 'cadre', 'caged', 'cages', 'cairn', 'canal', 'candy', 'canes', 'canny', 'canoe', 'canon', 'cards', 'cared', 'cares', 'cargo', 'carol', 'carry', 'carts', 'carve', 'cased', 'cases', 'casks', 'caste', 'casts', 'catch', 'cater', 'cause', 'caved', 'caves', 'cavil', 'cease', 'cedar', 'ceded', 'cells', 'cents', 'chaos', 'chaps', 'charm', 'chart', 'chary', 'chase', 'chasm', 'chats', 'cheap', 'cheat', 'check', 'cheek', 'cheer', 'chefs', 'chess', 'chest', 'chick', 'chide', 'chief', 'child', 'chill', 'chime', 'china', 'chunk', 'civic', 'civil', 'clack', 'claim', 'cloak', 'clock', 'clods', 'clogs', 'close', 'cloth', 'cloud', 'clout', 'clove', 'clown', 'clubs', 'cluck', 'clues', 'clump', 'clung', 'coach', 'coals', 'coast', 'coats', 'cobra', 'cocoa', 'codes', 'coils', 'coins', 'colds', 'colic', 'colon', 'colts', 'combs', 'comer', 'comes', 'comet', 'comic', 'comma', 'conch', 'cones', 'conic', 'cooed', 'cooks', 'cools', 'copra', 'copse', 'coral', 'cords', 'cores', 'corks', 'corns', 'corps', 'costs', 'cotes', 'couch', 'cough', 'could', 'count', 'coupe', 'coups', 'court', 'cover', 'coves', 'covet', 'covey', 'cowed', 'cower', 'coyly', 'cozen', 'crabs', 'crack', 'craft', 'crags', 'cramp', 'crane', 'crank', 'crape', 'crash', 'crass', 'crate', 'crave', 'crawl', 'craze', 'crazy', 'creak', 'cream', 'credo', 'creed', 'creek', 'creep', 'crepe', 'crept', 'cress', 'crest', 'crews', 'cribs', 'crick', 'cried', 'crime', 'crimp', 'crisp', 'croak', 'crock', 'crone', 'crony', 'crook', 'crops', 'cross', 'croup', 'crowd', 'crown', 'crows', 'crude', 'cruel', 'crumb', 'crush', 'crust', 'crypt', 'cubes', 'cubic', 'cubit', 'cuffs', 'cults', 'curds', 'cured', 'cures', 'curls', 'curly', 'curry', 'curse', 'curst', 'curve', 'cycle', 'cynic', 'daily', 'dairy', 'daisy', 'dales', 'dally', 'dames', 'damps', 'dazed', 'deals', 'dealt', 'deans', 'dears', 'death', 'debar', 'debit', 'debts', 'debut', 'decay', 'decks', 'decoy', 'decry', 'deeds', 'deems', 'deeps', 'defer', 'deign', 'deity', 'delay', 'dells', 'delta', 'delve', 'demon', 'demur', 'dense', 'dents', 'depot', 'depth', 'derby', 'desks', 'deter', 'deuce', 'devil', 'diary', 'diced', 'dices', 'dicta', 'diets', 'digit', 'dikes', 'dimes', 'dimly', 'dined', 'diner', 'dines', 'dingy', 'dirge', 'dirty', 'discs', 'disks', 'ditch', 'dizzy', 'docks', 'dodge', 'doers', 'dogma', 'doing', 'doled', 'dolls', 'domed', 'domes', 'donor', 'dooms', 'doors', 'dosed', 'doses', 'doted', 'dotes', 'doubt', 'dough', 'doves', 'dowdy', 'downs', 'downy', 'dowry', 'dozed', 'dozen', 'draft', 'drags', 'drain', 'drake', 'drama', 'drams', 'drank', 'drape', 'dread', 'dream', 'dregs', 'dress', 'dried', 'droll', 'drone', 'droop', 'drops', 'dross', 'drove', 'drown', 'drugs', 'drums', 'drunk', 'dryly', 'ducal', 'ducat', 'duchy', 'ducks', 'ducts', 'duels', 'dunce', 'dunes', 'duped', 'dupes', 'dusky', 'dusty', 'dwarf', 'dwell', 'dwelt', 'dying', 'eager', 'eagle', 'earls', 'early', 'earns', 'earth', 'eased', 'easel', 'eases', 'eaten', 'eater', 'eaves', 'ebbed', 'ebony', 'edged', 'edges', 'edict', 'edify', 'eerie', 'egged', 'eight', 'eject', 'elate', 'elbow', 'elder', 'elect', 'elegy', 'elfin', 'elite', 'elope', 'elude', 'elves', 'email', 'emits', 'empty', 'enact', 'ended', 'endow', 'enemy', 'enjoy', 'ennui', 'enrol', 'ensue', 'enter', 'entry', 'envoy', 'epics', 'epoch', 'equal', 'equip', 'erase', 'erect', 'erred', 'error', 'essay', 'ether', 'ethic', 'evade', 'event', 'every', 'evils', 'evoke', 'exalt', 'excel', 'exert', 'exile', 'exist', 'exits', 'expel', 'extol', 'extra', 'exult', 'eying', 'eyrie']
def findCommonCharacters(string1, string2):
    set1 = set(string1)
    set2 = set(string2)
    common_chars = set1.intersection(set2)
    return list(common_chars)

if (game3 == 'yes'):
    randomWord = random.choice(words)

while (guesses > 0):
    guessedWord = input('Input a 5 letter word: ')
    guessedWordCharacters = list(guessedWord)
    guessedWordCharacters = len(guessedWordCharacters)
    if (guessedWordCharacters == 5):
        h = 'h'
    else:
        guesses = 0
        print('Only 5 letter words')
    matches = findCommonCharacters(randomWord, guessedWord)
    print(f'The common characters are {matches}')
    guesses = guesses - 1
    
    if (guessedWord == randomWord):
        score3 = score3 + 1
        print('Yay you got the word')
        randomWord = random.choice(words)
    
    if (guesses == 0):
        print(f'The word was {randomWord}')
        print(f'Your score is {score3}')

if (score3 < 3):
    print('Better luck next time, you are not a master at wordle')
else:
    print('Congratulations... You are a wordle master, and one of the luckiest people on earth')
