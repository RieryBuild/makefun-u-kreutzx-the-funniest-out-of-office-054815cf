"""make.fun entry: "The Funniest Out-of-Office".

Writes a one-line out-of-office reply (117 chars) to $MAKEFUN_OUTPUT_DIR/entry.txt:
a real, settable OOO line whose twist is that the inbox has been left in the
care of the sender's future self — who is already disappointed in both of them.
The file is written with no trailing newline, per the bounty gate.
"""

import os

ENTRY = "I'm out of office until Monday. My inbox is in the care of my future self, who is already disappointed in both of us."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)
with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
