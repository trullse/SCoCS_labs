from storage import Storage
from storageCLI import StorageCLI


storage = StorageCLI()
command = str(input())
while storage.command_handler(command):
    command = str(input())
