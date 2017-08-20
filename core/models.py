from __future__ import unicode_literals

from django.db import models

# Create your models here.

# class Employee(models.Model):
# 	name = models.CharField(max_length=140)

# 	mon_start = models.IntegerField(default=9,  blank=True, null=True)
# 	mon_end   = models.IntegerField(default=17, blank=True, null=True)

# 	tue_start = models.IntegerField(default=9,  blank=True, null=True)
# 	tue_end   = models.IntegerField(default=17, blank=True, null=True)

# 	wed_start = models.IntegerField(default=9,  blank=True, null=True)
# 	wed_end   = models.IntegerField(default=17, blank=True, null=True)

# 	thu_start = models.IntegerField(default=9,  blank=True, null=True)
# 	thu_end   = models.IntegerField(default=17, blank=True, null=True)

# 	fri_start = models.IntegerField(default=9,  blank=True, null=True)
# 	fri_end   = models.IntegerField(default=17, blank=True, null=True)

# 	preferred_hours = models.IntegerField()
# 	max_shift = models.IntegerField(default=8)

# 	def __str__(self):
# 		return self.name

# class ScheduledEmployee(models.Model):
# 	employee = models.ForeignKey('Employee')

# 	start_time = models.IntegerField()
# 	end_time = models.IntegerField()

# 	day = models.CharField(max_length=10, default="Monday")

# 	def __str__(self):
# 		return self.employee.name + "'s shift on " + self.day + " from " + self.start_time + " to " + self.end_time

class Shift(models.Model):
	day = models.CharField(max_length=10, default="Monday")
	start_time = models.IntegerField(default=9)
	end_time = models.IntegerField(default=13)

	part_time_workers = models.IntegerField(default=1)
	full_time_shift = models.BooleanField(default=False)

	def __str__(self):
		if self.start_time > 12:
			self.start_time -= 12
		if self.end_time > 12:
			self.end_time -= 12
		return self.day + "'s " + str(self.start_time) + " to " + str(self.end_time)

class Worker(models.Model):
	name = models.CharField(max_length=140)
	shift_availability = models.ManyToManyField('Shift', blank=True, null=True)

	preferred_hours = models.IntegerField()

	def __str__(self):
		return self.name

class ScheduledWorker(models.Model):
	worker = models.ForeignKey('Worker')
	shift = models.ForeignKey('Shift')

	def __str__(self):
		if self.shift.start_time > 12:
			self.shift.start_time -= 12
		if self.shift.end_time > 12:
			self.shift.end_time -= 12
		return self.worker.name + "'s shift on " + self.shift.day + " from " + str(self.shift.start_time) + " to " + str(self.shift.end_time)








