#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tak_mission_api.py from https://github.com/sgofferj/takserver-api-python
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


"""home-api - https://docs.tak.gov/api/takserver#tag/mission-api"""

import asyncio


async def get_mission(self, name):
    """Returns a mission"""
    path = f"/Marti/api/missions/{name}"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


async def get_mission_role(self, name):
    """Returns role in the mission"""
    path = f"/Marti/api/missions/{name}/role"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


async def get_mission_subscriptions(self, name):
    """Returns subscribtions to the mission"""
    path = f"/Marti/api/missions/{name}/subscriptions"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


async def get_mission_subscription_roles(self, name):
    """Returns subscribtions to the mission"""
    path = f"/Marti/api/missions/{name}/subscriptions/roles"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("get", url, headers=headers)
    return s, r


async def create_mission(
    self, name, creatorUid, group="", defaultrole="", classification=""
):
    """Creates a mission"""
    path = f"/Marti/api/missions/{name}?creatorUid={creatorUid}"
    if group != "":
        path += f"&group={group}"
    if defaultrole != "":
        path += f"&defaultRole={defaultrole}"
    if classification != "":
        path += f"&classification={classification}"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("put", url, headers=headers)
    return s, r


async def create_mission_subscription(
    self, name, uid, topic="", password="", secago="", start="", end=""
):
    """Creates a mission subscription"""
    path = f"/Marti/api/missions/{name}/subscription?uid={uid}"
    if topic != "":
        path += f"&topic={topic}"
    if password != "":
        path += f"&password={password}"
    if secago != "":
        path += f"&secago={secago}"
    if start != "":
        path += f"&start={start}"
    if end != "":
        path += f"&end={end}"
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("put", url, headers=headers)
    return s, r


async def set_mission_role(self, name, clientUid, username, role, token):
    """Sets the role for a subscriber"""
    path = f"/Marti/api/missions/{name}/role?clientUid={clientUid}&username={username}&role={role}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    s, r = await self.request("put", url, headers=headers)
    return s, r


async def add_mission_content(self, name, uids, MY_UID, token):
    path = f"/Marti/api/missions/{name}/contents?creatorUid={MY_UID}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.api_base_url + path
    headers = {"Content-Type": "application/json"}
    data = {"uids": uids}
    s, r = await self.request("put", url, headers=headers, json=data)
    return s, r


async def remove_mission_content(self, name, uid, MY_UID, token):
    path = f"/Marti/api/missions/{name}/contents?creatorUid={MY_UID}&uid={uid}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.api_base_url + path
    s, r = await self.request("delete", url, headers=headers)
    return s, r
