def new_password(newpassword, oldpassword):
    if newpassword != oldpassword and len(newpassword) >= 6 and not str.isalpha(newpassword):
        print('True')
    else:
        print('False')