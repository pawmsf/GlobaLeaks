# -*- coding: UTF-8
# datainit.py: database initialization
#   ******************
import json

import re
import os

from globaleaks import models
from globaleaks.orm import transact
from globaleaks.handlers.admin.user import db_create_admin
#from globaleaks.handlers.submission import db_assign_submission_sequence
from globaleaks.handlers.admin.field import db_create_field
from globaleaks.rest import errors, requests
from globaleaks.settings import GLSettings
from globaleaks.security import get_salt
from globaleaks.third_party import rstr
from globaleaks.utils.utility import datetime_null


def load_appdata():
    if os.path.exists(GLSettings.appdata_file):
        with file(GLSettings.appdata_file, 'r') as f:
            json_string = f.read()
            appdata_dict = json.loads(json_string)
            return appdata_dict

    raise errors.InternalServerError("Unable to load application data")


def load_default_fields(store):
    this_directory = os.path.dirname(__file__)

    if os.path.exists(GLSettings.fields_path):
        for fname in os.listdir(GLSettings.fields_path):
            fpath = os.path.join(GLSettings.fields_path, fname)
            with file(fpath, 'r') as f:
                json_string = f.read()
                field_dict = json.loads(json_string)
                db_create_field(store, field_dict, None)
                return

    raise errors.InternalServerError("Unable to load default fields")


def db_init_appdata(store):
    # Load new appdata
    appdata_dict = load_appdata()

    # Drop old appdata
    store.find(models.ApplicationData).remove()

    # Setup new appdata
    appdata = models.ApplicationData(appdata_dict)
    appdata.version = appdata_dict['version']
    appdata.default_questionnaire = appdata_dict['default_questionnaire']

    store.add(models.ApplicationData(appdata_dict))

    return appdata_dict


@transact
def init_appdata(store):
    return db_init_appdata(store)