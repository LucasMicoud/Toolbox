import argparse

from install_scripts.crypto import install_crypto
from install_scripts.forensics import install_forensics
from install_scripts.reverse import install_reverse

def install_all():
    print("Installing all packages...")
    install_basics()
    install_crypto()
    install_forensics()
    install_reverse()


def install_basics():
    print("Installing basic packages...")

def list_packages():
    print("Listing installed packages...")

def main():
    parser = argparse.ArgumentParser(description="Package Installation and Listing Script")
    subparsers = parser.add_subparsers(title="Actions", dest="action")

    install_parser = subparsers.add_parser("install", help="Install packages")
    install_parser.add_argument("package", choices=["basics", "crypto", "forensics", "reverse"], help="Package to install")

    list_parser = subparsers.add_parser("list", help="List available packages")

    args = parser.parse_args()

    if args.action == "install":
        if args.package == "all":
            install_all()
        elif args.package == "basics":
            install_basics()
        elif args.package == "crypto":
            install_crypto()
        elif args.package == "forensics":
            install_forensics()
        elif args.package == "reverse":
            install_reverse()
    elif args.action == "list":
        list_packages()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
