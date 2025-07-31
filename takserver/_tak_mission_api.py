#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# _tak_mission_api.py from https://github.com/sgofferj/takserver-api-python
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

import requests as req

req.packages.urllib3.disable_warnings()


def getMission(self, name):
    """Returns a mission"""
    path = f"/Marti/api/missions/{name}"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def getMissionRole(self, name):
    """Returns role in the mission"""
    path = f"/Marti/api/missions/{name}/role"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def getMissionSubscriptions(self, name):
    """Returns subscribtions to the mission"""
    path = f"/Marti/api/missions/{name}/subscriptions"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def getMissionSubscriptionRoles(self, name):
    """Returns subscribtions to the mission"""
    path = f"/Marti/api/missions/{name}/subscriptions/roles"
    url = self.apiBaseURL + path
    r = req.get(url, cert=self.crt, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def createMission(self, name, creatorUid, group="", defaultrole="", classification=""):
    """Creates a mission"""
    path = f"/Marti/api/missions/{name}?creatorUid={creatorUid}"
    if group != "":
        path += f"&group={group}"
    if defaultrole != "":
        path += f"&defaultRole={defaultrole}"
    if classification != "":
        path += f"&classification={classification}"
    url = self.apiBaseURL + path
    r = req.put(url, cert=self.crt, verify=False)
    if r.status_code != 201:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def createMissionSubscription(
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
    url = self.apiBaseURL + path
    r = req.put(url, cert=self.crt, verify=False)
    if r.status_code != 201:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def setMissionRole(self, name, clientUid, username, role, token):
    """Sets the role for a subscriber"""
    path = f"/Marti/api/missions/{name}/role?clientUid={clientUid}&username={username}&role={role}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.apiBaseURL + path
    r = req.put(url, cert=self.crt, headers=headers, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def addMissionContent(self, name, uids, MY_UID, token):
    path = f"/Marti/api/missions/{name}/contents?creatorUid={MY_UID}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.apiBaseURL + path
    data = {"uids": uids}
    r = req.put(url, json=data, cert=self.crt, headers=headers, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()


def removeMissionContent(self, name, uid, MY_UID, token):
    path = f"/Marti/api/missions/{name}/contents?creatorUid={MY_UID}&uid={uid}"
    headers = {"Authorization": f"Bearer {token}"}
    url = self.apiBaseURL + path
    r = req.delete(url, cert=self.crt, headers=headers, verify=False)
    if r.status_code != 200:
        return r.status_code, r.text
    else:
        return r.status_code, r.json()
