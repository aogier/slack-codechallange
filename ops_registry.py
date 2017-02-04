import logging

from modules.fileops import copy

OPERATIONS_REGISTRY = {
    'copy': copy
}


class OpsRegistry(object):

    def __init__(self):
        self.logger = logging.getLogger('mgmt.' + __name__)
        self.operations_registry = OPERATIONS_REGISTRY

    def add_operation(self, operation, function):
        try:
            if self.operations_registry[operation]:
                self.logger.error('Operation %s already exists' % operation)
        except KeyError:
            self.operations_registry[operation] = function
            self.logger.info('Operation %s added successfully' % operation)

    def delete_operation(self, operation):
        try:
            if self.operations[operation]:
                del self.operations_registry[operation]
                self.logger.info(
                    'Operation: %s successfully removed' % str(operation))
        except KeyError:
            self.logger.warning(
                'Operation: %s not found. Not removed' % str(operation))
