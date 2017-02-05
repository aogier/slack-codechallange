import logging
import subprocess
import shlex

logger = logging.getLogger('mgmt.' + __name__)


def _exec_command(cmd_line):
    try:
        process = subprocess.Popen(shlex.split(
            cmd_line), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        out, err = process.communicate()
        if out:
            logger.info(out)
        if err:
            logger.error(err)
    except subprocess.CalledProcessError as e:
        logger.error('cmd_line %s failed with output %s' %
                     (cmd_line, e.output))
        return False


def install_package(packagename, notice=None, cmd_before=None, cmd_after=None):
    cmd_line = 'apt-get install -y --quiet %s' % packagename
    if cmd_before:
        _exec_command(cmd_before)
    success = _exec_command(cmd_line)
    if cmd_after:
        _exec_command(cmd_after)

    if success:
        logger.info('Package %s installed successfully' % packagename)
    else:
        logger.info('Package %s install failed' % packagename)


def remove_package(packagename, notice=None, cmd_before=None, cmd_after=None):
    if cmd_before:
        _exec_command(cmd_before)
    cmd_line = 'apt-get remove -y --quiet %s' % packagename
    success = _exec_command(cmd_line)
    if success:
        logger.info('Package %s unistalled successfully' % packagename)
    else:
        logger.info('Package %s uninstall failed' % packagename)
