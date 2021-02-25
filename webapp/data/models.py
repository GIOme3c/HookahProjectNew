from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.timezone import now

class Profile(models.Model):
    user = models.OneToOneField(
        User, 
        on_delete = models.CASCADE
        )
    name = models.CharField(
        'Имя', 
        max_length= 20, 
        default='Имя',
        )
    famName = models.CharField(
        'Фамилия', 
        max_length= 20, 
        default='Фамилия',
        )
    fathName = models.CharField(
        'Отчество', 
        max_length= 20, 
        default='Отчество',
        )
    vk = models.URLField(
        'ВК', 
        default='vk.com/', 
        blank=True,
        )
    telegramNick = models.CharField(
        'Телеграмм', 
        default='NickName', 
        max_length=20, 
        blank=True,
        )
    date = models.DateField(
        'Дата приёма на работу',
        default= now(),
        #blank= True,
        )
    avatar = models.ImageField(
        'Аватар',
        blank = True,
        )

    def __str__(self):
        return self.name+' '+self.famName
    
    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Place(models.Model):
    title = models.CharField(
        'Название',
        max_length= 25,
        default= 'Заведение',
        )
    adres = models.CharField(
        'Адрес',
        max_length= 50,
        default='Ул. __, д. __',
        )
    preview = models.ImageField(
        'Превью',
        blank = True,
        )
   
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Заведение'
        verbose_name_plural = 'Заведения'

class Position(models.Model):
    title = models.CharField(
        'Название позиции',
        max_length=20,
        default='Simple',
        )
    cost = models.FloatField(
        'Стоимость позиции',
        default=23.0
        )

    def __str__(self):
        return self.title+' '+str(self.cost)
    
    class Meta:
        verbose_name = 'Позиция на продажу'
        verbose_name_plural = 'Позиции на продажу'

class MobilePhone(models.Model):
    staff = models.ForeignKey(
        Profile, 
        verbose_name='Сотрудник',
        on_delete = models.CASCADE,
        )
    number = models.CharField(
        'Номер',
        max_length=13,
        default='+375331234567',
        )

    def __str__(self):
        return self.staff.__str__()
    
    class Meta:
        verbose_name = 'Сотрудник и телефон'
        verbose_name_plural = 'Сотрудники и телефоны'

class Session(models.Model):
    staff = models.ForeignKey(
        Profile,
        verbose_name='Сортудник',
        on_delete = models.CASCADE,
        )
    place = models.ForeignKey(
        Place,
        verbose_name='Заведение',
        on_delete = models.CASCADE,
        )
    startTime = models.DateTimeField(
        'Время открытия смены',
        default=now(),
        )
    endTime = models.DateTimeField(
        'Время закрытия смены',
        default=now(),
        )
    isOpen = models.BooleanField(
        'Открыта ли смена',
        default=True,
        )
    
    def __str__(self):
        return self.place.__str__()+' '+self.staff.__str__()+' '+str(self.startTime.date())+' '+str(self.startTime.time())+'-'+str(self.endTime.date())+' '+str(self.endTime.time())
    
    class Meta:
        verbose_name = 'Смена'
        verbose_name_plural = 'Смены'
        get_latest_by = "endTime"

class Order(models.Model):
    session = models.ForeignKey(
        Session,
        on_delete = models.CASCADE,
        verbose_name= 'Смена',
        )
    position = models.ForeignKey(
        Position,
        on_delete = models.CASCADE,
        verbose_name= 'Позиция',
        )
    comment = models.TextField(
        'Комментарий',
        default=' ',
        blank=True,
        )
    
    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
    
    def __str__(self):
        return self.position.__str__()

class ItemCountType(models.Model):
    title = models.CharField(
        'Способ исчисления',
        max_length=10,
        default='г'
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип исчисления'
        verbose_name_plural = 'Типы исчисления'

class Item(models.Model):
    title = models.CharField(
        'Наименование',
        max_length=30,
        default=' ',
        )
    countType = models.ForeignKey(
        ItemCountType,
        verbose_name='Тип исчисления',
        on_delete = models.CASCADE,
        )
    
    def __str__(self):
        return self.title+', '+self.countType.__str__()

    class Meta:
        verbose_name = 'Позиция инвентаря'
        verbose_name_plural = 'Позиции инвентаря'

class StartSession(models.Model):
    session = models.ForeignKey(
        Session,
        verbose_name= 'Смена',
        on_delete = models.CASCADE,
        )
    item = models.ForeignKey(
        Item,
        verbose_name= 'Позиция',
        on_delete = models.CASCADE,
        )
    count = models.FloatField(
        'Количесвто',
        default=0,
        )
    
    class Meta:
        verbose_name = 'Начало смены'
        verbose_name_plural = 'Начала смен'

    def __str__(self):
        return self.session.__str__()+' '+self.item.__str__()+' '+str(self.count)

class EndSession(models.Model):
    session = models.ForeignKey(
        Session,
        verbose_name= 'Смена',
        on_delete = models.CASCADE,
        )
    item = models.ForeignKey(
        Item,
        verbose_name= 'Позиция',
        on_delete = models.CASCADE,
        )
    count = models.FloatField(
        'Количесвто',
        default=0,
        )
    
    class Meta:
        verbose_name = 'Окончание смены'
        verbose_name_plural = 'Окончания смен' 
    
    def __str__(self):
        return self.session.__str__()+' '+self.item.__str__()+' '+str(self.count)

# class ImgForSession(models.Model):
#     session = models.ForeignKey(
#         Session,
#         verbose_name= 'Смена',
#         on_delete = models.CASCADE,
#         )
#     image = models.ImageField(
#         'Сопроводительное изображение',
#         )
#     class Meta:
#         verbose_name = 'Изображение для смены'
#         verbose_name_plural = 'Изображения для смен' 

class AddToSession(models.Model):
    session = models.ForeignKey(
        Session,
        verbose_name= 'Смена',
        on_delete = models.CASCADE,
        )
    item = models.ForeignKey(
        Item,
        verbose_name= 'Позиция',
        on_delete = models.CASCADE,
        )
    count = models.FloatField(
        'Количесвто',
        default=0,
        )
    
    class Meta:
        verbose_name = 'Привоз'
        verbose_name_plural = 'Пирвозы'
    
    def __str__(self):
        return self.item.__str__()+str(self.count)

class DeleteOnSession(models.Model):
    session = models.ForeignKey(
        Session,
        verbose_name= 'Смена',
        on_delete = models.CASCADE,
        )
    item = models.ForeignKey(
        Item,
        verbose_name= 'Позиция',
        on_delete = models.CASCADE,
        )
    count = models.FloatField(
        'Количесвто',
        default=0,
        )
    
    class Meta:
        verbose_name = 'Увоз'
        verbose_name_plural = 'Увозы'
    
    def __str__(self):
        return self.item.__str__()+str(self.count)