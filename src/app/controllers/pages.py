# Flask standard imports for controllers
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session,
    url_for
)


# Create the blueprint
bp = Blueprint('pages', __name__, url_prefix='/pages')


# Routes and views
@bp.route('/homepage')
def homepage():
    language = 'en'
    charset = 'utf-8'
    title = 'Welcome to Artumis'
    return render_template(
        'pages/homepage.html.jinja',
        language=language,
        charset=charset,
        title=title
    )
