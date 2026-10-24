import json, subprocess, urllib.request

raw = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                     capture_output=True, text=True).stdout
c ...[truncated]