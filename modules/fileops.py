import logging
import os
from os.path import dirname, isdir, join, basename
import shutil

import jinja2

logger = logging.getLogger('mgmt.' + __name__)


def copy(source, destination, mode='0777'):
    logger.info('copy() called')
    try:
        if source.startswith('/'):
            shutil.copy(source, destination)
        else:
            root = dirname(dirname(__file__))
            # TODO: This is somehow hardcoded. The fix would be somehow know
            # hosts_config_directory from HostConfig
            data_dir = join(root, 'hosts/data')
            if isdir(data_dir):
                source = join(data_dir, basename(source))
                shutil.copy(source, destination)
            else:
                os.chmod(destination, int(mode))
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
