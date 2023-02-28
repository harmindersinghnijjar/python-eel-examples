import eel

eel.init('web')

@eel.expose
def set_theme(theme):
    if theme == 'dark':
        eel.set_color('#333333')
        eel.set_background_color('#222222')
    else:
        eel.set_color('#000000')
        eel.set_background_color('#ffffff')

eel.start('index.html', size=(400, 400))
