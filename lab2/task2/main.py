from storage import Storage


stor = Storage()
stor.switch_user("username")
stor.add("something")
stor.add(["anything", "any"])
print(stor.list())
print(stor.find("any"))
print(stor.find(["something", "anything"]))
print(stor.grep("thing"))
stor.remove("anything")
print(stor.list())
stor.save_changes()
stor.switch_user("aliaksei")
print(stor.list())
stor.switch_user("username")
stor.load_container()
print(stor.list())
