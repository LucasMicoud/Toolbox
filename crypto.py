import os
import subprocess

package_folder = "Crypto"

requirements = [
    "libssl-dev",
    "openssl",
]

def install_john():
    try:
        subprocess.check_call(["git", "clone", "https://github.com/openwall/john", "-o", f"{package_folder}/john"])
        os.chdir(f"{package_folder}/john/src")
        subprocess.check_call(["./configure"])
        subprocess.check_call(["make"])
        print("Package installed successfully : john")
    except subprocess.CalledProcessError as e:
        print(f"Error installing package john: {e}")
    except FileNotFoundError:
        print("apt-get command not found. Make sure you are running this on a Debian/Ubuntu-based system.")


def install_requirements():
    try:
        subprocess.check_call(["sudo", "apt", "install", "-y"] + requirements)
        print("Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
    except FileNotFoundError:
        print("apt-get command not found. Make sure you are running this on a Debian/Ubuntu-based system.")

def install_crypto():
    print("Installing crypto requirements...")
    install_requirements()
    print("Installing crypto packages...")
    os.mkdir(package_folder)

