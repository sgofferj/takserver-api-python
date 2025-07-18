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
print(myserver.isAdmin())
print(myserver.listUsers())

```

## Functions

- `myserver.isAdmin()`
  Returns True if the configured certificate has admin rights on the server, otherwise returns False
  Should be the first thing to call before anything else to prevent errors.

- `myserver.listGroups()`
  Returns all groups on the server.

- `myserver.groupExists(group)`
  Returns True if group exists, otherwise returns False.

- `myserver.listUsers()`
  Returns all users on the server.

- `myserver.userExists(user)`
  Returns True if user exists, otherwise returns False.

- `myserver.createUser(username,password,grouplistBoth,grouplistIn,grouplistOut)`
  Creates a new user on the server, returns the result of the API call.
