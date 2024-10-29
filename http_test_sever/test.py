import json
from urllib.request import Request, urlopen

if __name__ == "__main__":
    data = {"data": {"key": "value"}}

    request = Request(
        "http://localhost:3000/",
        headers={"Content-Type": "application/json"},
        data=json.dumps(data).encode("utf-8"),
    )
    with urlopen(request, timeout=1) as response:
        response_data = json.loads(response.read())
        print(response_data)
