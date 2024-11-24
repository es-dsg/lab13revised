# import Mammal class
from mammal import *

# create your PolarBear class that extends from the Mammal class
class PolarBear(Mammal):

 
    # Call the superclass's __init__ method and pass the required arguments. Note that we also have to pass self as an argument
  def __init__(self, domain, kingdom, phylum, class_type,name):
    Mammal.__init__(self, domain, kingdom, phylum, class_type)
    self.name = name
     # Initialize the __order, __family, __genius, __species, __vulnerability, __resilience, and __status
    
    self.order = "Carnivora"
    self.family = "Ursidae"
    self.genus = "Ursus"
    self.species = "U. maritimus"
    self.vulnerability = "Habitat specialists, rely almost entirely on the sea-ice environment."
    self.resilience = "Opportunistic eaters, prefer seals, but will feed on whale carcasses and even hunt walrus and beluga. Will prey on land animals when necessary."
    self.status = "Vulnerable"
 

  # methods for the mutators/setters for the attributes
  def set_order(self,order):
    self.order = order
  def set_family(self,family):
    self.family = family
  def set_genus(self,genus):
    self.genus = genus
  def set_species(self,species):
    self.species = species
  def set_vulnerability(self,vulnerability):
    self.vulnerability = vulnerability
  def set_resilience(self,resilience):
    self.resilience = resilience
  def set_status(self,status):
    self.status = status
  # methods for the accessors/getters for the attributes
  def get_order(self):
    return self.order
  def get_family(self):
    return self.family
  def get_genus(self):
    return self.genus
  def get_species(self):
    return self.species
  def get_vulnerability(self):
    return self.vulnerability
  def get_resilience(self):
    return self.resilience
  def get_status(self):
    return self.status 
  # method for class string
  def __str__(self):
    return f"This is the polar bear's taxonomy: {Mammal.__str__(self)} --> {self.order} --> {self.family} --> {self.genus} --> {self.species}"