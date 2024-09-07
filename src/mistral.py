import re
import json
import requests


def __call__(data: dict):
    url = "http://127.0.0.1:11112/api/generate"

    payload = json.dumps(data)
    headers = {
        'Content-Type': 'application/json'
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    text = re.sub(r"\}\s*\{", "},\n{", response.text)
    return json.loads(f"[{text}]")


def mistral(msg: str, **kwargs) -> str:
    assert type(msg) is str
    data = {
        "model": "mistral",
        "prompt": msg
    }
    for key in kwargs:
        assert key not in data
        data[key] = kwargs[key]
    response: str = "".join([r.get("response", "") for r in __call__(data)])
    response = response.strip()
    return response