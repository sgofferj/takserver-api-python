#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _tak_users.py from https://github.com/sgofferj/takserver-api-python
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


"""file-user-account-management-api - https://docs.tak.gov/api/takserver#tag/file-user-account-management-api/operation/createOrUpdateFileUser"""

import requests as req

req.packages.urllib3.disable_warnings()


def createOrUpdateFileUser(
    self,
    username,
    password,
    grouplistBoth=None,
    grouplistIn=None,
    grouplistOut=None,
):
    """Create a new user on the server"""
    path = "/user-management/api/new-user"
    url = self.server + path
    headers = {"Content-Type": "application/json"}
    data = {"username": username, "password": password}
    if grouplistIn != None:
        data.update({"groupListIN": grouplistIn})
    if grouplistOut != None:
        data.update({"groupListOUT": grouplistOut})
    if grouplistBoth != None:
        data.update({"groupList": grouplistBoth})
    r = req.post(url, headers=headers, json=data, cert=self.crt, verify=False)
    return r


def getAllUsers(self):
    """Returns a list of all users on the server"""
    path = "/user-management/api/list-users"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    return r.json()


def getAllGroupNames(self):
    """Returns a list of all groups on the server"""
    path = "/user-management/api/list-groupnames"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    return r.json()


def userExists(self, user):
    """Check if a user exists on the server"""
    r = self.listUsers()
    g = next((item for item in r if item["username"] == user), None)
    if g:
        return True
    else:
        return False


def groupExists(self, group):
    """Check if a group exists on the server"""
    r = self.listGroups()
    g = next((item for item in r if item["groupname"] == group), None)
    if g:
        return True
    else:
        return False
