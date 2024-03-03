# >> DESIGN OVERVIEW
# User: Represents a user of the fitness tracker.
# Activity: Abstract base class representing various user activities (e.g., walking, running). 
#           Subclasses can be created for specific activities like swimming or cycling.
# ActivityMonitor: Observes user activities and notifies the Display when new data is collected.
# DataStorage: Responsible for storing user activity data.
# Display: Displays user activity data.

# >> DESIGN RATIONALE
# Single Responsibility Principle (SRP):
#           User Class: Represents a single user of the fitness tracker, focusing solely on user-
#           related data.
#           Activity Classes: Each concrete activity class (e.g., "Walking") is responsible for 
#           managing data collection and notifying observers about its specific activity type.
#           ActivityMonitor Class: Observes user activities and notifies the display, adhering to a 
#           single responsibility of monitoring activities.
#           DataStorage Class: Handles the storage of user activity data, ensuring a clear 
#           separation of concerns between data storage and other functionalities.
#           Display Class: Focuses on displaying user activity data, ensuring separation of 
#           concerns between data presentation and other functionalities.
# Open-Closed Principle (OCP):
#           Activity Classes: Abstract base class "Activity" defines a contract for collecting 
#           and notifying observers about user activities. Concrete activity classes like "Walking" 
#           can be extended or new subclasses can be added for new activity types (e.g., swimming, 
#           cycling) without modifying existing code.
#           ActivityMonitor Class: Utilizes the Observer pattern to notify observers about user 
#           activities, allowing for easy addition of new activity types without modifying the monitor.
# Liskov Substitution Principle (LSP):
#           Activity Class and Subclasses: Activity subclasses (e.g., "Walking") adhere to the 
#           observer pattern's contracts by implementing methods for attaching, detaching, and 
#           notifying observers, making them compatible with the notification mechanism used by 
#           the "ActivityMonitor".
# Interface Segregation Principle (ISP):
#           DataCollector and DataDisplayer Interfaces: Define separate interfaces for data 
#           collection and display, ensuring that each interface has a distinct set of responsibilities. 
#           This allows clients to depend only on the methods they use, preventing unnecessary coupling.
# Dependency Inversion Principle (DIP):
#           ActivityMonitor Constructor: Injects dependencies like "DataStorage" and "Display" 
#           into the constructor, promoting loose coupling and allowing for easier testing and 
#           maintenance. The "ActivityMonitor" class depends on abstractions (interfaces)
#           rather than concrete implementations, facilitating flexibility and extensibility.
#           Extensibility: The system is designed to be easily extensible, allowing for the addition 
#           of new activity types without modifying existing code. This is achieved through the use of 
#           abstract base classes, interfaces, and the Observer pattern.
#           Testability: The separation of concerns and dependency injection make the system easier to 
#           test. Mock objects can be used to simulate behavior of dependencies (e.g., "DataStorage"
#           and "Display") during unit testing of other components.
#           Documentation: Each class and method is accompanied by clear comments explaining its 
#           purpose, responsibilities, and interactions with other components. This documentation helps
#           developers understand the design decisions and rationale behind the system architecture.

from abc import ABC, abstractmethod
from typing import List

# Interface for data collection
class DataCollector(ABC):
    @abstractmethod
    def collect_data(self):
        # Abstract method to collect data
        raise NotImplementedError("Subclasses must implement collect_data method.")

# Interface for data display
class DataDisplayer(ABC):
    @abstractmethod
    def display_data(self, data: dict):
        # Abstract method to display data
        raise NotImplementedError("Subclasses must implement display_data method.")

# User class representing a fitness tracker user
class User:
    def __init__(self, user_id: int, name: str):
        self.user_id = user_id
        self.name = name

# Abstract class representing user activity
class Activity(ABC):
    def __init__(self, user: User):
        self.user = user
        self.observers: List[DataDisplayer] = []

    def attach(self, observer: DataDisplayer):
        self.observers.append(observer)

    def detach(self, observer: DataDisplayer):
        self.observers.remove(observer)

    def notify_observers(self, data: dict):
        for observer in self.observers:
            observer.display_data(data)

    @abstractmethod
    def collect_data(self):
        print("Subclass implemented collect_data method.")

# Concrete activity class for walking
class Walking(Activity):
    def collect_data(self):
        # Dummy data collection logic for walking activity
        data = {"activity": "Walking", "steps": 5000, "distance": 3.5, "calories": 200}
        self.notify_observers(data)

# ActivityMonitor observes user activities and notifies the Display
class ActivityMonitor:
    def __init__(self, user: User, data_storage: DataCollector, display: DataDisplayer):
        self.user = user
        self.data_storage = data_storage
        self.display = display

    def monitor_activity(self, activity: Activity):
        activity.attach(self.display)
        activity.collect_data()

# DataStorage stores user activity data
class DataStorage(DataCollector):
    def collect_data(self):
        # Dummy implementation to store data in a database or file
        print("Data stored in database.")

# Display displays user activity data
class Display(DataDisplayer):
    def display_data(self, data: dict):
        print("Displaying data:", data)

# Main function to test the system using dummy data
def main():
    # Create a user
    user = User(1, "Alice")

    # Create instances of DataStorage and Display
    data_storage = DataStorage()
    display = Display()

    # Create an instance of ActivityMonitor
    activity_monitor = ActivityMonitor(user, data_storage, display)

    # Monitor a specific activity (e.g., walking)
    walking_activity = Walking(user)
    activity_monitor.monitor_activity(walking_activity)

if __name__ == "__main__":
    main()