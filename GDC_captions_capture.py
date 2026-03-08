import requests
import time
import sys

max_range = 10 # force limit max number
join_every = 2

# the full vtt input look like this
# "https://cdn-a.blazestreaming.com/out/v1/f72822c3f77b451dae57d181272eac23/38549d9a185b445888c6fbc2e2e792e9/8ab8ab8373024769a1c46afeb024f7a4/cbf0efaa7e8742959383a02621409d7c/index_4_0_33.vtt"
# 
# we'll turn format from A to B
# A: ".../index_4_0_33.vtt"
# B: ".../index_4_0_%d.vtt"

template = "_".join(sys.argv[1].split("_", 3)[:3]) + "_%d.vtt"
file_content = ""
capture_404 = 0
i = 0

start_time = time.time()  # Start time before the code block
while True:
    if capture_404 > 3:
        break
    if i > 1000:
        print ("Reach max_range: 1000")
        break

    r = requests.get(template % i)
    if r.status_code == 404:
        print ("status code: 404")
        capture_404 += 1

    content = r.content.decode("utf-8").replace("\\n\\n", "\n").strip() + "\n\n"
    lines = content.split("\n\n")

    for index, line in enumerate(lines):
        # index > 0: remove the header
        # index != len(lines)-2 : remove the duplicated lines
        # index: make sure the line has content
        if index > 0 and line and index != len(lines)-2:
            file_content += line+"\n\n"
    print ("chunk {0}".format(i))
    i += 1

with open("caption.txt", 'w') as f:
    f.write(file_content)

end_time = time.time()  # Time after the code block
time_in_seconds = end_time - start_time
time_in_minutes = time_in_seconds / 60  # Convert to minutes

print ("FINISHED, Time cost: {0} minutes".format(time_in_minutes))