from djongo import models
from django import forms
# Create your models here.

class Actions(models.Model):
    liste = models.CharField(max_length=80)
    class Meta:
        abstract = True
class Match(models.Model):
    dl_dest = models.CharField(max_length=80)
    in_port = models.IntegerField()
    dl_src = models.CharField(max_length=80)

    class Meta:
        abstract = True


class Flow(models.Model):
    _id = models.ObjectIdField()
    switch_name = models.CharField(max_length=50)
    priority = models.IntegerField()
    duration_sec = models.IntegerField()
    hard_timeout = models.IntegerField()
    byte_count = models.IntegerField()
    length = models.IntegerField()
    actions = models.EmbeddedField(
        model_container=Actions,
    )
    duration_nsec = models.IntegerField()
    packet_count = models.IntegerField()
    idle_timeout = models.IntegerField()
    cookie = models.IntegerField()
    flags = models.IntegerField()
    table_id = models.IntegerField()
    match = models.EmbeddedField(
        model_container=Match,
    )
    objects = models.DjongoManager()