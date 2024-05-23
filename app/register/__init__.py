# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('register', __name__)

from app.register import routes
