import base64

MESSAGE = '''
EUMYHQINCRoSSUpeS08GHAkIFUlGREwLDgIADAAJHwFMSFtOSwwSGg8BBg0FSUBJRgsMAgQaFR1L 
SVtOTQ0FCxMLCAADAg9DR0hGDw8BCAscAQYNDxpLSVtOTREFBA4NBwwFSUZETBoADA4AFR1NRFFI 
Rh0NDwRJRkRMDg4BS0lbTk0TAgZASRE=
'''

KEY = 'jdkhanlian'

result = []
for i, c in enumerate(base64.b64decode(MESSAGE)):
    result.append(chr(ord(c) ^ ord(KEY[i % len(KEY)])))

print ''.join(result)