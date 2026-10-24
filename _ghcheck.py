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


me, _ = api("/user")
print("user:", me.get("login"))
for name in ("local-comfyui-shorts",):
    d, code = api(f"/repos/{user}/{name}")
    print(name, code, d.get("html_url"), "private" if d.get("private") else "public")
