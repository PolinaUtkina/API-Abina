import streamlit as st
from youtube_comment_downloader import *
import pandas as pd	
import matplotlib.pyplot as plt
#from model import Model
#model = Model()

def download(message: str):
    comments_text = []
    downloader = YoutubeCommentDownloader()
    try:
        comments = downloader.get_comments_from_url(message, sort_by=SORT_BY_POPULAR)
        for comment in comments:
            comments_text.append(comment['text'])
        comments_df = pd.DataFrame({'text': comments_text})
        result = 'Комментарии получены'
    except Exception:
        result = 'Ошибка в ссылке'
        comments_df = ''
    return result, comments_df

form = st.form(key='input_link')
message = form.text_input(label='Введите ссылку на видео на YouTube')
submit_button = form.form_submit_button(label='Готово')

if submit_button:
    st.write('Подождите, пожалуйста')
    comments = download(message)
    st.write(comments[0])
    if comments[0] == 'Комментарии получены':
        df_comments = comments[1]
        df_comments['lengt'] = df_comments['text'].apply(len)
        df_comments.groupby('lengt').count().plot(kind="bar")
        plt.savefig('abr.png')
        st.image('abr.png', caption='Диаграмма распределения позитивных (1) и негативных (0) отзывов')
