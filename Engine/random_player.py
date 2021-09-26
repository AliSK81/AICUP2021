import random
init_msg = input()
# Do stuff
print('init confirm')
while True:
    state_msg = input()
    if 'term' in state_msg:
        break
    # Do stuff
    print(int(random.random() * 10))