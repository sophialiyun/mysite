from django.db import models

class Post(models.Model):
	title = models.CharField(max_length=100)
	content = models.TextField(blank=True)
	photo = models.URLField(blank=True)
	location = models.CharField(max_length=100)
	create_at = models.DateTimeField(auto_now_add=True)     
	update_at = models.DateTimeField(auto_now=True)      

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )

    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    name = models.CharField(max_length=10)    
    birth = models.DateField()                
    Email = models.EmailField()   

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)


class Article(models.Model):
	title = models.CharField(max_length=128,unique=True)
	content = models.TextField()

	def __str__(self):
		return self.title

class Comment(models.Model):
	article = models.ForeignKey(Article,on_delete = models.CASCADE)
	content = models.CharField(max_length=128)

	def __str__(self):
		return self.article.title+'-'+str(self.id)
 		
