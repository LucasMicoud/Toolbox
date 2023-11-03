import os
import subprocess
import shutil

from install_scripts.utils import install_requirements

package_folder = "Forensics"

forensics_requirements = [
    "python3-pip",

]

def install_volatility3():
    try:
        # Clone repository
        if os.path.exists(f"{package_folder}/volatility3"):
            shutil.rmtree(f"{package_folder}/volatility3")
        subprocess.check_call(["git", "clone", "https://github.com/volatilityfoundation/volatility3", f"{package_folder}/volatility3"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # Build
        subprocess.check_call(["python3", "-m", "pip", "install", "-r", f"{package_folder}/volatility3/requirements.txt"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        os.chdir(f"{package_folder}/volatility3")
        subprocess.check_call(["python3", "setup.py", "build"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Package installed successfully : volatility3")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package volatility3: {e}")

def install_forensics():
    print("Installing forensics requirements...")
    install_requirements(forensics_requirements)
    print("Installing forensics packages...")
    if not os.path.exists(package_folder):
        os.mkdir(package_folder)
    install_volatility3()