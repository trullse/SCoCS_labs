from storage import Storage


stor = Storage()
stor.add("13")
stor.add(["something", "anything"])
print(stor.list())
print(stor.grep(r"thing"))
stor.remove("something")
print(stor.list())
print(stor.find(["13", "something"]))
