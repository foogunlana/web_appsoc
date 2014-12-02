from __future__ import absolute_import

from celery import shared_task

import time


@shared_task
def add(x, y):
    for num in range(1, 10):
        time.sleep(1)
        print num, "........."
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)
