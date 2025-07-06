# takserver-api-python

Helper class for talking to the (tak.gov) TAK server API.

&copy;2025 Stefan Gofferje

License: GPL V3

**WARNING: Not for production! Still developing and testing!**

## Init
`myserver = takserver(host,certificate,key)`

**Example:**

`myserver = takserver("localhost","server.pem","server.key")`

Creates an instance of takserver.

## Functions

* `myserver.listGroups()`
Returns all groups on the server.

* `myserver.groupExists(group)`
Returns True if group exists, otherwise returns False.

* `myserver.listUsers()`
Returns all users on the server.

* `myserver.userExists(user)`
Returns True if user exists, otherwise returns False.

* `myserver.createUser(username,password,grouplistBoth,grouplistIn,grouplistOut)`
Creates a new user on the server, returns the result of the API call.

* `myserver.isAdmin()`
Returns True if the configured certificate has admin rights on the server, otherwise returns False
