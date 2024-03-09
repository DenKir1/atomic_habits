from rest_framework.serializers import ValidationError


def validator_habit(value):
    """ Проверка заполнения полей  """
    try:
        if value['is_good']:
            if value['related'] or value['prize']:
                raise ValidationError('У приятной привычки не может быть связанной привычки или вознаграждения')
    except KeyError:
        pass

    try:
        if value['related'] and value['prize']:
            raise ValidationError('Приятная привычка или вознаграждение, что-то одно.')
    except KeyError:
        pass

    try:
        if value['duration'] > 2:
            raise ValidationError('Не более 2 минут')
    except KeyError:
        pass

    try:
        if value['related']:
            if not value['related'].is_good:
                raise ValidationError('Связанные привычки = приятные привычки')
    except KeyError:
        pass
