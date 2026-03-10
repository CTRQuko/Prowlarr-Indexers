import json
import pathlib

import jsonschema
import yaml

schema_path = pathlib.Path(r"c:\homelab\docker\prowlarr\Prowlarr-Indexers\v9-schema.json")
file_path = pathlib.Path(r"c:\homelab\docker\torrentio.yml")

data = yaml.safe_load(file_path.read_text())
schema = json.loads(schema_path.read_text())

try:
    jsonschema.validate(instance=data, schema=schema)
    print('VALID')
except jsonschema.exceptions.ValidationError as e:
    print('INVALID')
    print(e.message)
    print('path:', list(e.path))
    print('schema_path:', list(e.schema_path))
    raise
