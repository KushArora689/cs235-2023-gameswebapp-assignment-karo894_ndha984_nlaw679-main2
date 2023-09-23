
from games.adapters.repository import AbstractRepository
import games.adapters.repository as repo


def get_number_of_games(repo: AbstractRepository):
    return repo.get_number_of_games()


def get_games(repo: AbstractRepository):
    games = repo.get_games()
    game_dicts = []
    for game in games:
        game_dict = {
            'game_id': game.game_id,
            'title': game.title,
            'game_url': game.description,
        }
        game_dicts.append(game_dict)
    return game_dicts
