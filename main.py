import abc
import math
import random
import time


class Person(metaclass=abc.ABCMeta):

    def __init__(self, name: str):
        self.hp = 100
        self.joy = random.randint(-20, 20)
        self.name = name
        self.age = 0

    def meet(self, other):
        if self.joy > 0 and other.joy > 0:
            self.joy += 15
            other.joy += 15
        elif self.joy > 0 and other.joy < 0:
            self.joy -= 5
            other.joy += 5
        elif self.joy < 0 and other.joy > 0:
            self.joy += 5
            other.joy -= 5
        else:
            self.joy -= 5
            other.joy -= 5

    def update_hp(self):
        if self.joy < 0:
            self.hp -= 5

    def __str__(self):
        return f'{self.name} HP: {self.hp} JOY: {self.joy} AGE:{self.age}'


class Ball(Person):

    def __init__(self, name: str, radius):
        super().__init__(name)
        self.radius = radius


class Square(Person):

    def __init__(self, name: str, side):
        super().__init__(name)
        self.side = side


def main():
    balls = [Ball(f"Ball{i}", radius=random.randint(-50, 50)) for i in range(10)]
    squares = [Square(f"Square{i}", side=random.randint(-50, 50)) for i in range(10)]
    people = balls + squares
    while True:
        print("*" * 20)
        p1 = random.choice(people)
        while True:
            p2 = random.choice(people)
            if p2 != p1:
                break
        print(f"{p1.name} met {p2.name}")
        print(str(p1) + '\n' + str(p2))

        p1.meet(p2)

        p1.update_hp()
        p2.update_hp()

        if p1.age % 30 == 0:
            p1.joy = -10
        if p2.age % 30 == 0:
            p2.joy = -10

        if random.randint(1, 5) == 1:
            p1.joy -= 10
            p2.joy -= 10

        if random.randint(1, 3) == 1:
            p1.joy += 10
            p2.joy += 10

        p1.age += 1
        p2.age += 1

        if p1.hp <= 0:
            print(f'{p1.name} DEAD')
            people.remove(p1)
            # time.sleep(3)
        if p2.hp <= 0:
            print(f'{p2.name} DEAD')
            people.remove(p2)
            # time.sleep(3)

        # time.sleep(0.25)

        if len(people) <= 1:
            print("ALL DEAD")
            break


if __name__ == '__main__':
    main()
