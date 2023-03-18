import json
from datetime import timedelta

from django.contrib import admin
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F

from .models import Event, ProductionSchedule, Machine


# Register your models here.
class EventDurationFilter(admin.SimpleListFilter):
    title = 'Event duration'
    parameter_name = 'duration'

    def lookups(self, request, model_admin):
        return (
            ('short', 'Short events (1 hour or less)'),
            ('long', 'Long events (more than 1 hour)'),
        )

    def queryset(self, request, queryset):
        if self.value() == 'short':
            return queryset.filter(end_time__lte=F('start_time') + timedelta(hours=1))
        elif self.value() == 'long':
            return queryset.filter(end_time__gt=F('start_time') + timedelta(hours=1))


@admin.register(ProductionSchedule)
class ProductionScheduleAdmin(admin.ModelAdmin):
    list_display = ('machine', 'event', 'start_time', 'end_time', 'duration')
    list_filter = ('machine', 'event', 'start_time', 'end_time', EventDurationFilter)
    search_fields = ('machine__serial_number', 'event__event_code')
    autocomplete_fields = ('machine',)

    def changelist_view(self, request, extra_context=None):
        schedules = ProductionSchedule.objects.all()
        chart_data = []
        for schedule in schedules:
            chart_data.append({
                'start': schedule.start_time.isoformat(),
                'end': schedule.end_time.isoformat(),
                'label': schedule.machine.name,
            })

        extra_context = extra_context or {"chart_data": chart_data}

        # Call the superclass changelist_view to render the page
        return super().changelist_view(request, extra_context=extra_context)


@admin.register(Machine)
class MachineAdmin(admin.ModelAdmin):
    ordering = ('name',)
    search_fields = ('serial_number',)


admin.site.register(Event)
