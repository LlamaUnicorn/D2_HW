from django.urls import path

from .views import (
    NewsList, NewsDetail, NewsCreate, NewsUpdate, NewsDelete, NewsSearch, subscribe_me, unsubscribe_me, CategoryList
)

urlpatterns = [
    path('', NewsList.as_view(), name='news_list'),
    path('category/', CategoryList.as_view()),
    path('<int:pk>', NewsDetail.as_view(), name='news_detail'),
    path('create/', NewsCreate.as_view(), name='news_create'),
    path('<int:pk>/update/', NewsUpdate.as_view(), name='news_update'),
    path('<int:pk>/delete/', NewsDelete.as_view(), name='news_delete'),
    path('search/', NewsSearch.as_view(), name='news_search'),
    path('subscribe/<int:pk>', subscribe_me),
    path('unsubscribe/<int:pk>', unsubscribe_me),
    path('category/subscribe/<int:pk>', subscribe_me),
    path('category/unsubscribe/<int:pk>', unsubscribe_me),
    # path('create2/', ArticleCreate.as_view(), name='article_create')
    path('subscribe/<int:pk>', subscribe_me),
    path('unsubscribe/<int:pk>', unsubscribe_me),
    path('category/subscribe/<int:pk>', subscribe_me),
    path('category/unsubscribe/<int:pk>', unsubscribe_me),
]

