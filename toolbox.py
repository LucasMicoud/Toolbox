import argparse

from crypto import install_crypto

def install_all():
    print("Installing all packages...")
    install_basics()
    install_crypto()
    install_forensic()


def install_forensic():
    print("Installing forensic packages...")
    # Add your forensic package installation code here

def install_basics():
    print("Installing basic packages...")
    # Add your basic package installation code here

def list_packages():
    print("Listing installed packages...")
    # Add your code to list the installed packages here

def main():
    parser = argparse.ArgumentParser(description="Package Installation and Listing Script")
    subparsers = parser.add_subparsers(title="Actions", dest="action")

    install_parser = subparsers.add_parser("install", help="Install packages")
    install_parser.add_argument("package", choices=["basics", "crypto", "forensic"], help="Package to install")

    list_parser = subparsers.add_parser("list", help="List available packages")

    args = parser.parse_args()

    if args.action == "install":
        if args.package == "all":
            install_all()
        elif args.package == "basics":
            install_basics()
        elif args.package == "crypto":
            install_crypto()
        elif args.package == "forensic":
            install_forensic()
    elif args.action == "list":
        list_packages()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
