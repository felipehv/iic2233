class Folder():

    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.subfolders = []
        
    @property
    def path(self):
        if self.parent == None:
            return ""
        return self.parent.path + "/{}".format(self.name)

