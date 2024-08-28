class  Father():
    def skills(self):
        print("i love gardening,progammingh")


class Mother():
    def skills(self):
        print("i love gardening,cokking")


class Child(Mother , Father):
    def skills(self):
        Mother.skills(self)
        Father.skills(self)
        print("i love sport")


c=Child()
c.skills()


