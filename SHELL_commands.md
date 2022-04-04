# D2_HW
1. Создать двух пользователей (с помощью метода User.objects.create_user('username')).
```
>>> user1 = User.objects.create_user(username='Alexa')
>>> user1
<User: Alexa>

>>> user2 = User.objects.create_user(username='Bill') 
>>> user2
<User: Bill>
```
2. Создать два объекта модели Author, связанные с пользователями.
```
>>> Author.objects.create(authorUser=user1) 
<Author: Author object (1)>
>>> Author.objects.create(authorUser=user2)  
<Author: Author object (2)>
```
3. Добавить 4 категории в модель Category.
```
>>> Category.objects.create(name='Politics')
<Category: Category object (1)>
>>> Category.objects.create(name='Finances') 
<Category: Category object (2)>
>>> Category.objects.create(name='Technology') 
<Category: Category object (3)>
>>> Category.objects.create(name='Sports')     
<Category: Category object (4)>
```
4. Добавить 2 статьи и 1 новость.
```
# Creating news:
>>> author = Author.objects.get(id=1)
>>> author
<Author: Author object (1)>

>>> Post.objects.create(author=author, categoryType='NW', title='News_title_1', text='News_text_
1')
<Post: Post object (1)>
>>> Post.objects.get(id=1).title
'News_title_1'

# Creating first article:
>>> Post.objects.create(author=author, categoryType='AR', title='Article_title_1', text='Article
_text_1')
>>> Post.objects.get(id=2).title 
'Article_title_1'

# Creating second article:
>>> author2 = Author.objects.get(id=2)
>>> author2
<Author: Author object (2)>
>>> Post.objects.create(author=author2, categoryType='AR', title='Article_title_2', text='Articl
e_text_2')
<Post: Post object (3)>
>>> Post.objects.get(id=3).title       
'Article_title_2'
```
5. Присвоить им категории (как минимум в одной статье/новости должно быть не меньше 2 категорий).
```
# Post id=1 gets categories 1 and 2:
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=1).postCategory.add(Category.objects.get(id=2))

# Post id=2 gets categories 1 and 3:
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=1))
>>> Post.objects.get(id=2).postCategory.add(Category.objects.get(id=3))

# Post id=3 gets category 4:
>>> Post.objects.get(id=3).postCategory.add(Category.objects.get(id=4))
```
[<img src="https://downloader.disk.yandex.ru/preview/3b6c336e0bae33d3050ebd99547d71814c87896f4491234d65fa0a5490055006/624b6282/gIVofEerUGoUyT9bf6HXyhy95Dxt8guQQMIOfSuT7ee1UFqa4ne_K7-rTL_cYJg0ca1T1s9M-aJw2dUiJG9uAg%3D%3D?uid=0&filename=2022-04-03_17-12-58.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048">](Визуализация)

6. Создать как минимум 4 комментария к разным объектам модели Post (в каждом объекте должен быть как минимум один комментарий).
```
>>> Comment.objects.create(commentPost=Post.objects.get(id=1), commentUser=Author.objects.get(id
=1).authorUser, text='comment_by_author')
<Comment: Comment object (1)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=1).authorUser, text='second
_comment_by_author')
<Comment: Comment object (2)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=2), commentUser=Author.objects.get(id=2).authorUser, text='first_
comment_by_author2')
<Comment: Comment object (3)>
>>> Comment.objects.create(commentPost=Post.objects.get(id=3), commentUser=Author.objects.get(id=2).authorUser, text='second
_comment_by_author2')
<Comment: Comment object (4)>
```
7. Применяя функции like() и dislike() к статьям/новостям и комментариям, скорректировать рейтинги этих объектов.
```
# Comments Likes/Dislikes
>>> Comment.objects.get(id=1).like()
>>> Comment.objects.get(id=1).rating
1
>>> Comment.objects.get(id=1).dislike()     
>>> Comment.objects.get(id=1).dislike()
>>> Comment.objects.get(id=1).dislike()
>>> Comment.objects.get(id=1).rating        
-2
>>> Comment.objects.get(id=2).like() 
>>> Comment.objects.get(id=2).like()
>>> Comment.objects.get(id=2).rating
2
>>> Comment.objects.get(id=3).dislike() 
>>> Comment.objects.get(id=3).rating   
-1
>>> Comment.objects.get(id=4).like()    
>>> Comment.objects.get(id=4).rating 
1

# Posts Likes/Dislikes
>>> Post.objects.get(id=1).like()
>>> Post.objects.get(id=1).rating  
1
>>> Post.objects.get(id=2).dislike()
>>> Post.objects.get(id=2).rating   
-1
>>> Post.objects.get(id=3).like()    
>>> Post.objects.get(id=3).like()
>>> Post.objects.get(id=3).rating 
2
```
[<img src="https://downloader.disk.yandex.ru/preview/11128a59ea27f84f95f77d2812e883ffe2313b786cce01ed385e496bef620e92/624b643b/aUvBNWDbIaJFj0QZz5eSTG1v42XxW13rjy-oOnR2WZpTGwi-qzxgHVKK9fJdonxyhPCzyjMiqS9b-r8RAEy4FA%3D%3D?uid=0&filename=2022-04-03_20-27-28.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048">](Рейтинг_комментариев)

[<img src="https://downloader.disk.yandex.ru/preview/fbebbb7137b512f947a46fdd33d3cd476ce37d60f58ee624df817c291788c4af/624b6478/22VZQDC3QdoIBSMUZBCQhe3ez1wVDIkXQqzFPETF1pp5LYO-_jcBc5FUM30msVxslzCH9jA71H2KgtHksYN0bw%3D%3D?uid=0&filename=2022-04-03_20-30-09.png&disposition=inline&hash=&limit=0&content_type=image%2Fpng&owner_uid=0&tknv=v2&size=2048x2048">](Рейтинг_постов)

8. Обновить рейтинги пользователей.
```
>>> a1 = Author.objects.get(id=1)
>>> a1.update_rating()
>>> a1.ratingAuthor

# Liked a post:
>>> Post.objects.get(id=1).like()
>>> a1.update_rating()
>>> a1.ratingAuthor

>>> a2 = Author.objects.get(id=2)
>>> a2.update_rating()
>>> a2.ratingAuthor

```
9. Вывести username и рейтинг лучшего пользователя (применяя сортировку и возвращая поля первого объекта).
```
>>> best_author = Author.objects.order_by('-ratingAuthor')[:1]
>>> best_author
<QuerySet [<Author: Author object (1)>]>

>>> for i in best_author:
...     i.ratingAuthor
...     i.authorUser.username
... 
1
'Alexa'
```
10. Вывести дату добавления, username автора, рейтинг, заголовок и превью лучшей статьи, основываясь на лайках/дислайках к этой статье.
```
>>> best_article = Post.objects.order_by('-rating')[:1]
>>> best_article 
>>> for i in best_article:
>>>     i.dateCreation.strftime('%d-%m-%Y')
>>>     i.author.authorUser.username
>>>     i.rating
>>>     i.title
>>>     i.preview()
>>>     ar_id = i.id
'03-04-2022'
'Alexa'
2
'comment_by_author'
```
11. Вывести все комментарии (дата, пользователь, рейтинг, текст) к этой статье.
```
best_article_comments = Comment.objects.filter(commentPost=ar_id)
for i in best_article_comments:
	i.dateCreation.strftime("%d-%m-%Y")
	i.commentUser.username
	i.rating
	i.text
'03-04-2022'
'Alexa'
-2
'comment_by_author'
```
