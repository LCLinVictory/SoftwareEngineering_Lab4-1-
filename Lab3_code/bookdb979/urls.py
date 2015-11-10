from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from BookDB import views

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$',views.bookdb_hello),
    url(r'^bookdb/$',views.bookdb_begin),
    url(r'^author-list/$',views.author_test),
    url(r'^bookdb/search_author/$',views.search_author),
    url(r'^bookdb/search_author/book_list/([^/]+)/$',views.search_author_book),
    url(r'^bookdb/add_book/$',views.add_book),
    url(r'^bookdb/add_author/$',views.add_author),
    url(r'^bookdb/update_book/([^/]+)/$',views.update_book),
)
