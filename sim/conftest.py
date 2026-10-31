import pytest


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "unverified_source: equation comes from a survey passage tagged "
        "[from abstract/standard account] or Unconfirmed",
    )
