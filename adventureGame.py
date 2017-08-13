import random
import time


def intro():
  print('\033[93m\033[1mVACCINE GAME\033[0m')
  print('\033[95mThe whole world being attacked by undetermined virus that caused people die in every hour')
  print('and you are the only healthy survivor who will be able to find a vaccine that can save lives.')
  time.sleep(2)
  print('The virus spreads very quickly, people will all die if you do not give them the vaccine within 1 hour.')
  print('There are 3 entrances in the building and only one that leads you to the vaccine.')
  time.sleep(2)
  print('The other two will bring you to the starting point and you will not have time to try again.')
  print('The vaccine locates in the building next to you and it takes you 20 mins to get in the building.')
  time.sleep(2)
  print('However, you do not know exactly where the vaccine it. Do you want to take a risk?\033[0m')

def choose_gate():
  while True:
    gate = input('\033[94mWhich gate do you enter? (1 or 2 or 3): \033[0m')
    if gate < 0 or gate > 3:
      print('\033[93mPlease re-enter valid option!\033[0m')
    else:
      break

  return gate

def validate(gate):
  print('You are heading to the gate...')
  time.sleep(2)
  print('There is no one there except you...')
  time.sleep(2)
  print('Time to open the door...')
  time.sleep(2)

  target = random.randint(1, 3)

  if gate == target:
    print('\033[92mCongratulations, you saved the world!!!\033[0m')
  else:
    print('\033[91mSorry but you will be the only one living in this world.\033[0m')

while True:
  intro()
  choice = choose_gate()
  validate(choice)
  replay = raw_input('\033[94mDo you want to replay? (yes or y to replay): \033[0m')
  if replay != 'yes' and replay != 'y':
    print('\033[1mThank you for playing. Good bye!\033[0m')
    break
