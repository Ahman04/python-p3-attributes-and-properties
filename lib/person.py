#!/usr/bin/env python3

class Person:
    APPROVED_JOBS = ["Sales", "ITC", "HR", "Engineer", "Manager"]

    def __init__(self, name=None, job=None):
        # Validate name
        if not isinstance(name, str) or len(name) == 0 or len(name) > 25:
            print("Name must be string between 1 and 25 characters.")
            return
        
        # Save valid, title-cased name
        self.name = name.title()

        # Validate job
        if job is not None:
            if job not in Person.APPROVED_JOBS:
                print("Job must be in list of approved jobs.")
                return
            self.job = job
        else:
            self.job = None
