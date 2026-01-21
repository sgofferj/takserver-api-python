#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# tak_class.py from https://github.com/sgofferj/takserver-api-python
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

import ssl
import aiohttp
import asyncio


class server:
    """Takserver API helper class"""

    def __init__(self, host, cert, key):
        """Initialize a server instance."""
        self.crt = (cert, key)
        self.cert = cert
        self.key = key
        self.api_base_url = f"https://{host}:8443"
        tcpconn = self.get_ssl_context()
        self.session = aiohttp.ClientSession(connector=tcpconn)

    async def close(self):
        """Close the connection"""
        await self.session.close()

    from .class_helpers import get_ssl_context, request

    from .tak_home_api import is_admin

    from .tak_file_user_account_management_api import (
        create_or_update_file_user,
        get_all_users,
        get_all_group_names,
        user_exists,
        group_exists,
    )

    from .tak_mission_api import (
        get_mission,
        get_mission_role,
        get_mission_subscriptions,
        get_mission_subscription_roles,
        create_mission,
        create_mission_subscription,
        set_mission_role,
        add_mission_content,
        remove_mission_content,
    )
