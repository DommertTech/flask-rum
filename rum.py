# ---- RUM ----------------------------
from runme import app
from flask_rum.main import rum
import flask_rum.rum_config as rum_config
app.config.from_object(rum_config)

# Sample override of Theme
app.config.THEME_FOLDER='rum/banana/' # Flavor of Rum
app.register_blueprint(rum) #  Flask-Rum Blueprint
#------------------------------------