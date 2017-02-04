import inspect
import logging
from functools import partial
import os

import yaml

from ops_registry import OpsRegistry


class HostParser(object):

    def __init__(self, host_config, host_properties_location='hosts', ops_registry=OpsRegistry()):
        self.host_properties_location = host_properties_location
        self.host_config = host_config
        self.ops_registry = ops_registry
        self.parsed_action = []
        self.logger = logging.getLogger('mgmt.' + __name__)

    def execute(self, action):
        func = self.ops_registry.operations_registry[action['action_name']]
        # Positional arguments
        for m in action['mandatory_params']:
            func = partial(func, action['action_params'][m])
            del action['action_params'][m]
        # Keword arguments
        for k, v in action['action_params'].items():
            t = {k: v}
            func = partial(func, **t)

        func()

    def parse(self):
        try:
            host_config_file = os.path.join(
                self.host_properties_location, self.host_config)
            with open(host_config_file, 'r') as f:
                config = yaml.load(f)
                for action in config['actions']:
                    for action_name, action_params in action['name'].items():
                        """
                        While checking we also return the mandatory params in order to execute
                        eventually the action.
                        """
                        mandatory_params = self._check(
                            action_name, action_params)
                        if mandatory_params:
                            self.parsed_action.append({'action_name': action_name,
                                                       'action_params': action_params,
                                                       'mandatory_params': mandatory_params})
                        else:
                            self.logger.info(
                                'Action %s could not be added' % action_name)
                            self.logger.info("Finished parsing actions for %s" %
                                             str(self.host_config))

        except FileNotFoundError:
            self.logger.error('host_config: %s not found. Abort' %
                              str(host_config_file))
            return False
        except yaml.parser.ParserError:
            self.logger.error(
                'host_config: %s is not valid yaml. Abort' % str(self.host_config))
            return False

        return self.parsed_action

    def _check(self, action_name, action_params):
        if action_name in self.ops_registry.operations_registry.keys():
            self.logger.debug("Action: %s found" % action_name)

            self.logger.debug(
                "Retrieving mandatory arguments for %s action" % action_name)
            signature = inspect.signature(
                self.ops_registry.operations_registry[action_name])
            mandatory_params = []
            not_mandatory_params = []
            """
            inspect.Paramenters is an ordered dictionary we can rely on that when we build the function back
            """
            for param in signature.parameters.values():
                if param.default == inspect.Parameter.empty:
                    mandatory_params.append(param.name)
                else:
                    not_mandatory_params.append(param.name)

            for mandatory_param in mandatory_params:
                if mandatory_param not in action_params:
                    self.logger.error("mandatory argument %s for action %s not specified. Abort" % (
                        mandatory_param, action_name))
                    return False

            self.logger.debug("Emitting %s with %s as argument" %
                              (action_name, action_params))
            return mandatory_params
        else:
            self.logger.error(
                "Action: `` %s `` not registered. Abort" % action_name)
            return False
