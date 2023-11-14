import os
import subprocess
import shutil

from install_scripts.utils import install_requirements

package_folder = "Reverse"

reverse_requirements = [

]

def install_cutter():
    try:
        # Clone repository
        if os.path.exists(f"{package_folder}/cutter"):
            os.remove(f"{package_folder}/cutter")
        subprocess.check_call(["wget", "https://github.com/rizinorg/cutter/releases/download/v2.3.2/Cutter-v2.3.2-Linux-x86_64.AppImage", "-O", f"./{package_folder}/cutter"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.check_call(["chmod", "+x", f"{package_folder}/cutter"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Package installed successfully : cutter")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package cutter: {e}")

def install_reverse():
    print("Installing reverse requirements...")
    install_requirements(reverse_requirements)
    print("Installing reverse packages...")
    if not os.path.exists(package_folder):
        os.mkdir(package_folder)
    install_cutter()