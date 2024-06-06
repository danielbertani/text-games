# Inspired by: 
# https://reintech.io/blog/how-to-create-a-text-based-adventure-game-with-python
# Modified to create my own game

rooms = {
    'start': {
        'description': """You are trapped in a dark labyrinth. To move you can use the following keys:
          f - forward
          b - back
          r - right
          l - left
          e - enter
        What would you like to do?
        """,
        'forward': 'room1',
        'right': 'room5'
    },
    'room1': {
        'description': '\nYou hear the scraping sound of scithe against stone.',
        'forward': 'room2',
        'back': 'start'
    },
    'room2': {
        'description': '\nYou continue exploring the labyrinth.',
        'right': 'room3',
        'back': 'room1'
    },
    'room3': {
        'description': '\nYou found a candle lighting dimly the way.',
        'forward': 'room4',
        'back': 'room2'
    },
    'room5': {
        'description': '\nThere is a picture in the wall of an old man with his two daughters. The man in the picture is staring at you.',
        'forward': 'room6',
        'back': 'start'
    },    
    'room6': {
        'description': '\nYou see a mysterious figure standing in the dark with red glowing eyes staring at you. It is not approaching you.',
        'left': 'room7',
        'back': 'room5'
    },
    'room7': {
        'description': '\nYou se a dim blue glowing light to your left emiting a strange aura.',
        'left': 'enter',
        'back': 'room6'
    },
    'enter': {
        'description': '\nYou found the source of the light. It is a blue glowing portal. Do you want to enter? It can be an exit or a trap, but it is the only way you got. ',
        'enter': 'start_2',
        'back': 'room7'
    },
    'start_2': {
        'description': '\nOh no! You are stuck in a new bigger labyrith. Good luck! Try to find the next portal. Maybe it is the exit this time.',
        'end': True
    },
    'room4': {
        'description': '\nYou found a dead end, guarded by a Lich. It raised its scythe and you got killed by it. Better luck next time!',
        'back': 'room3',
        'end': True
    }
}

def show_room(room):
    print(room['description'])

    if 'forward' in room:
        print('There is a path to move forward.')
    if 'back' in room:
        print('There is a path to go back.')
    if 'left' in room:
        print('There is a path to your left.')
    if 'right' in room:
        print('There is a path to your right.')
    if 'enter' in room:
        print('You can enter the portal.')

def get_action(room):
    while True:
        action = input('What do you want to do? ').lower().strip()

        if action == 'f' and 'forward' in room:
            return room['forward']
        elif action == 'l' and 'left' in room:
            return room['left']
        elif action == 'b' and 'back' in room:
            return room['back']
        elif action == 'r' and 'right' in room:
            return room['right']
        elif action == 'e' and 'enter' in room:
            return room['enter']
        else:
            print('Invalid action. Try again.')

current_room = rooms['start']

while 'end' not in current_room:
    show_room(current_room)
    next_room = get_action(current_room)
    current_room = rooms[next_room]

print(current_room['description'])