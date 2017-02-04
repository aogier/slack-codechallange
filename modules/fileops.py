import logging
logger = logging.getLogger('mgmt.' + __name__)


def copy(source, destination, mode='0777'):
    logger.info('copy() called')


def copy_from_template(source, destination, variables, mode='0777', test='cacca'):
    logger.info('copy_from_template() called')
