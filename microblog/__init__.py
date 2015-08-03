#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask import Flask
from flask.ext.mongoengine import MongoEngine
app = Flask(__name__)

app.config.from_object('config')

db = MongoEngine(app)

from microblog import models,views
