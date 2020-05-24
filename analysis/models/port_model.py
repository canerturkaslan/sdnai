from djongo import models


class Port(models.Model):
    _id = models.ObjectIdField()
    tx_dropped = models.IntegerField()
    rx_packets = models.IntegerField()
    rx_crc_err = models.IntegerField()
    tx_bytes = models.IntegerField()
    rx_dropped = models.IntegerField()
    port_no = models.IntegerField()
    rx_over_err = models.IntegerField()
    rx_frame_err = models.IntegerField()
    rx_bytes = models.IntegerField()
    tx_errors = models.IntegerField()
    duration_nsec = models.IntegerField()
    collisions = models.IntegerField()
    duration_sec = models.IntegerField()
    rx_errors = models.IntegerField()
    tx_packets = models.IntegerField()
    curr = models.IntegerField()
    name = models.CharField(max_length=60)
    mac_addr = models.CharField(max_length=60)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = models.DjongoManager()

    def __str__(self):
        return self.name
