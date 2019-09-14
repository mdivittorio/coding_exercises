import math


def is_bad_version(version: int):
    return version > 7


def first_bad_version(versions: list) -> int:
    if versions:
        for version in versions:
            if is_bad_version(version):
                return version
    return -1


def first_bad_version_improved(versions: list) -> int:
    if not versions:
        return -1
    mid = math.ceil(len(versions)/2)-1
    if is_bad_version(versions[mid]):
        if mid == 0:
            return versions[mid]
        else:
            return first_bad_version_improved(versions[:mid+1])
    elif len(versions) == 1:
        return -1
    else:
        return first_bad_version_improved(versions[mid+1:])
