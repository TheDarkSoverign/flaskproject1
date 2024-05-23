# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('page', __name__)

from app.page import routes
