from storageCLI import StorageCLI


def main():
    storage = StorageCLI()
    command = str(input())
    while storage.command_handler(command):
        command = str(input())


if __name__ == '__main__':
    main()
