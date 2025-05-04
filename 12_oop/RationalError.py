# class RationalError(Exception):
#     def __init__(self, message):
#         super().__init__()
#         self.message = message
#
#     def __str__(self):
#         return f'{self.message}'

class RationalError(ZeroDivisionError):
    def __init__(self, message="Denominator cannot be zero"):
        super().__init__(message)

class RationalValueError(ValueError):
    def __init__(self, message="Invalid value for Rational operation"):
        super().__init__(message)
