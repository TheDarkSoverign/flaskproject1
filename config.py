# -*- coding: utf-8 -*-
class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql://root:root@mysql:3306/flaskdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    POSTS_PER_PAGE = 3
