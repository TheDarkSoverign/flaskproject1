# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('posts', __name__)

from app.posts import routes
