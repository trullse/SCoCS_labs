from storage import Storage
from storageCLI import StorageCLI


storage = StorageCLI()
while True:
    command = str(input())
    storage.command_handler(command)
