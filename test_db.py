from .models import Gifs_of_skins


def test_abaddon():
    hero = Gifs_of_skins.query.all()
    id = hero[0].id
    name = hero[0].hero_name
    gif = hero[0].gif_link
    if (id == 1) and (name == 'abaddon') and (gif == 'static/gifs/abaddon.gif'):
        print("OK")
    else:
        print("NO OK")

