# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from rally import consts
from rally.plugins.openstack import scenario
from rally.plugins.openstack.scenarios.monasca import utils as monascautils
from rally.task import validation


"""Scenarios for monasca Metrics API."""


@validation.add("required_services",
                services=[consts.Service.MONASCA])
@validation.add("required_platform", platform="openstack", users=True)
@scenario.configure(name="MonascaMetrics.list_metrics", platform="openstack")
class ListMetrics(monascautils.MonascaScenario):

    def run(self, **kwargs):
        """Fetch user's metrics.

        :param kwargs: optional arguments for list query:
               name, dimensions, start_time, etc
        """
        self._list_metrics(**kwargs)