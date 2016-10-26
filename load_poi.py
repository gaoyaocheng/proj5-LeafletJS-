class Poi() :
    def __init__(self, poifile):
        self.poilist = []
        ls = open(poifile, 'r')
        for line in ls:
            if line.strip().startswith("#"):
                continue
            line = line.strip().split()
            if len(line) < 3:
                continue
            poi = []
            poi.append(line[0])
            poi.append(line[1])
            description = ""
            for i in range(len(line) - 2):
                description += line[i + 2]
                if i != len(line) - 3:
                    description += " "
            poi.append(description)
            self.poilist.append(poi)
    def as_list(self):
        return self.poilist

