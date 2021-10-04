from nltk import FreqDist
import string
from nltk.corpus import stopwords

from natasha import (
    PER,
    NamesExtractor,
    MorphVocab,
    Doc,
    Segmenter,
    NewsEmbedding,
    NewsNERTagger,
    NewsMorphTagger,
)

# Визуализация
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import numpy as np
from PIL import Image


def file_process(*file_names):
    for name in file_names:
        with open(name, 'r', encoding='utf-8') as file:
            extract_names_keys(file.read(), 10)


def extract_names_keys(text, word_count):
    segmenter = Segmenter()
    emb = NewsEmbedding()
    morph_tagger = NewsMorphTagger(emb)
    # syntax_parser = NewsSyntaxParser(emb)
    ner_tagger = NewsNERTagger(emb)
    doc = Doc(text)

    doc.segment(segmenter)
    # new fields appear sents and tokens
    doc.tag_morph(morph_tagger)
    # doc.parse_syntax(syntax_parser)
    # After applying morph_tagger and syntax_parser, tokens get 5 new fields id, pos, feats, head_id, rel
    doc.tag_ner(ner_tagger)
    # After applying ner_tagger doc gets spans field with PER, LOC, ORG annotation

    morph_vocab = MorphVocab()
    punctuation = string.punctuation + '\n\xa0«»\t—…'
    for token in doc.tokens:
        token.lemmatize(morph_vocab)
    stop = stopwords.words("russian")
    key_words_list = [_.lemma for _ in doc.tokens if _.lemma not in stop and _.lemma not in punctuation]
    tag_cloud(key_words_list)
    key_words_list = [word[0] for word in FreqDist(key_words_list).most_common(word_count)]
    print(key_words_list)

    names_extractor = NamesExtractor(morph_vocab)

    for span in doc.spans:
        span.normalize(morph_vocab)
        if span.type == PER:
            span.extract_fact(names_extractor)
    names = [_.fact.as_dict for _ in doc.spans if _.type == PER]

    print(names)


def tag_cloud(text):
    text = " ".join(text)

    mask = np.array(Image.open('mask.png'))
    word_cloud = WordCloud(width=1300,
                           height=1300,
                           random_state=1,
                           background_color='#2D1303',
                           margin=20,
                           colormap='Set2',
                           collocations=False,
                           mask=mask).generate(text)

    # Устанавить размер картинки
    plt.figure(figsize=(40, 30))
    # Показать изображение
    plt.imshow(word_cloud)
    # Без подписей на осях
    plt.axis("off")
    word_cloud.to_file(str(hash(word_cloud)) + '.png')

