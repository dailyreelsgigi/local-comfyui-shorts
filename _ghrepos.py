import json, subprocess, urllib.request

raw = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                     capture_output=True, text=True).stdout
c = dict(l.split("=", 1) for l in raw.strip().splitlines() if "=" in l)
tok, user = c["password"], c["username"]


def api(path):
    r = urllib.request.Request("https://api.github.com" + path, headers={
        "Authorization": "Bearer " + tok, "Accept": "application/vnd.github+json"})
    try:
        return json.load(urllib.request.urlopen(r, timeout=20)), 200
    except urllib.error.HTTPError as e:
        return {}, e.code


repos, code = api("/user/repos?sort=created&direction=desc&per_page=10")
print("status", code)
for r in repos:
    print(r["name"], r["updated_at"], "private" if r["private"] else "public", r["default_branch"])
