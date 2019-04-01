import json
import os
import re
import sys

WHITESPACE_RE = re.compile("\s")


def count_whitespace(path):
    print("Counting whitespace in file {}".format(path))
    with open(path, "r", encoding="utf-8") as file:
        data = file.read()
    result = {}
    result["check_id"] = "whitespace"
    result["path"] = path
    result["extra"] = {}
    result["extra"]["size"] = len(data)
    result["extra"]["num_whitespace"] = len(WHITESPACE_RE.findall(data))
    return result


all_results = []
for path in sys.argv[1:]:
    all_results.append(count_whitespace(os.path.abspath(path)))

with open("/analysis/output/output.json", "w") as output:
    output.write(json.dumps({"results": all_results}, sort_keys=True, indent=4))
