from django.db import models



from django.template.defaultfilters import slugify

class Category(models.Model):
        name = models.CharField(max_length=25, unique=True)

        def __str__(self):
                return self.name




class Post(models.Model):
	
	frontimage=models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	title = models.CharField(max_length=255)
	subtitle1 = models.CharField(max_length=255 ,blank=True)
	body1 = models.TextField(blank=True)
	subtitle2 = models.CharField(max_length=255, blank=True)
	image1 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	subtitle3 = models.CharField(max_length=255, blank=True)
	body2 = models.TextField(blank=True)
	image2 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image3 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	subtitle4 = models.CharField(max_length=255, blank=True)
	image4 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image5 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image6 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image7 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image8 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image9 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image10 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image11 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image12 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image13 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body3 = models.TextField(blank=True)
	image14 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image15 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	image16 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	subtitle5 = models.CharField(max_length=255, blank=True)
	body4 = models.TextField(blank=True)
	subtitle6 = models.CharField(max_length=255, blank=True) 
	image17 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	subtitle7= models.CharField(max_length=255,blank=True)
	#upload_file = models.FileField(upload_to='files/', max_length=None, blank=True)
	body5 = models.TextField(blank=True)
	image18 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body5 = models.TextField(blank=True)
	image19 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body6 = models.TextField(blank=True)
	image20 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body7 = models.TextField(blank=True)
	image21 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body8 = models.TextField(blank=True)
	image22 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body9 = models.TextField(blank=True)
	image23 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	subtitle8 = models.CharField(max_length=255, blank=True)
	body10 = models.TextField(blank=True)
	image24 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body11 = models.TextField(blank=True)
	image25 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body12 = models.TextField(blank=True)
	image26 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body13 = models.TextField(blank=True)
	image27 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body14 = models.TextField(blank=True)
	image28 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body15 = models.TextField(blank=True)
	image29 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body16 = models.TextField(blank=True)
	image30 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	body17 = models.TextField(blank=True)
	image31 = models.ImageField(upload_to='images/', height_field=None, width_field=None, max_length=100, blank=True, null=True)
	created_on = models.DateTimeField(auto_now_add=True)
	last_modified = models.DateTimeField(auto_now=True)
	categories = models.ManyToManyField('Category', related_name='posts')
	def __str__(self):
		return self.title
    

    
class Comment(models.Model):
    author = models.CharField(max_length=60)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE)


