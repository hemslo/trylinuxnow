# -*- coding: utf-8 -*-
from django.contrib import admin
from trylinux.models import Course, Stages


class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'info')
    #filter_horizontal = ('stages',)
    def __unicode__(self):
        return u'%s %s %s' % (self.id, self.name, self.info)


class StagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'content')
    def __unicode__(self):
        return u'%s %s' % (self.id, self.content)


admin.site.register(Course, CourseAdmin)
admin.site.register(Stages, StagesAdmin)
