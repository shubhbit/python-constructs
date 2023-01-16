from animal import Animal

class Human(Animal):
    def move(self):
        """
        human move
        """
        print("I walk")

class Snake(Animal):
    def move(self):
        """
        snake move
        """
        print("I crawl")

class Dog(Animal):
    def move(self):
        """
        dog move
        """
        print("I bark.")


if __name__ == "__main__":
    human = Human()
    human.move()
    snake = Snake()
    snake.move()
    dog = Dog()
    dog.move()
