import logging
import os

from django.shortcuts import render

from lottery.tasks import pick_random_number


logger = logging.getLogger('lottery')


def lottery(request):
    log_data = open('{}/logs/lottery.log'.format(os.path.dirname(os.path.dirname(__file__))), 'r').read()
    context = {
        'log': log_data,
    }
    if request.method == 'POST':
        task = pick_random_number.delay()
        logger.info('Task %s scheduled.', task.task_id)
        context['task_id'] = task.task_id
    return render(request, 'lottery/lottery.html', context)
