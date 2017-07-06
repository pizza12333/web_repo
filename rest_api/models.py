from __future__ import unicode_literals
from django.db import models

class ChickenData(models.Model):
    id = models.BigIntegerField(db_column='Id', primary_key=True)  # Field name made lowercase.
    date = models.TextField(db_column='Date', blank=True, null=True)  # Field name made lowercase.
    year = models.BigIntegerField(db_column='Year', blank=True, null=True)  # Field name made lowercase.
    month = models.BigIntegerField(db_column='Month', blank=True, null=True)  # Field name made lowercase.
    day = models.BigIntegerField(db_column='Day', blank=True, null=True)  # Field name made lowercase.
    day_of_weeks = models.BigIntegerField(db_column='Day_of_weeks', blank=True, null=True)  # Field name made lowercase.
    gender = models.BigIntegerField(db_column='Gender', blank=True, null=True)  # Field name made lowercase.
    age = models.BigIntegerField(db_column='Age', blank=True, null=True)  # Field name made lowercase.
    loc_mid = models.TextField(db_column='Loc_mid', blank=True, null=True)  # Field name made lowercase.
    call = models.BigIntegerField(db_column='Call', blank=True, null=True)  # Field name made lowercase.
    class Meta:
        managed = False
        db_table = 'chicken_data'