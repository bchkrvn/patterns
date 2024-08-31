from validators import ListValidator, StringValidator, IntegerValidator, DictValidator, BaseValidator


class ValidatorFactory:
    data = {
        'string': StringValidator,
        'integer': IntegerValidator,
        'list': ListValidator,
        'dict': DictValidator,
    }

    @classmethod
    def get_validator(cls, type_: str) -> BaseValidator or None:
        validator = cls.data.get(type_.lower())
        if not validator:
            raise TypeError
        return validator
