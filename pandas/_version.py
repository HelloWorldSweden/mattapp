
# This file was generated by 'versioneer.py' (0.15) from
# revision-control system data, or from the parent directory name of an
# unpacked source archive. Distribution tarballs contain a pre-generated copy
# of this file.

from warnings import catch_warnings
with catch_warnings(record=True):
    import json
import sys

version_json = '''
{
 "dirty": false,
 "error": null,
 "full-revisionid": "a00154dcfe5057cb3fd86653172e74b6893e337d",
 "version": "0.22.0"
}
'''  # END VERSION_JSON


def get_versions():
    return json.loads(version_json)
