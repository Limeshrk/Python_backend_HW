### 2.1 Counter class készítése
class Counter:
    def __init__(self, value, step=1):
        self.value = value
        self.step = step

    def increment(self):
        self.value += self.step

    def decrement(self):
        self.value -= self.step

    def set_value(self, value):
        self.value = value

    def set_step(self, step):
        self.step = step

    def get_value(self):
        return self.value
    
#Teszt
myCounter = Counter(10)
myCounter.increment()
myCounter.increment()
print(myCounter.get_value()) 
myCounter.set_step(5)
myCounter.decrement()
print(myCounter.get_value())
myCounter.set_value(100)
myCounter.increment()
print(myCounter.get_value())



###2.2 ScoreCounter alosztály a Counter alapján
class ScoreCounter(Counter):
    def __init__(self, value, name, age, step=1):
        super().__init__(value, step)
        self.name = name
        self.age = age
        self.winner = False

    def increment(self):
        super().increment()
        if self.value >= 12:
            self.winner = True

#Teszt
myScoreCounter = ScoreCounter(10, 'Zsolt', 34)
myScoreCounter.increment()
print(myScoreCounter.get_value())
myScoreCounter.increment()
print(myScoreCounter.get_value())
print(myScoreCounter.winner)
