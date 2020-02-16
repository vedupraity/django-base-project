from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('admin/', admin.site.urls),
]


import logging


logger = logging.getLogger(__name__)


def sample_logging():
    logger.debug('logger.debug')
    logger.error('logger.error')


sample_logging()
