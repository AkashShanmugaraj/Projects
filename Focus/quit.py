import subprocess

while True:
    apps = ['msedge.exe', 'brave.exe', 'Nox.exe', 'Chrome.exe', 'Code.exe']
    for i in range(0,len(apps)):
        proc = subprocess.run(["TASKKILL", "/F", "/IM", apps[i]], stderr=subprocess.PIPE)
        