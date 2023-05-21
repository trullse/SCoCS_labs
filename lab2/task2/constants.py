ADD = "add"
REMOVE = "remove"
FIND = "find"
LIST = "list"
GREP = "grep"
SAVE = "save"
LOAD = "load"
SWITCH = "switch"
HELP = "help"
EXIT = "exit"
SAVE_PATH = "containers/"
FILE_EXTENSION = ".json"
COMMANDS_HELP = [("add <key> [key, …]", "add one or more elements to the container (if the element is already in there "
                                        "then don’t add)"),
                 ("remove <key>", "delete key from container"),
                 ("find <key> [key, …]", "check if the element is presented in the container, print each found or "
                                         "'No such elements' if nothing is"),
                 ("list", "print all elements of container"),
                 ("grep <regex>", "check the value in the container by regular expression, print each found or "
                                  "'No such elements' if nothing is"),
                 ("save/load", "save container to file/load container from file"),
                 ("switch", "switches to another user"),
                 ("help", "show all the commands"),
                 ("exit", "exit the program")]
