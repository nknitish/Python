# multilevel inheritance.
# Grandparent → Parent → Child

# Grandparent Class
class GrandParent:
    def grandparent_property(self):
        print("I have a house.")


# Parent Class inherits GrandParent
class Parent(GrandParent):
    def parent_property(self):
        print("I have a car.")


# Child Class inherits Parent
class Child(Parent):
    def child_property(self):
        print("I have a bicycle.")


# Create Child object
c = Child()

# Child can access methods from all levels
c.grandparent_property()
c.parent_property()
c.child_property()