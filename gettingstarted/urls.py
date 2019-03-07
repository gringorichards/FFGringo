from django.urls import path, include

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("reports/manager_reports/1/", hello.views.manager_reports1, name="manager_reports1"),
    path("reports/manager_reports/1/", hello.views.manager_reports1, name="manager_reports1"),
    path("reports/manager_reports/2/", hello.views.manager_reports2, name="manager_reports2"),
    path("reports/manager_reports/3/", hello.views.manager_reports3, name="manager_reports3"),
    path("reports/manager_reports/4/", hello.views.manager_reports4, name="manager_reports4"),
    path("manager_of_the_week/", hello.views.manager_of_the_week, name="manager_of_the_week"),
    path("reports/", hello.views.reports, name="reports"),
    path("admin/", admin.site.urls),
]
