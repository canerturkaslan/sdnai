from django.contrib import admin
from .models.flow_model import Flow




@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):

    list_display = ('switch_name','actions__OUTPUT', 'match__dl_dst','match__dl_src','match__in_port','byte_count','packet_count','table_id','priority')

    def actions__OUTPUT(self,obj):
        return obj.actions.OUTPUT

    def match__dl_dst(self,obj):
        return obj.match.dl_dst

    def match__in_port(self,obj):
        return obj.match.in_port

    def match__dl_src(self,obj):
        return obj.match.dl_src

