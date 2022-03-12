# Upload File

import os
os.system("curl -sL https://git.io/file-transfer | sh ")
a = os.popen("./transfer lit Win.zip --no-progress")
print(a.read())
