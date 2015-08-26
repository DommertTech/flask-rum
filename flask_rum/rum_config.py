# Dommert's Flask-Rum [Version 0.1.0]
# Rum_Config.py
#---------------------------------

# Host IP
HOST='127.0.0.1'
PORT=5000
DEBUG=True

#SECRET_KEY='...'
#SESSION_COOKIE_DOMAIN
#SERVER_NAME

PROJECT_TITLE = '[Flask-Rum]'
# THEMES
THEME = 'banana' # DEFAULTS: coconut, banana
THEME_FOLDER = 'rum/themes/'+ THEME +'/'

ADMINS = [
('Admin', 'Admin@Domain.com')
]
# Defaults
TEMPLATE_DEFAULTS = {
'nav': 'site/blocks/rum_nav.html',
'menu': 'site/blocks/menu.html',
'footer': 'site/blocks/rum_footer.html'
}
