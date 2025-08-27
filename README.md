# takserver-api-python

Helper module for talking to the (tak.gov) TAK server API.

&copy;2025 Stefan Gofferje

License: GPL V3

> [!CAUTION]
> This is not for production! I am still working on the library on a daily basis and things can change.
> However, I have tested all functions before pushing to GitHub, so they _should_ work.
> **USE AT YOUR OWN RISK**

**Example:**

```python

import takserver as ts

myserver = ts.server("localhost","server.pem","server.key")
if myserver.isAdmin():
  print(myserver.getAllUsers())

```

## Documentation

Documentation can be found in the Wiki.
