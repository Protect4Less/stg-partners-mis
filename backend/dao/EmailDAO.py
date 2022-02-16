from django.db import models
from django.conf import settings
from django.db import connection
from decouple import config
from dateutil.relativedelta import relativedelta

import datetime
from datetime import datetime


# logger = logging.getLogger(__name__)

class EmailDAO():

    def insert_email_tran(data):
        cursor = connection.cursor()
        column_keys = ""
        column_values = ""
        for k, v in data.items():
            if k:
                column_keys += k+", "
                column_values += "'"+str(v)+"', "

        column_keys += "et_addedon"
        column_values += "NOW()"
        query = "INSERT INTO "+config('P4L_DB_NAME')+".`email_transaction` ("+column_keys+") VALUES ("+column_values+")"
        cursor.execute(query)
        return cursor.lastrowid