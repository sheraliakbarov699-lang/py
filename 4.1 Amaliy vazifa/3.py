import subprocess
import os

cmd = "dir" if os.name == "nt" else ["ls", "-la"]

result = subprocess.run(cmd, capture_output=True, text=True)
print("Terminal buyrug'i natijasi:")
print(result.stdout)
