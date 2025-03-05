class Point:
    """
    Класс для представления точки в 2D пространстве.

    Attributes:
        x (float): Координата по оси X.
        y (float): Координата по оси Y.
    """

    def __init__(self, x: float, y: float) -> None:
        """
        Инициализирует точку с заданными координатами.

        Args:
            x (float): Координата по оси X.
            y (float): Координата по оси Y.
        """
        self.x = x
        self.y = y

    def distance_to(self, other: 'Point') -> float:
        """
        Вычисляет расстояние до другой точки.

        Args:
            other (Point): Другая точка.

        Returns:
            float: Расстояние до другой точки.

        Examples:
            >>> p1 = Point(0, 0)
            >>> p2 = Point(3, 4)
            >>> p1.distance_to(p2)
            5.0
        """
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5


class Circle:
    """
    Класс для представления круга.

    Attributes:
        center (Point): Центр круга.
        radius (float): Радиус круга.
    """

    def __init__(self, center: Point, radius: float) -> None:
        """
        Инициализирует круг с заданным центром и радиусом.

        Args:
            center (Point): Центр круга.
            radius (float): Радиус круга.
        """
        self.center = center
        self.radius = radius

    def area(self) -> float:
        """
        Вычисляет площадь круга.

        Returns:
            float: Площадь круга.

        Examples:
            >>> c = Circle(Point(0, 0), 1)
            >>> c.area()
            3.141592653589793
        """
        import math
        return math.pi * (self.radius ** 2)


class Rectangle:
    """
    Класс для представления прямоугольника.

    Attributes:
        bottom_left (Point): Левая нижняя точка прямоугольника.
        width (float): Ширина прямоугольника.
        height (float): Высота прямоугольника.
    """

    def __init__(self, bottom_left: Point, width: float, height: float) -> None:
        """
        Инициализирует прямоугольник с заданной левой нижней точкой, шириной и высотой.

        Args:
            bottom_left (Point): Левая нижняя точка прямоугольника.
            width (float): Ширина прямоугольника.
            height (float): Высота прямоугольника.
        """
        self.bottom_left = bottom_left
        self.width = width
        self.height = height

    def area(self) -> float:
        """
        Вычисляет площадь прямоугольника.

        Returns:
            float: Площадь прямоугольника.

        Examples:
            >>> r = Rectangle(Point(0, 0), 3, 4)
            >>> r.area()
            12
        """
        return self.width * self.height


if __name__ == "__main__":
    import doctest
    doctest.testmod()
