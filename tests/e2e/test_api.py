import uuid
import pytest
import requests

from cyclecomposition import config


def random_suffix() -> str:
    return uuid.uuid4().hex[:6]


def random_cycleref(name: str = "") -> str:
    return f"cycle-{name}-{random_suffix()}"


@pytest.mark.usefixtures("restart_api")
def test_post_to_add_cycle() -> None:
    url = config.get_api_url()
    ref: str = random_cycleref("mycycle")
    print("Ref: " + ref)
    respond = requests.post(f"{url}/add_cycle", json={"ref": ref}, timeout=500)
    assert respond.status_code == 201
