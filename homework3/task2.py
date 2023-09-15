# Паттер strategy
# Множество схожих классов, отличающихся поведением
# Много поведений через ветвления

from abc import ABC, abstractmethod
from enum import Enum


class Mood(Enum):
    "Настроение баристы"
    GOOD = 1
    BAD = 2
    BETTER_STAY_AWAY = 3


class Strategy(ABC):
    """Интерфейс strategy"""

    @abstractmethod
    def check_mood(self, mood: Mood) -> bool:
        raise NotImplementedError("Метод check_mood_chief должен быть переопределн в дочернем классе")

    def order_processing(self, money: int) -> str:
        raise NotImplementedError("Метод order_processing должен быть переопределн в дочернем классе")


class GoodStrategy(Strategy):

    def check_mood(self, mood: Mood) -> bool:
        if (mood is Mood.GOOD
                or mood is Mood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return 'Лучший напиток из возможных'


class BadStrategy(Strategy):

    def check_mood(self, mood: Mood) -> bool:
        if (mood is Mood.BETTER_STAY_AWAY
                or mood is Mood.BAD):
            return True
        return False

    def order_processing(self, money: int) -> str:
        return 'Налить americano'


class NormalStrategy(Strategy):

    def check_mood(self, mood: Mood) -> bool:
        return True

    def order_processing(self, money: int) -> str:
        if money < 5:
            return 'Вежливо отказатья от заказа'

        if money < 10:
            return 'Приготовить эспрессо'

        if money < 25:
            return 'Приготовить капучино или латте'

        return 'Лучший напиток из возможных'


class Barista:
    def __init__(self, strategy: Strategy,
                 mood: Mood):
        self._strategy = strategy
        self._mood = mood
        print(f'Текущее настроение баристы {mood.name}')

    def set_mood(self, mood: Mood) -> None:
        print((f'Текущее настроение баристы {mood.name}'))
        self._mood = mood

    def set_strategy(self, strategy: Strategy) -> None:
        self._strategy = strategy

    def take_order(self, money: int) -> None:
        print(f'Клиент отдал за заказ {money} рублей')

        if self._strategy.check_mood(self._mood):
            print(self._strategy.order_processing(money))
        else:
            print("Изобразить будто ничего не произошло")


barista1 = Barista(NormalStrategy(), Mood.BETTER_STAY_AWAY)
barista1.take_order(1)
barista1.take_order(20)
barista1.take_order(30)
barista1.set_strategy(BadStrategy())
barista1.take_order(1)
barista1.take_order(20)
barista1.take_order(30)
barista1.set_strategy(GoodStrategy())
barista1.take_order(1)
barista1.set_mood(Mood.GOOD)
barista1.take_order(1)
barista1.take_order(20)
barista1.take_order(30)
