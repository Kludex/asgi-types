from asgi_types import ASGIApplication, ASGIReceiveCallable, ASGISendCallable, Scope


def test_asgi_application() -> None:
    async def app(scope: Scope, receive: ASGIReceiveCallable, send: ASGISendCallable) -> None: ...

    def is_asgi_application(app: ASGIApplication) -> bool:
        return True

    assert is_asgi_application(app)
