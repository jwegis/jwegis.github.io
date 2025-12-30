import subprocess
import sys
import os
from format import format_site

def build():
    print("Building site with Zensical...")
    try:
        # Run zensical build. checking=True raises CalledProcessError on non-zero exit
        subprocess.run(["uv", "run", "zensical", "build"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: Build failed with exit code {e.returncode}")
        sys.exit(e.returncode)

    print("Build successful. Running HTML formatter...")

    # Run the formatter
    try:
        # Defaults to "site" directory
        format_site("site")
    except Exception as e:
        print(f"Error during formatting: {e}")
        sys.exit(1)

    print("Build and formatting complete.")

if __name__ == "__main__":
    build()
