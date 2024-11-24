# import Mammal class
from mammal import *

# create your SnowLeopard class that extends from the Mammal class
class SnowLeopard(Mammal):

 
    # Call the superclass's __init__ method and pass the required arguments. Note that we also have to pass self as an argument
  def __init__(self, domain, kingdom, phylum, class_type,name):
    Mammal.__init__(self, domain, kingdom, phylum, class_type)
    self.name = name
     # Initialize the __order, __family, __genius, __species, __vulnerability, __resilience, and __status
    
    self.order = "Carnivora"
    self.family = "Felidae"
    self.genus = "Panthera"
    self.species = "P. uncia"
    self.vulnerability = "Susceptible to indirect impacts of climate change, such as habitat encroachment by humans as a result of changing conditions in the region."
    self.resilience = "High mobility across their large, mountainous range—not bound to a narrow altitude or region."
    self.status = "Endangered"
 

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
    return f"This is the snow leopard's taxonomy:{Mammal.__str__(self)} --> {self.order} --> {self.family} --> {self.genus} --> {self.species}"
