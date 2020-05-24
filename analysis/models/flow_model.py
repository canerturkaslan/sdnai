from djongo import models


class Actions(models.Model):
    OUTPUT = models.CharField(max_length=80, blank=True)

    class Meta:
        abstract = True
    def __str__(self):
        return self.OUTPUT

class Match(models.Model):
    dl_dst = models.CharField(max_length=80, blank=True)
    in_port = models.IntegerField(blank=True, max_length=15)
    dl_src = models.CharField(max_length=80, blank=True)

    class Meta:
        abstract = True


class Flow(models.Model):
    _id = models.ObjectIdField()
    check_id = models.CharField(max_length=24)
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
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.switch_name
