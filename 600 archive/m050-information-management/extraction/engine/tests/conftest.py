import socket

import pytest


@pytest.fixture(autouse=True)
def block_network(monkeypatch):
    def prohibited(*args, **kwargs):
        raise AssertionError("Gate 5 offline tests may not access the network")

    monkeypatch.setattr(socket, "create_connection", prohibited)
    monkeypatch.setattr(socket.socket, "connect", prohibited)
