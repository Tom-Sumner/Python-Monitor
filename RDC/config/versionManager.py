def compare_versions(version1, version2):
    # Split the versions into their components
    v1 = list(map(int, version1.split(".")))
    v2 = list(map(int, version2.split(".")))

    # Compare each component of the versions
    for i in range(len(v1)):
        if v1[i] > v2[i]:
            return version1
        elif v1[i] < v2[i]:
            return version2

    # If all components are equal, the versions are the same
    return version1