import logging
import subprocess
import shlex

logger = logging.getLogger('mgmt.' + __name__)


def _exec_command(cmd_line):
    try:
        subprocess.run(shlex.split(cmd_line), check=True)
        return True
    except subprocess.CalledProcessError as e:
        logger.error('cmd_line %s failed with output %s' %
                     (cmd_line, e.output))
        return False


def install_package(packagename, notice=None, cmd_before=None, cmd_after=None):
    cmd_line = 'apt install %s' % packagename
    success = _exec_command(cmd_line)
    if success:
        logger.info('Package %s installed successfully' % packagename)
    else:
        logger.info('Package %s install failed' % packagename)


def remove_package(packagename, notice=None, cmd_before=None, cmd_after=None):
    if cmd_before:
        _exec_commnad(cmd_before)
    cmd_line = 'apt remove %s' % packagename
    success = _exec_command(cmd_line)
    if success:
        logger.info('Package %s unistalled successfully' % packagename)
    else:
        logger.info('Package %s uninstall failed' % packagename)
