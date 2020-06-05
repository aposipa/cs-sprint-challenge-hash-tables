# Your code here

import re

# def finder(files, queries):
#     #files is an array of paths
#     #queries is an array of filenames

#     file_dict = {}


#     for path in files:
#         for filename in queries:
#             if filename in path:
#                 file_dict[path] = filename
#                 break

#     # result = [val for key, val in test_dict.items() if search_key in key]
#     result = []
#     for path in file_dict:
#         result.append(path)
#     #return all the filepaths that match a query
#     return result

def finder(files, queries):
    q_str = ', '.join(queries)

    path_dict = {}
    result = []
    for path in files:
        path_arr = path.split('/')
        path_dict[path] = path_arr[-1]

    for path in path_dict:
        if path_dict[path] in q_str:
            result.append(path)

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
