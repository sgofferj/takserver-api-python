# takserver-api-python

Helper module for talking to the (tak.gov) TAK server API.

&copy;2025 Stefan Gofferje

License: GPL V3

**WARNING WARNING WARNING**

This is not for production! I am using this project to learn Python classes, modules and packaging
and do something useful at the same time. I primarily uploaded it to Github so others can review
and comment on it.

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
