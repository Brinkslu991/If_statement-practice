superheros = ['Thor', 'Spider-Man', 'Hulk', 'Deadpool', 'Batman']
fav = ('Spider-Man')
if fav in superheros:
    print(f'Hey look {fav}')

score = int(input('Enter quiz score: '))
if score >= 85:
    print('You get a B')

quote = ('There is no victory without sacrifice.')
if quote.startswith('T'):
    print('This quote starts with the letter T')

filename = ('file.png')
if filename.endswith('.png'):
    print('This file name ends with .png')

is_registered = True
if is_registered == False:
    print('You are not registered')