from flask import Blueprint


# cms_bp = Blueprint('cms', __name__, subdomain='cms')
cms_bp = Blueprint('cms', __name__, url_prefix='/cms/')


from . import cms_views