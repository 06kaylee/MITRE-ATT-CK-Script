import json
import urllib.request
from pathlib import Path

output_path = Path('d:\Splunk_Inputs\MITREDefs\enterprise-attack.json')

with urllib.request.urlopen("https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json") as url:
    data = json.loads(url.read().decode())
    with open(output_path, "w") as output:
        json.dump(data, output, indent = 4)

    

