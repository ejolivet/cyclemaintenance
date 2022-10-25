import time
from pathlib import Path

import pytest
import requests

from requests.exceptions import RequestException

from cyclecomposition import config


def wait_for_webapp_to_come_up() -> requests.Response:
    deadline = time.time() + 10
    url = config.get_api_url()
    while time.time() < deadline:
        try:
            return requests.get(url, timeout=500)
        except RequestException:
            time.sleep(0.5)
    pytest.fail("API never came up")


@pytest.fixture
def restart_api() -> None:
    (Path(__file__).parent / "../app/djangoproject/manage.py").touch()
    time.sleep(0.5)
    wait_for_webapp_to_come_up()
