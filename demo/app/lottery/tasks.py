import logging
import random

from celery import shared_task


logger = logging.getLogger('lottery')


@shared_task
def pick_random_number():
    number = random.randint(0, 100)
    logger.info('Task %s completed. Result: %s', pick_random_number.request.id, number)
