# takserver-api-python

Helper module for talking to the (tak.gov) TAK server API.

&copy;2025 Stefan Gofferje

License: GPL V3

> [!CAUTION]
> This is not for production! I am using this project to learn Python classes, modules and packaging
> and do something useful at the same time. I primarily uploaded it to Github so others can review
> and comment on it.

**Example:**

```python

import takserver as ts

myserver = ts.server("localhost","server.pem","server.key")
if myserver.isAdmin():
  print(myserver.getAllUsers())

```

## Functions

### home-api

Server documentation: [https://docs.tak.gov/api/takserver#tag/home-api](https://docs.tak.gov/api/takserver#tag/home-api)

#### API wrappers

- `server.isAdmin()`

  Returns True if the configured certificate has admin rights on the server, otherwise returns False.
  Should be the first thing to call before anything else to prevent errors.

### file-user-account-management-api

Server documentation: [https://docs.tak.gov/api/takserver#tag/file-user-account-management-api](https://docs.tak.gov/api/takserver#tag/file-user-account-management-api)

#### API wrappers

- `server.createOrUpdateFileUser(username,password,grouplistBoth,grouplistIn,grouplistOut)`

  Creates a new user on the server, returns the result of the API call.

- `server.getAllGroupNames()`

  Returns all groups on the server.

- `server.getAllUsers()`

  Returns all users on the server.

#### Helper functions

- `server.userExists(user)`

  Returns True if user exists, otherwise returns False.

- `server.groupExists(group)`

  Returns True if group exists, otherwise returns False.

### mission-api

Server documentation: [https://docs.tak.gov/api/takserver#tag/mission-api](https://docs.tak.gov/api/takserver#tag/mission-api)

#### API wrappers

- `getMission(name)`

  Returns the full mission with name `name`

- `getMissionRole(name)`

  Returns the role of the certificate user in the mission `name`

- `getMissionSubscriptions(name)`

  Returns all subscriptions for mission `name`

- `getMissionSubscriptionRoles(name)`

  Returns all roles for users subscribed to mission `name`

- `createMission(name, creatorUid, group="", defaultrole="", classification="")`

  Creates a mission. You will want to save the token in the returned data for further use.

- `createMissionSubscription(name, uid, topic="", password="", secago="", start="", end="")`

  Creates a mission subscription. You will want to save the token in the returned data for further use.

- `setMissionRole(name, clientUid, userName, role, token)`

  Sets the role for a user in mission `name`. Possible roles are: `"MISSION_OWNER"`, `"MISSION_SUBSCRIBER"`, `"MISSION_READONLY_SUBSCRIBER"`

- `addMissionContent(name, uids, creatorUid, token)`

  Adds uids to a mission. uids is a list (`[]`) of UIDs of CoTs sent to the server before the addMissionContent call. Those CoTs must be sent
  to a stream input which has archiving enabled and they must contain the attribute `<marti><dest mission="missionname"></marti>` in the detail attribute.

> [!NOTE]
> Hashes will be implemented later. It's on my list.<br>

- `removeMissionContent(name, uid, creatorUid, token)`

  Removes object `uid` from mission `name`
