from nltk.corpus import wordnet as wn
import random
import urllib.parse
from app.extensions import db

class URLGenerator:
    @staticmethod
    def generate_random_noun():
        nouns = list(wn.all_synsets(pos=wn.NOUN))
        random_noun = random.choice(nouns)
        noun_lemmas = random_noun.lemmas()
        return noun_lemmas[0].name() if noun_lemmas else None

    @staticmethod
    def generate_urls(count, base_url):
        urls = []
        for _ in range(count):
            var = URLGenerator.generate_random_noun()
            if var:
                encoded_var = urllib.parse.quote(var)
                url = f"{base_url}?id={encoded_var}&tab=Design&name=index"
                urls.append({'url': url, 'noun': var})
        return urls

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    noun = db.Column(db.String(64), index=True)
    url = db.Column(db.String(256))
    created_at = db.Column(db.DateTime, server_default=db.func.now())