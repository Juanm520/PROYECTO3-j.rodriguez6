from flask import Blueprint, render_template, request
from flask_login import login_user
from models.Usuarios import Usuario


'''auth_blueprint = Blueprint('auth', __name__, url_prefix = '/login/auth')
@auth_blueprint.route('/', method='POST')
def auth_controller():
    usuario = request.args.get('user')
    contrasena = request.args.get('password')
    try:
        user = Usuario.query.filter_by(usernmae = usuario, password = contrasena).first()
        if user.password == contrasena:
            login_user(user)
            if user.is_admin:
                return render_template('dashboard_admin.html')
            else: 
                return render_template('dashboard.html')
        else:
            return render_template('index.html', str = 'Contraseña incorrecta.')
    except Exception:
        return render_template('index.html', str = 'No existe usuario.')'''
