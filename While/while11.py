users = ['Ali', 'Budi', 'Citra', 'Dodi', 'Ella']
active_users = ['Ali',  'Citra', 'Ella']

i = 0
while i < len(users):
    if users[i] in active_users:
        print (users[i], 'is active')
    else:
        print (users[i], 'is not active')
    i += 1