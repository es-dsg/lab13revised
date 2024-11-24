
# create your Mammal class
class Mammal:

  # __init__ method accepts the arguments for the kindom, phylum,and class_type. It initiliazes the data attributes with these values
  def __init__(self, domain, kingdom, phylum, class_type):
    self.domain = domain
    self.kingdom = kingdom
    self.phylum = phylum
    self.class_type= class_type


  # methods for the mutators/setters for the class's data attributes
  def set_domain(self, domain):
    self.domain = domain
  def set_kingdom(self, kingdom):
    self.kingdom = kingdom
  def set_phylum(self, phylum):
    self.phylum = phylum
  def set_kingdom(self, class_type):
    self.class_type = class_type

  # methods for the accessors/getters for the class's data attributes
  def get_domain(self):
    return self.domain
  def get_kingdom(self):
    return self.kingdom
  def get_phylum(self):
    return self.phylum
  def get_class_type(self):
    return self.class_type

  # method for class string
  def __str__(self):
    return "This is the mammal's taxonomy: " f"{self.domain} -->{self.kingdom}--> {self.phylum}--> {self.class_type}"