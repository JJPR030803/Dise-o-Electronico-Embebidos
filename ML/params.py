import random


class Param:
    """
    Clase que representa un parámetro a optimizar, incluyendo su rango válido, valor actual,
    peso de importancia, costo de cambio y el modo de optimización ("max" o "min").
    """

    def __init__(self, name: str, min: int, max: int, v_actual: float,
                 weight: float, costo_cambio: float, optim_mode: str):
        """
        Inicializa un nuevo parámetro.

        Args:
            name (str): Nombre del parámetro.
            min (int): Valor mínimo permitido.
            max (int): Valor máximo permitido.
            v_actual (float): Valor actual del parámetro.
            weight (float): Peso o importancia del parámetro.
            costo_cambio (float): Costo asociado a modificar este parámetro.
            optim_mode (str): Modo de optimización: "max" o "min".
        """
        self.name = name
        self.min = min
        self.max = max
        self.v_actual = v_actual
        self.weight = weight
        self.costo_cambio = costo_cambio
        self.optim_mode = optim_mode

    def show(self):
        """Imprime por pantalla la información del parámetro."""
        print(f"Parametro: {self.name}")
        print(f"  Min: {self.min}")
        print(f"  Max: {self.max}")
        print(f"  Valor Actual: {self.v_actual}")
        print(f"  Peso: {self.weight}")
        print(f"  Costo de Cambio: {self.costo_cambio}")
        print(f"  Modo de Optimización: {self.optim_mode}")
        print("  ---------------------")

    def calc_satisfaction(self) -> float:
        """
        Calcula el nivel de satisfacción del valor actual según el modo de optimización.

        Returns:
            float: Satisfacción normalizada entre 0 y 1.
        """
        if self.optim_mode == "max":
            return (self.v_actual - self.min) / (self.max - self.min)
        elif self.optim_mode == "min":
            return (self.max - self.v_actual) / (self.max - self.min)
        else:
            raise ValueError("Modo de optimización no válido. Debe ser 'max' o 'min'.")

    def calc_distancia_x_costo(self) -> float:
        """
        Calcula el impacto del costo de cambiar este parámetro.

        Returns:
            float: Valor penalizado por el costo de cambio.
        """
        if self.optim_mode == "max":
            return self.costo_cambio * abs((self.v_actual - self.min) / (self.max - self.min))
        elif self.optim_mode == "min":
            return self.costo_cambio * abs((self.max - self.v_actual) / (self.max - self.min))
        else:
            raise ValueError("Modo de optimización no válido. Debe ser 'max' o 'min'.")

    def calc_quadratic_penalty(self) -> float:
        """
        Calcula una penalización cuadrática si el valor actual está fuera del rango permitido.

        Returns:
            float: Penalización por violar el rango permitido.
        """
        if self.v_actual < self.min:
            return self.costo_cambio * ((self.min - self.v_actual) / (self.max - self.min)) ** 2
        elif self.v_actual > self.max:
            return self.costo_cambio * ((self.v_actual - self.max) / (self.max - self.min)) ** 2
        return 0

    def calc_satisfaction_con_penalty(self) -> float:
        """
        Calcula la satisfacción penalizada si el valor actual está fuera del rango.

        Returns:
            float: Satisfacción después de aplicar penalización.
        """
        base_satisfaction = self.calc_satisfaction()
        penalty = 0
        if self.v_actual < self.min or self.v_actual > self.max:
            penalty = self.calc_quadratic_penalty()
        return max(0, base_satisfaction - penalty)

    def generate_neighbor_v_actual(self, percentage_step: float) -> float:
        """
        Genera un nuevo valor vecino para el parámetro en base a un porcentaje del rango.

        Args:
            percentage_step (float): Tamaño del paso en porcentaje del rango total.

        Returns:
            float: Nuevo valor vecino dentro de los límites permitidos.
        """
        step_size = (self.max - self.min) * percentage_step
        direction = random.choice([-1, 1])
        valor_vecino = self.v_actual + direction * random.uniform(0, step_size)
        return max(self.min, min(self.max, valor_vecino))

    def is_in_range(self, value=None) -> bool:
        """
        Verifica si un valor (o el actual) está dentro del rango permitido.

        Args:
            value (float, optional): Valor a verificar. Por defecto se usa v_actual.

        Returns:
            bool: True si está dentro del rango, False en caso contrario.
        """
        check_value = value if value is not None else self.v_actual
        return self.min <= check_value <= self.max
