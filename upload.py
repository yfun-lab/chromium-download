# Upload File

import os
os.system("curl -sL https://git.io/file-transfer | sh ")
a = os.popen("./transfer cat Win.zip")
print(a.read())
