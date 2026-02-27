class ProctorCSP:
    def __init__(self, exams, proctors, availability, skills):
        self.exams = exams                      # List of exams
        self.proctors = proctors                # List of proctors
        self.availability = availability        # Proctor availability
        self.skills = skills                    # Proctor skills

    # Check if assigning proctor to exam is valid
    def is_valid(self, exam, proctor, assignment):
        # 1. Proctor must be available for that exam
        if exam not in self.availability.get(proctor, []):
            return False

        # 2. Skill must match
        if exam not in self.skills.get(proctor, []):
            return False

        # 3. One proctor per exam (already ensured by assignment)
        # 4. Proctor should not be assigned to two exams at same time
        if proctor in assignment.values():
            return False

        return True

    # Backtracking algorithm
    def backtrack(self, assignment):
        # If all exams assigned
        if len(assignment) == len(self.exams):
            return assignment

        # Select unassigned exam
        exam = next(e for e in self.exams if e not in assignment)

        # Try all proctors
        for proctor in self.proctors:
            if self.is_valid(exam, proctor, assignment):
                assignment[exam] = proctor
                result = self.backtrack(assignment)

                if result:
                    return result

                # Backtrack
                del assignment[exam]

        return None


# ------------------ Example Data ------------------

exams = ["Math", "Physics", "Chemistry"]

proctors = ["Alice", "Bob", "Charlie"]

availability = {
    "Alice": ["Math", "Physics"],
    "Bob": ["Physics", "Chemistry"],
    "Charlie": ["Math", "Chemistry"]
}

skills = {
    "Alice": ["Math"],
    "Bob": ["Physics"],
    "Charlie": ["Chemistry"]
}

# Create CSP object
csp = ProctorCSP(exams, proctors, availability, skills)

solution = csp.backtrack({})

# Print result
if solution:
    print("Proctor Assignment:")
    for exam, proctor in solution.items():
        print(f"{exam} → {proctor}")
else:
    print("No valid assignment found.")

"""
output:
Proctor Assignment:
Math → Alice
Physics → Bob
Chemistry → Charlie
"""