from .constants import Directions


class Snake:
    def __init__(self):
        self.__snake = [(0, 2), (0, 1), (0, 0)]
        self.__direction = Directions.UP

    def set_direction(self, direction):
        if Directions.can_set_direction(self.__direction, direction):
            self.__direction = direction

    def step(self, width, height, fruit):
        old_head = self.__snake[0]
        movement = self.__direction.increment
        new_head = (old_head[0]+movement[0], old_head[1]+movement[1])

        if (
                new_head[0] < 0 or
                new_head[0] >= width or
                new_head[1] < 0 or
                new_head[1] >= height or
                new_head in self.__snake
        ):
            return False

        if fruit == new_head:
            fruit.place_fruit(width, height, self.__snake)
        else:
            tail = self.__snake[-1]
            del self.__snake[-1]

        self.__snake.insert(0, new_head)
        return True

    def display(self, display_func):
        for snake_piece in self.__snake:
            display_func(snake_piece)
