# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://wafulakevin070.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0E_-XJSFBlVHXHPlQM7F4qqSCBIUwR07C3gxtMGBVVRN9xOrpVyuXaUQ4CM0M4JSPXNjqZcLu7-zykhKrqVcwW0YEgag-_0Op9UPQmhck6AKcFOYm2IXKusZaK83D-hfp7xi8XJw3LSPfQ1MKISkUAoeGTW4sjb1EY6-tFaHiXOI=A0AEDDF6"

auth = HTTPBasicAuth("wafulakevin070@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
