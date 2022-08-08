import urllib.request
import subprocess


githubURL = "https://raw.githubusercontent.com/Tiller431/League-Bot-VM-Manager/main/"

LatestVersionURL = githubURL + "version"
newSctiptURL = githubURL + "dist/vm.exe"

try:
    with open("version", "r") as f:
        version = f.read().strip()
except:
    version = "0.0.0"

try:
    with urllib.request.urlopen(LatestVersionURL) as response:
        latestVersion = response.read().decode('utf-8')
        if latestVersion == version:
            print("You are up to date!")
        else:
            print("You are not up to date!")
            print("Downloading new version...")
            with urllib.request.urlopen(newSctiptURL) as response:

                newScript = response.read()

                #write new exe
                with open("vm.exe", "wb") as f:
                    f.write(newScript)

                #update version file
                with open("version", "w") as f:
                    f.write(latestVersion)            
                print("Done updating!")

except Exception as e:
    print("Error checking for update: " + str(e))