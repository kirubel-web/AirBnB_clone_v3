from flask import Blueprint
from api.v1.views.index import *  # noqa
from api.v1.views.states import *  # noqa
from api.v1.views.amenities import *  # noqa
from api.v1.views.cities import *
from api.v1.views.users import *  # noqa

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')
