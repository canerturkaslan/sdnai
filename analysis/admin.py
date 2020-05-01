from django.contrib import admin
from .models.flow_model import Flow,Actions
from .models.port_model import Port



@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):

    list_display = ('switch_name', 'actions__OUTPUT', 'match__dl_dst','match__dl_src','match__in_port','byte_count','packet_count','table_id','priority','created_at')
    search_fields = ('switch_name','byte_count','packet_count','table_id','priority','actions')

    def actions__OUTPUT(self,obj):
        return obj.actions.OUTPUT

    def match__dl_dst(self,obj):
        return obj.match.dl_dst

    def match__in_port(self,obj):
        return obj.match.in_port

    def match__dl_src(self,obj):
        return obj.match.dl_src

@admin.register(Port)
class PortAdmin(admin.ModelAdmin):
    list_display = ('name', 'mac_addr', 'rx_crc_err','tx_bytes','rx_dropped','port_no','rx_over_err',
                    'rx_frame_err','rx_bytes','tx_errors','duration_nsec',
                    'collisions','duration_sec','rx_errors','tx_packets','curr','tx_dropped','rx_packets','created_at')
    search_fields = ('mac_addr', 'name')
