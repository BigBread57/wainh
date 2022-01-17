from sqlalchemy_utils import ChoiceType


class CacheChoiceType(ChoiceType):
    cache_ok = True
