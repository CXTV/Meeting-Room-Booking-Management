from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=32, verbose_name='用户名', unique=True)
    password = models.CharField(max_length=64, verbose_name='密码')

    class Meta:
        verbose_name_plural = '用户表'

    def __str__(self):
        return self.name


class MeetingRoom(models.Model):
    name = models.CharField(max_length=32, verbose_name='会议室名称')
    num = models.IntegerField(verbose_name='容纳人数')
    addr = models.CharField(max_length=64, verbose_name='会议室地址')

    class Meta:
        verbose_name_plural = '会议室表'

    def __str__(self):
        return self.name

class Booking(models.Model):
    user_info = models.ForeignKey(to='User', verbose_name='用户')
    room_info = models.ForeignKey(to='MeetingRoom', verbose_name='会议室')
    booking_date = models.DateField(verbose_name='预定日期')
    time_choices = (
        (1, '8:00-9:00'),
        (2, '9:00-10:00'),
        (3, '10:00-11:00'),
        (4, '11:00-12:00'),
        (5, '12:00-13:00'),
        (6, '13:00-14:00'),
        (7, '14:00-15:00'),
        (8, '15:00-16:00'),
        (9, '16:00-17:00'),
        (10, '17:00-18:00'),
        (11, '18:00-19:00'),
        (12, '19:00-20:00'),
        (13, '20:00-21:00'),
    )
    booking_time = models.IntegerField(choices=time_choices, verbose_name='预定时间段')

    class Meta:
        verbose_name_plural = '预定关系表'
        unique_together = (
            ('room_info', 'booking_date', 'booking_time')
        )
