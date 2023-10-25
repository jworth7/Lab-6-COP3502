
def encoder(password):
    newPassword = ''
    for i in range(0,len(password)):
        newPassword = newPassword + str(int(password[i])+3)
    return newPassword
