from src.data_base import current_session
from src.data_base.models.player_and_room import Player, Room
from src.data_base.models.game import Game


async def get_username(user_id):
    return current_session.query(Player).get({'user_id': user_id})
