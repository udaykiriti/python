class SimpleReflexAgent:
    def init(self):
        self.location = None

    def set_location(self, location):
        self.location = location

    def get_location(self):
        return self.location

    def update_environment(self, environment):
        if environment[self.location] == 'dirty':
            environment[self.location] = 'clean'
            print(f'Cleaned location: {self.location}')

environment = {'A': 'dirty', 'B': 'clean', 'C': 'dirty'}
agent = SimpleReflexAgent()
print(environment)
agent.set_location('A')

agent.update_environment(environment)

print(environment)

agent.set_location('B')
agent.update_environment(environment)
print(environment)

agent.set_location('C')
agent.update_environment(environment)
print(environment)