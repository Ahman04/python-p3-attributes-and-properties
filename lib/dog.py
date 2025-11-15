#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = ["Pug", "Dalmatian", "Labrador", "Beagle", "Bulldog", "German Shepherd"]

    def __init__(self, name=None, breed=None):
        # Validate name
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        
        # Save valid name
        self.name = name

        # Validate breed
        if breed is not None:
            if breed not in Dog.APPROVED_BREEDS:
                print("Breed must be in list of approved breeds.")
                return
            self.breed = breed
        else:
            self.breed = None
