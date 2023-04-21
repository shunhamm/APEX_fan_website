from blog.models import Character
from bs4 import BeautifulSoup
import requests
import random
from .models import ExternalLink

def get_character_profile_at_random() -> Character:

    characters = Character.objects.all()

    character = random.choice(characters)

    return character

def add_image_url(links: list[ExternalLink]):

    for link in links:
        res = requests.get(link.url)
        soup = BeautifulSoup(res.text, 'html.parser')
        link.image_url = soup.find('meta', property='og:image').get('content')

    return links
