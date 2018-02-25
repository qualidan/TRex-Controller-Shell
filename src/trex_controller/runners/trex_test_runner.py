#!/usr/bin/python
# -*- coding: utf-8 -*-

from cloudshell.traffic.trex.cli.trex_cli_handler import TRexCliHandler
from cloudshell.traffic.trex.client.trex_client.trex_client import CTRexClient

from trex_controller.flows.load_test_config_flow import TRexLoadTestConfigFlow
from trex_controller.flows.traffic_controll_flow import TRexTrafficControlFlow
from trex_controller.flows.trex_results_flow import TRexResultsFlow


class TRexTestRunner(object):
    def __init__(self, cli, resource_config, logger):

        self._cli = cli
        self._resource_config = resource_config
        self._logger = logger

    @property
    def cli_handler(self):
        """ CLI Handler property """

        return TRexCliHandler(self._cli,
                              self._resource_config.address,
                              self._resource_config.username,
                              self._resource_config.password)

    @property
    def trex_client(self):
        """ TRex client """

        return CTRexClient(trex_host=self._resource_config.address,
                           trex_daemon_port=self._resource_config.trex_daemon_port)

    @property
    def load_test_config_flow(self):
        """  """
        return TRexLoadTestConfigFlow(cli_handler=self.cli_handler,
                                      trex_client=self.trex_client,
                                      logger=self._logger)

    @property
    def start_traffic_flow(self):
        """  """

        return TRexTrafficControlFlow(trex_client=self.trex_client, logger=self._logger)

    @property
    def stop_traffic_flow(self):
        """  """

        return TRexTrafficControlFlow(trex_client=self.trex_client, logger=self._logger)

    @property
    def get_results_flow(self):
        """  """

        return TRexResultsFlow(trex_client=self.trex_client, logger=self._logger)

    def load_test_config(self, test_config_url):
        """ Load test configuration files from FTP/TFTP Server """

        return self.load_test_config_flow.load_test_config(test_config_path=test_config_url)

    def start_traffic(self, test_config):
        """ Start traffic based on provided test configuration file """

        return self.start_traffic_flow.start_traffic(test_config=test_config)

    def stop_traffic(self):
        """ Stop traffic """

        return self.stop_traffic_flow.stop_traffic()

    def get_results(self):
        """ Get results """

        return self.get_results_flow.get_results()