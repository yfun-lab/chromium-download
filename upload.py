# Upload File

import os
os.system("curl -sL https://git.io/file-transfer | sh ")
a = os.popen("./transfer lit Win.zip")
print(a.read())

print(a.read().split("Download Link: ")[1])
