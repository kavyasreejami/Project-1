import unittest
from db.database import Base, engine
from db.models import NewsArticle
from sqlalchemy.orm import sessionmaker

# Setting up test database
Session = sessionmaker(bind=engine)
session = Session()

class TestDatabase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Runs once before all tests."""
        Base.metadata.create_all(engine)

    @classmethod
    def tearDownClass(cls):
        """Runs once after all tests."""
        Base.metadata.drop_all(engine)

    def test_create_article(self):
        """Test inserting a new article into the database."""
        article = NewsArticle(
            url='https://example.com/news1',
            title='Test Article',
            content='This is a test article.',
            entities='[{"text": "Example", "label": "ORG"}]',
            sentiment='positive'
        )
        session.add(article)
        session.commit()

        # Query the article from the database
        retrieved_article = session.query(NewsArticle).filter_by(url='https://example.com/news1').first()
        self.assertEqual(retrieved_article.title, 'Test Article')
        self.assertEqual(retrieved_article.sentiment, 'positive')

if __name__ == '__main__':
    unittest.main()
