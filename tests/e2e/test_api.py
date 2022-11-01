import uuid
import pytest
import requests

from cyclecomposition import config


def random_suffix() -> str:
    return uuid.uuid4().hex[:6]


def random_reference(name: str = "") -> str:
    return f"reference-{name}-{random_suffix()}"


def random_marque(name: str = "") -> str:
    return f"marque-{name}-{random_suffix()}"


@pytest.mark.usefixtures("restart_api")
def test_post_to_add_component() -> None:
    url = config.get_api_url()
    ref: str = random_reference("mycycle")
    marque: str = random_marque("mymarque")
    respond = requests.post(
        f"{url}/cyclecomp/define_component_api",
        data={"reference": ref, "marque": marque},
        timeout=500,
    )
    assert respond.status_code == 201
