from django.urls import path

urlpatterns = [
    '',
    path(
        'attachments/',
        'sirtrevor.views.attachment',
        name='sirtrevor_attachments',
    ),
]
