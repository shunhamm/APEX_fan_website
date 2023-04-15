from blog.models import Character
import random

def get_character_profile_at_random() -> Character:

    characters = Character.objects.all()

    character = random.choice(characters)

    return character
