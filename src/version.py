__version__ = "0.0.0"
__dev_version__ = "0.0.0"
__stable_version__ = "0.0.0"


def digital_version(version: str):
    return tuple(map(int, version.split(".")))
