# takserver-api-python

Helper module for talking to the (tak.gov) TAK server API.

&copy;2025 Stefan Gofferje

License: GPL V3

> [!CAUTION]
> I have changed all function names from camelCase to snake_case to be more compliant with Python style guides.
> Please check the Wiki for the new function names. Additionally everything is using asyncio and aiohttp now.

**Example:**

```python

import takserver as ts
import asyncio

async def main()
    myserver = ts.server("localhost","server.pem","server.key")
    if await myserver.is_admin():
      print(await myserver.get_all_users())
      await myserver.close()

asyncio.run(main())

```

## Documentation

Documentation can be found in the Wiki.
