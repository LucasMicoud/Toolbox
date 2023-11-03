import os
import subprocess
import shutil

from install_scripts.utils import install_requirements

package_folder = "Crypto"

crypto_requirements = [
    "libssl-dev",
    "openssl",
]

def install_john():
    try:
        # Clone repository
        if os.path.exists(f"{package_folder}/john"):
            shutil.rmtree(f"{package_folder}/john")
        subprocess.check_call(["git", "clone", "https://github.com/openwall/john", f"{package_folder}/john"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # Build
        os.chdir(f"{package_folder}/john/src")
        subprocess.check_call(["./configure"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        subprocess.check_call(["make"],
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        # Remove sources
        os.chdir("../../..")
        try:
            shutil.rmtree(f"{package_folder}/john/src")  # This removes a folder and its contents
        except OSError as e:
            print(f"Error removing john sources : {e}")
        print("Package installed successfully : john")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package john: {e}")


def install_crypto():
    print("Installing crypto requirements...")
    install_requirements(crypto_requirements)
    print("Installing crypto packages...")
    if not os.path.exists(package_folder):
        os.mkdir(package_folder)
    install_john()

