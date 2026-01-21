#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tak_file_user_account_management_api.py from https://github.com/sgofferj/takserver-api-python
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


"""file-user-account-management-api - https://docs.tak.gov/api/takserver#tag/file-user-account-management-api"""

import asyncio


async def create_or_update_file_user(
    self,
    username,
    password,
    group_list_both=None,
    group_list_in=None,
    group_list_out=None,
):
    """Create or update a user on the server"""
    path = "/user-management/api/new-user"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    data = {"username": username, "password": password}
    if group_list_in != None:
        data.update({"groupListIN": group_list_in})
    if group_list_out != None:
        data.update({"groupListOUT": group_list_out})
    if group_list_both != None:
        data.update({"groupList": group_list_both})
    s, r = await self.request("post", url, headers=headers, json=data)
    return s, r


async def get_all_users(self):
    """Returns a list of all users on the server"""
    path = "/user-management/api/list-users"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


async def get_all_group_names(self):
    """Returns a list of all groups on the server"""
    path = "/user-management/api/list-groupnames"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


def user_exists(self, user) -> bool:
    """Check if a user exists on the server"""
    r = self.get_all_users()
    g = next((item for item in r if item["username"] == user), None)
    if g:
        return True
    else:
        return False


def group_exists(self, group) -> bool:
    """Check if a group exists on the server"""
    r = self.get_all_group_names()
    g = next((item for item in r if item["groupname"] == group), None)
    if g:
        return True
    else:
        return False
