import logging
import os
import shutil

import jinja2

logger = logging.getLogger('mgmt.' + __name__)


def copy(source, destination, mode='0777'):
    logger.info('copy() called')
    try:
        shutil.copy(source, destination)
        os.chmod(destination, mode)
    except FileNotFoundError as e:
        logger.error('copy of %s to %s failed.' % (source, destination))
        logger.error(e)
    except PermissionError as e:
        logger.error('copy of %s to %s failed.' % (source, destination))
        logger.error(e)


def copy_from_template(source, destination, variables, mode='0777', test='cacca'):
    logger.info('copy_from_template() called')
    try:
        with open(source, 'r') as t:
            template = jinja2.Template(t.read())
            rendered = template.render(variables)
            try:
                with open(destination, 'w') as w:
                    w.write(rendered)
            except FileNotFoundError as e:
                logger.error('Could not write to %s' % destination)
                logger.error(e)
    except FileNotFoundError as e:
        logger.error('Could not open %s ' % source)
        logger.error(e)
