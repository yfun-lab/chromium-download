# Upload File
import os
# Install Transfer
os.system("curl -sL https://git.io/file-transfer | sh ")

# LitterBox
# lit = {}
# lit["win"] = os.popen("./transfer lit Win.zip --no-progress").read()
# lit["win_x64"] = os.popen("./transfer lit Win_x64.zip --no-progress").read()
# lit["mac"] = os.popen("./transfer lit Mac.zip --no-progress").read()
# lit["mac_arm"] = os.popen("./transfer lit Mac_Arm.zip --no-progress").read()
# lit["linux"] = os.popen("./transfer lit Linux.zip --no-progress").read()
# lit["linux_x64"] = os.popen("./transfer lit Linux_x64.zip --no-progress").read()
# lit["chromiumos"] = os.popen("./transfer lit Linux_ChromiumOS_Full.zip --no-progress").read()
# lit["android"] = os.popen("./transfer lit Android.zip --no-progress").read()


# CatBox
# cat = {}
# cat["win"] = os.popen("./transfer cat Win.zip --no-progress").read()
# cat["win_x64"] = os.popen("./transfer cat Win_x64.zip --no-progress").read()
# cat["mac"] = os.popen("./transfer cat Mac.zip --no-progress").read()
# cat["mac_arm"] = os.popen("./transfer cat Mac_Arm.zip --no-progress").read()
# cat["linux"] = os.popen("./transfer cat Linux.zip --no-progress").read()
# cat["linux_x64"] = os.popen("./transfer cat Linux_x64.zip --no-progress").read()
# cat["chromiumos"] = os.popen("./transfer cat Linux_ChromiumOS_Full.zip --no-progress").read()
# cat["android"] = os.popen("./transfer cat Android.zip --no-progress").read()

# Null
# null = {}
# null["win"] = os.popen("./transfer null Win.zip --no-progress").read()
# null["win_x64"] = os.popen("./transfer null Win_x64.zip --no-progress").read()
# null["mac"] = os.popen("./transfer null Mac.zip --no-progress").read()
# null["mac_arm"] = os.popen("./transfer null Mac_Arm.zip --no-progress").read()
# null["linux"] = os.popen("./transfer null Linux.zip --no-progress").read()
# null["linux_x64"] = os.popen("./transfer null Linux_x64.zip --no-progress").read()
# null["chromiumos"] = os.popen("./transfer null Linux_ChromiumOS_Full.zip --no-progress").read()
# null["android"] = os.popen("./transfer null Android.zip --no-progress").read()

# Transfer.sh

trs = {}
trs["win"] = os.popen("./transfer trs Win.zip --no-progress").read()
trs["win_x64"] = os.popen("./transfer trs Win_x64.zip --no-progress").read()
trs["mac"] = os.popen("./transfer trs Mac.zip --no-progress").read()
trs["mac_arm"] = os.popen("./transfer trs Mac_Arm.zip --no-progress").read()
trs["linux"] = os.popen("./transfer trs Linux.zip --no-progress").read()
trs["linux_x64"] = os.popen("./transfer trs Linux_x64.zip --no-progress").read()
trs["chromiumos"] = os.popen("./transfer trs Linux_ChromiumOS_Full.zip --no-progress").read()
trs["android"] = os.popen("./transfer trs Android.zip --no-progress").read()

with open('./README_TEMPLATE.md', 'r') as f:
    markdown = f.read()
#     for k, v in lit.items():
#         markdown.replace("@{lit_"+k+"}", v)
#     for k, v in cat.items():
#         markdown.replace("@{cat_"+k+"}", v)
    for k, v in trs.items():
        markdown.replace("@{trs_"+k+"}", v)

with open('./README.md', 'w') as f:
    f.write(markdown)
