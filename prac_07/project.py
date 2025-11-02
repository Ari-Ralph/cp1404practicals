"""
CP1404 - Practical 07
Project class file.
Estimate: 2 hours
Actual:
"""

class Project:
    """Project class to store information about a project"""
    def __init__(self,name, start_date, priority, cost_estimate, completion_percentage):
        """Initialise a project object"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = float(cost_estimate)
        self.completion_percentage = int(completion_percentage)

    def __str__(self):
        """Return string format of project object."""
        return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate:,.2f}, completion: {self.completion_percentage}%"

    def is_complete(self):
        """Is completion percentage 100"""
        return self.completion_percentage == 100