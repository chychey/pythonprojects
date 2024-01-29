

#parent class
class Organism:
    name = "Unknown"
    species = "Unknown"
    legs = 0
    arms = 0
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: ()\nspecies: ()\nLegs: ()\nName: ()\nDNA: ()\nOrigin: ()nCarbon Based ()".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        return msg









if __name__ == "__main__":
  
