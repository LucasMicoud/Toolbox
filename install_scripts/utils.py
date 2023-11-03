import subprocess

def install_requirements(requirements):
    try:
        subprocess.check_call(["sudo", "apt", "install", "-y"] + requirements,
            stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Requirements installed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error installing packages: {e}")
    except FileNotFoundError:
        print("apt command not found. Make sure you are running this on a Debian/Ubuntu-based system.")