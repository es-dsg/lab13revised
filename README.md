[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/mFTZNmOG)
[![Open in Codespaces](https://classroom.github.com/assets/launch-codespace-2972f46106e565e64193e422d61a12cf1da4916b45550586e14ef0a7c637dd04.svg)](https://classroom.github.com/open-in-codespaces?assignment_repo_id=17232127)
# Lab 13 - Taxonomy and Climate Change  

  _Learning Objective: demonstrate class inheritance._

  To organize different species that are affected by Climate Change. The most fundamental part of inheritance is to be able to reuse attributes and methods that are share among different groups. For example there are many different mammals species. We are looking at two main species affected by Climate Change, polar bears and snow leopards.

## Part 1
Start your class definition. Name it **_Mammal_** and create the `__init__` method. Your method should initialize the following data attributes:
- domian = Eukaryota
- kindom = Animalia
- phylum = Chordata
- class_type = Mammalia


Write an accessor/getter and mutator/setter for each variable on the Mammal class. Remember naming conventions by starting each with `get_` or `set_` then the identifier for the variable.

Write the `__str__` method which returns a string of all the instance variables for a mammal taxonomy object.

ex: Eukaryota-->Animalia-->Chordata-->Mammalia

Add the data attributes and methods to the UML diagram under the UML.py file.

The identifier for each variable is given in the UML diagram in UML.py.

Test your method in main.py by creating a Mammal object.

## Part 2
Start your new class definition. Name it **_PolarBear_** and create the `__init__` method. 

Use the super `__init__` to assign values to inherit data attributes.

Your method should assign parameter value for the following data:

- name

Your method should initialize the following data attributes:

- name = name
- order = Carnivora
- family = Ursidae
- genus = Ursus
- species = U. maritimus
- vulnerability = Habitat specialists, rely almost entirely on the sea-ice environment.
- resilience = Opportunistic eaters, prefer seals, but will feed on whale carcasses and even hunt walrus and beluga. Will prey on land animals when necessary.
- status = Vulnerable

Write an accessor/getter and mutator/setter for each variable on the PolarBear class. Remember naming conventions by starting each with `get_` or `set_` then the identifier for the variable.

Write the `__str__` method which returns a string of all the instance variables for a polar bear taxonomy object.

ex: Eukaryota-->Animalia-->Chordata-->Mammalia-->Carnivora-->Ursidae-->Ursus-->U. maritius

Add the data attributes and methods to the UML diagram under the UML.py file.

The identifier for each variable is given in the UML diagram in UML.py.

Test your method in main.py by creating a PolarBear object.

## Part 3
Start your new class definition. Name it **_SnowLeopard_** and create the `__init__` method. 

Use the super `__init__` to assign values to inherit data attributes.

Your method should assign parameter value for the following data:

- name

Your method should initialize the following data attributes:

- name = name
- order = Carnivora
- family = Felidae
- genus = Panthera
- species = P. uncia
- vulnerability = Susceptible to indirect impacts of climate change, such as habitat encroachment by humans as a result of changing conditions in the region.
- resilience = High mobility across their large, mountainous range—not bound to a narrow altitude or region.
- status = Endangered

Write an accessor/getter and mutator/setter for each variable on the SnowLeopard class. Remember naming conventions by starting each with `get_` or `set_` then the identifier for the variable.

Write the `__str__` method which returns a string of all the instance variables for a polar bear taxonomy object.

ex: Eukaryota-->Animalia-->Chordata-->Mammalia-->Carnivora-->Felidae-->Panthera-->P. uncia

Add the data attributes and methods to the UML diagram under the UML.py file.

The identifier for each variable is given in the UML diagram in UML.py.

Test your method in `main.py` by creating a SnowLeopard object.

## Part 4
Start your definition main. Create a Mammal, SnowLeopard, and PolarBear object. For SnowLeopard pass the parameter 'Snow Leopard' for the name, and for PolarBear pass the parameter 'Polar Bear' for the name. 

Print each object to test the `__str__` method.

ex: This is the mammal's taxonomy Eukaryota-->Animalia-->Chordata-->Mammalia

ex: This is the Snow Leopard's taxonomy Eukaryota-->Animalia-->Chordata-->Mammalia-->Carnivora-->Felidae-->Panthera-->P. uncia

ex: This is the Polar Bear's taxonomy Eukaryota-->Animalia-->Chordata-->Mammalia-->Carnivora-->Ursidae-->Ursus-->U. maritius

Create a menu using while loops:

**Choose animal under danger:**

**a) Polar Bear**

**b) Snow Leopard**

**c) Exit**

If 'c' is choose print 'Goodbye!'

Create a submenu using while loops:

**Choose animal's:**

**a) Vulnerabiliy**

**b) Resilience**

**c) Status**

**d) Exit**

## Test and Submit
There are no automated tests for this lab so make sure you check the output of the functions before submitting. 
Send an email, drop by student hours, check in with a peer, or stop by the STEM Center if you need any assistance.

