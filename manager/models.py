from django.db import models
# from django.db.models.signals import post_save
from django.conf import settings

# class Admin(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

#     def __str__(self):
#         return str(self.user.username)

# def post_save_user_model_receiver(sender, instance, created, *args, **kwargs):
#     if created:
#         try:
#             Admin.objects.create(user=instance)
#         except:
#             pass

# post_save.connect(post_save_user_model_receiver, sender=settings.AUTH_USER_MODEL)

def Interndocs(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'intern_{0}/{1}'.format(instance.id, filename)
# def Internimg(instance,filename):
# 	return 'intern_{0}/{1}'.format(instance.id, filename)

class Intern(models.Model):
	admin = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='internadmin',on_delete=models.CASCADE)
	fullname=models.CharField(max_length=20)
	email=models.EmailField()
	phone=models.CharField(max_length=13)
	profilepic=models.ImageField(upload_to=Interndocs)
	document = models.FileField(upload_to=Interndocs)
	stipend=models.FloatField()
	date_of_join = models.DateField()
	date_of_leave = models.DateField()
	admin_remark=models.TextField()
	status=models.BooleanField(default=False)

	def __str__(self):
		return self.fullname