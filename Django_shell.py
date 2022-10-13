from News.models import *

# 1. Создать двух пользователей 

User.object.create_user('User_1')
User.object.create_user('User_2')

# 2. Создать два объекта модели Author, связанные с пользователем

Author.objects.create(user_id = 1)
Author.objects.create(user_id = 2)

# 3. Добавить 4 категории в модель Category

Category.objects.create(category = 'News')
Category.objects.create(category = 'Sport') 
Category.objects.create(category = 'History')
Category.objects.create(category = 'Education') 

# 4. Добавить 2 статьи и 1 новость

Post.objects.create(post_name = 'News_1', post_text = '10001010010001001111011010100101', type_post = 'news', user_id = 1)
Post.objects.create(post_name = 'Cool story', post_text = 'It is cool story, bro', type_post = 'article', user_id = 2) 
Post.objects.create(post_name = 'P', post_text = 'Very, very, very...', type_post = 'article', user_id = 1)

# 5. Присвоить им категории

PostCategory.objects.create(post_id = 1, category_id = 1)
PostCategory.objects.create(post_id = 2, category_id = 2)
PostCategory.objects.create(post_id = 2, category_id = 4) 
PostCategory.objects.create(post_id = 3, category_id = 3) 

# 6. Создать 4 комментария к разным объектам модели Post

Comment.objects.create(post_id =1, user_id =2, comment_text='oioioio')
Comment.objects.create(post_id =1, user_id =1, comment_text='uauauau')
Comment.objects.create(post_id =2, user_id =1, comment_text='uauau') 
Comment.objects.create(post_id =3, user_id =2, comment_text='bugaga') 

# 7. Применить функции like(), dislike(), скорректировать рейтинги объектов

Post.objects.get(id=1).rate1()		#4 раза
like			
Post.objects.get(id=1).rate1()
dislike
Post.objects.get(id=2).rate1()		#3 раза
like
Post.objects.get(id=2).rate1()
dislike
Post.objects.get(id=3).rate1()		#5 раз
like
Post.objects.get(id=3).rate1()		#2 раза
dislike
Comment.objects.get(id=1).rate2()	#4 раза
like
Comment.objects.get(id=1).rate2()
dislike
Comment.objects.get(id=2).rate2()	#2 раза
like
Comment.objects.get(id=3).rate2()
like
Comment.objects.get(id=4).rate2() 
like 

# 8. Обновить рейтинги пользователей

Author.objects.get(user_id = 1).update_rating()
Author.objects.get(user_id = 2).update_rating() 

# 9. Вывести username и рейтинг лучшего пользователя

Author.objects.all().order_by('-_rating').values('user', '_rating')[0]

# 10. Вывести дату добавления, автора, рейтинг, заголовок и превью лучшей статьи

Post.objects.all().order_by('-rating').values('publication_date', 'author', 'rating', 'post_name')[0]  
best_post = Post.objects.all().order_by('-_rating')[0]
best_post.preview()

# 11. Вывести все комментарии к этой статье

Comment.objects.filter(post = best_post).values('pub_time', 'user', '_rating', 'text')