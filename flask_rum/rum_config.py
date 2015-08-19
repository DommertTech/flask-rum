# Flask-Rum [Version 0.1.2]
# Rum_Config.py
#---------------------------------

# Host IP
HOST='127.0.0.1'
PORT=5000
DEBUG=True

#SECRET_KEY='...'
#SESSION_COOKIE_DOMAIN
#SERVER_NAME

THEME = 'coconut'
THEME_FOLDER = 'rum/themes/'+ THEME +'/'
PROJECT_TITLE = '[Flask-Rum]'
ADMINS = [
('Admin', 'Admin@Domain.com')
]
# Defaults
TEMPLATE_DEFAULTS = {
'nav': 'site/blocks/rum_nav.html',
'menu': 'site/blocks/menu.html',
'footer': 'site/blocks/rum_footer.html'
}
