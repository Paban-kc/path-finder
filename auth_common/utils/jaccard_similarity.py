from auth_common.model.vacancy import Vacancy

class CustomSet:
    def __init__(self, elements=None):
        """Initialize the custom set with an optional list of elements."""
        if elements is None:
            elements = []
        self.elements = []
        for element in elements:
            if element not in self.elements:
                self.elements.append(element)

    def custom_add(self, element):
        """Add an element to the set if it's not already present."""
        if element not in self.elements:
            self.elements.append(element)

    def custom_remove(self, element):
        """Remove an element from the set if it exists."""
        if element in self.elements:
            self.elements.remove(element)

    def custom_size(self):
        """Return the size of the set."""
        return len(self.elements)

    def __str__(self):
        """Return a string representation of the set."""
        return "{" + ", ".join(str(e) for e in self.elements) + "}"

    def custom_intersection(self, other):
        """Return a new CustomSet with the intersection of this set and another."""
        intersection_elements = [element for element in self.elements if element in other.elements]
        return CustomSet(intersection_elements)

    def custom_union(self, other):
        """Return a new CustomSet with the union of this set and another."""
        union_elements = self.elements.copy()
        for element in other.elements:
            if element not in self.elements:
                union_elements.append(element)
        return CustomSet(union_elements)


def jaccard_similarity(list1, list2):
    set1 = CustomSet(list1)
    set2 = CustomSet(list2)

    intersection = set1.custom_intersection(set2)
    union = set1.custom_union(set2)
    no_union=union.custom_size()
    print(no_union,"union")

    if union.custom_size() == 0:
        return 0

    return intersection.custom_size() / union.custom_size()




