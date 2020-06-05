# Your code here

import re

def finder(files, queries):
    #files is an array of paths
    #queries is an array of filenames

    file_dict = {}

    # for filename in queries:
    #     if filename not in file_dict:
    #         file_dict[filename] = len(filename)

    for path in files:
        if path not in file_dict:
            file_dict[path] = None

    result = []
    for filename in queries:
        for path in files:
            if filename in path:
                result.append(path)

    



    #return all the filepaths that match a query
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
