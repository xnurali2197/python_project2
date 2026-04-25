class Concept:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")

class SubConcept(Concept):
    def __init__(self, name, description, sub_name):
        super().__init__(name, description)
        self.sub_name = sub_name

    def display_sub_info(self):
        print(f"Sub Name: {self.sub_name}")

class ConceptManager:
    def __init__(self):
        self.concepts = []

    def add_concept(self, concept):
        self.concepts.append(concept)

    def display_concepts(self):
        for concept in self.concepts:
            concept.display_info()
            if isinstance(concept, SubConcept):
                concept.display_sub_info()

def main():
    concept1 = Concept("Concept #1", "This is the first concept")
    concept2 = Concept("Concept #2", "This is the second concept")
    sub_concept1 = SubConcept("Concept #3", "This is the third concept", "Sub Concept #1")

    manager = ConceptManager()
    manager.add_concept(concept1)
    manager.add_concept(concept2)
    manager.add_concept(sub_concept1)

    manager.display_concepts()

    print("\n")

    for concept in manager.concepts:
        if isinstance(concept, Concept):
            print(f"{concept.name} is a concept")
        elif isinstance(concept, SubConcept):
            print(f"{concept.name} is a sub concept")

    print("\n")

    for concept in manager.concepts:
        if hasattr(concept, 'sub_name'):
            print(f"{concept.name} has a sub name: {concept.sub_name}")

def check_type(concept):
    if isinstance(concept, Concept):
        return "Concept"
    elif isinstance(concept, SubConcept):
        return "SubConcept"

def get_concept_info(concept):
    return {
        "name": concept.name,
        "description": concept.description,
        "type": check_type(concept)
    }

def main2():
    concept1 = Concept("Concept #1", "This is the first concept")
    concept2 = Concept("Concept #2", "This is the second concept")
    sub_concept1 = SubConcept("Concept #3", "This is the third concept", "Sub Concept #1")

    print(get_concept_info(concept1))
    print(get_concept_info(concept2))
    print(get_concept_info(sub_concept1))

main()
main2()