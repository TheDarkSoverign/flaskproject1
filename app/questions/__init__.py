# -*- coding: utf-8 -*-
from flask import Blueprint

bp = Blueprint('questions', __name__)

from app.questions import routes
