from python_bootstrap_package.version import get_version


def test_version():
    assert isinstance(get_version(), str)
