#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _tak_home_api.py from https://github.com/sgofferj/takserver-api-python
#
# Copyright Stefan Gofferje
#
# Licensed under the Gnu General Public License Version 3 or higher (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at https://www.gnu.org/licenses/gpl-3.0.en.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either expressed or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#


"""home-api - https://docs.tak.gov/api/takserver#tag/home-api"""

import requests as req

req.packages.urllib3.disable_warnings()


def isAdmin(self):
    """Check if the configured certificate has admin rights on the server"""
    path = "/Marti/api/util/isAdmin"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    if r.text == "true":
        return True
    else:
        return False
