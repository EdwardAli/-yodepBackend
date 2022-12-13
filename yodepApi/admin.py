from multiprocessing import Event
from django.contrib import admin

from . models import Career, Testimonial, Project, Gallary, News, Events, Blog, Comment, Partner, Vacancy

# Register your models here.


admin.site.register(Testimonial)
admin.site.register(Project)
admin.site.register(Career)
admin.site.register(Gallary)
admin.site.register(News)
admin.site.register(Events)
admin.site.register(Blog)
admin.site.register(Comment)
admin.site.register(Partner)
admin.site.register(Vacancy)