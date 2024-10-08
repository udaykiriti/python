import random

class SimpleReflexAgent:
    def init(self):
        self.current_location = random.choice(['A', 'B', 'C'])

    def perceive(self):
        # Simulate perception of the current cell's status (dirty or clean)
        return random.choice(['clean', 'dirty'])

    def act(self, status):
        if status == 'dirty':
            print(f"Current location {self.current_location} is dirty. Cleaning...")
            # Simulate cleaning action
            print("Cleaning complete.")
        else:
            print(f"Current location {self.current_location} is clean. Doing nothing.")

        # Simulate moving to a new random location
        self.current_location = random.choice(['A', 'B', 'C'])
        print(f"Moving to location {self.current_location}")

if name == "main":
    agent = SimpleReflexAgent()

    for _ in range(10):
        current_status = agent.perceive()
        agent.act(current_status)
        print("------")