from django.contrib import admin
from .models.flow_model import Flow

@admin.register(Flow)
class FlowAdmin(admin.ModelAdmin):
    list_display = ('switch_name',)



