from django.db import models
from django.urls import reverse
# Create your models here.

#글 분류 (일상,유머,정보)
class Category(models.Model):
    name=models.CharField(max_length=50,help_text="블로그 분류")    #글 삽입을 위한 CharField모듈, 최대글수는 50

    def __str__(self):
        return self.name
#블로그 글(제목,작성일,대표 이미지,내용,분류)
class Post(models.Model):
    title=models.CharField(max_length=200)
    title_image=models.ImageField(blank=True)       #이미지 삽입을 위한 모듈 ImageField, 빈 이미지일수도 있으니 blank=Ture
    content=models.TextField()                #글의 내용(매우 길수가 있으니 TextField)
    createDate=models.DateTimeField(auto_now_add=True)      #글의 작성일(날짜를 자동으로)
    updateDate=models.DateTimeField(auto_now_add=True)      #글 수정한 경우(날짜를 자동으로)
    category=models.ManyToManyField(Category,help_text="글의 분류를 설정하세요.")   #글의 분류(하나의 글이 여러가지 분류에 해당할수 있다.->다대다 관계)

    def __str__(self):
        return self.title
    #1번글의 경우->post/1
    def get_absolute_url(self):
        return reverse("post",args=[str(self.id)])
    #내용이 40자가 넘으면
    def is_content_more40(self):
        return len(self.content) > 40
    #내용을 40자로 자른다
    def get_content_under40(self):
        return self.content[:40]