import joblib
import re
from nltk.corpus import stopwords
stop_words = set(stopwords.words("russian"))

class Model:
	def __init__(self):
		self.model = joblib.load('abina_model.sav')
		self.vectorizer = joblib.load('abina_tfidf.bin')
		self.lemmatizer = joblib.load('abina_lemmatizer.bin')
		
	def predict(self, text: str):
		preprocessed_text = self.preprocess(text)
		vectorized_text = self.vectorizer.transform(preprocessed_text)
		return vectorized_text #self.model.predict(vectorized_text)
		
	def preprocess(self, comment:str):
		comment = re.sub(r'[^А-яЁё]+', ' ', comment).lower()
		comment = " ".join(comment.split())
		comment = [word for word in comment.split() if not word in stop_words]
		comment = [self.lemmatizer.lemmatize(token) for token in comment.split()]
		comment = [self.lemmatizer.lemmatize(token, "v") for token in comment]
		#comment = [word for word in comment if not word in stop_words]
		#comment = " ".join(comment)
		return comment
	

# # Оставим в тексте только кириллические символы
# def clear_text(text):
#     clear_text = re.sub(r'[^А-яЁё]+', ' ', text).lower()
#     return " ".join(clear_text.split())


# # напишем функцию удаляющую стоп-слова
# def clean_stop_words(text, stopwords):
#     text = [word for word in text.split() if word not in stopwords]
#     return " ".join(text)

# # загрузим список стоп-слов
# stopwords = set(nltk_stopwords.words('russian'))
# np.array(stopwords)	