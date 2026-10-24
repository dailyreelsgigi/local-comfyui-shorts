import json, subprocess, time, urllib.request

raw = subprocess.run(["git", "credential", "fill"], input="protocol=https\nhost=github.com\n\n",
                     capture_output=True, text=True).stdout
c = dict(l.split("=", 1) for l in raw.strip().splitlines() if "=" in l)
tok, user = c["password"], c["username"]
NAME = "local-comfyui-shorts"


def api(path, method="GET", payload=None):
    data = json.dumps(payload).encode() if payload is not None else None
    r = urllib.request.Request("https://api.github.com" + path, data=data, method=method, headers={
        "Authorization": "Bearer " + tok, "Accept": "application/vnd.github+json",
        "Content-Type": "application/json"})
    try:
        return json.load(urllib.request.urlopen(r, timeout=25)), 200
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:300]
        return {"error": body}, e.code


repo, code = api(f"/repos/{user}/{NAME}")
if code == 404:
    repo, code = api("/user/repos", "POST", {
        "name": NAME, "private": False, "has_issues": True, "has_wiki": False,
        "description": "Local ComfyUI Cantonese AI short EP1 + workflow notes"})
print("repo:", code, repo.get("html_url") or repo.get("error"))

if code in (200, 201):
    subprocess.run(["git", "remote", "remove", "origin"], capture_output=True)
    subprocess.run(["git", "remote", "add", "origin", f"https://github.com/{user}/{NAME}.git"],
                   capture_output=True)
    p = subprocess.run(["git", "push", "-u", "origin", "main"], capture_output=True, text=True,
                       env={"GIT_TERMINAL_PROMPT": "0", "PATH": "/c/Program Files/Git/bin:/usr/bin:/bin"})
    print("push:", p.returncode, (p.stderr or p.stdout).strip().splitlines()[-1][:160])

    pages, pcode = api(f"/repos/{user}/{NAME}/pages")
    if pcode == 404:
        pages, pcode = api(f"/repos/{user}/{NAME}/pages", "POST", {
            "source": {"branch": "main", "path": "/"}})
    print("pages:", pcode, pages.get("html_url") or pages.get("error"))
