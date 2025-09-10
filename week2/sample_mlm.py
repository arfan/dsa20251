class Member:
    def __init__(self, name, member1=None, member2=None):
        self.name = name    
        self.member1 = member1
        self.member2 = member2

    def print_all(self, depth=0):
        print("    "*depth, self.name)
        if self.member1 is not None:
            # print("member 1: ", self.member1.name)
            self.member1.print_all(depth+1)
        if self.member2 is not None:
            # print("member 2: ", self.member2.name)
            self.member2.print_all(depth+1)


arfan = Member("Arfan")
rifky = Member("Rifky")
susi = Member("Susi")
hafiz = Member("Hafiz")
ziaul = Member("Ziaul")

arfan.member1 = rifky
arfan.member2 = susi
susi.member1 = hafiz
hafiz.member1 = ziaul

arfan.print_all()