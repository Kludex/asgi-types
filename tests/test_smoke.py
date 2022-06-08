import inspect

import asgi_types


def test_smoke() -> None:
    assert inspect.ismodule(asgi_types)
