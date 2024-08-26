import os
from flask_admin import Admin
from models import db, User
from flask_admin.contrib.sqla import ModelView

from models import db, User, People, Planet, Favorite

def setup_admin(app):
    app.secret_key = os.environ.get('FLASK_APP_KEY', 'sample key')
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    admin = Admin(app, name='4Geeks Admin', template_mode='bootstrap3')

    # Añadir el modelo User al panel de administración
    admin.add_view(ModelView(User, db.session))
    
    # Añadir el modelo People al panel de administración
    admin.add_view(ModelView(People, db.session))
    
    # Añadir el modelo Planet al panel de administración
    admin.add_view(ModelView(Planet, db.session))
    
    # Añadir el modelo Favorite al panel de administración
    admin.add_view(ModelView(Favorite, db.session))
