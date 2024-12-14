# ner_extraction.py
import spacy
    
nlp = spacy.load("en_core_web_sm")

def extract_entities(article_text):
    """Extract PERSON and ORG entities from the article text."""
    doc = nlp(article_text)
    entities = [(ent.text, ent.label_) for ent in doc.ents if ent.label_ in ['PERSON', 'ORG']]
    return entities