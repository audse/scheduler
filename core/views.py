from django.shortcuts import render, redirect
from .models import Worker, ScheduledWorker, Shift

# Create your views here.

def home_page(request):
	workers = Worker.objects.all()
	scheduled_shifts = ScheduledWorker.objects.all().order_by('shift')
	scheduled_workers = ScheduledWorker.objects.all().count()
	return render(request, 'home_page.html', {'workers':workers, 'scheduled_shifts':scheduled_shifts, 'scheduled_workers':scheduled_workers})

def set_schedule_page(request):
	shifts = Shift.objects.all()
	for shift in shifts:
		if shift.start_time > 12:
			shift.start_time -= 12
			shift.start_pm = True
			shift.start_am = False
		if shift.end_time > 12:
			shift.end_time -= 12
			shift.end_pm = True
			shift.end_am = False
	return render(request, 'set_schedule_page.html', {'shifts':shifts})

def add_shift(request):
	start_time = request.POST.get("start_time")
	end_time = request.POST.get("end_time")
	day = request.POST.get("day")
	part_time_workers = request.POST.get("part_time_workers")
	shift = Shift.objects.create(start_time=start_time, end_time=end_time, day=day, part_time_workers=part_time_workers)
	return redirect(set_schedule_page)

def delete_shift(request, pk):
	shift = Shift.objects.get(pk=pk)
	shift.delete()
	return redirect(set_schedule_page)

def add_worker_page(request):
	order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
	shifts = sorted(Shift.objects.all(), key = lambda p: order.index(p.day))
	for shift in shifts:
		if shift.start_time > 12:
			shift.start_time -= 12
			shift.start_pm = True
			shift.start_am = False
		if shift.end_time > 12:
			shift.end_time -= 12
			shift.end_pm = True
			shift.end_am = False
	return render(request, 'add_worker_page.html', {'shifts':shifts})

def add_worker(request):
	name = request.POST.get("name")
	availability = request.POST.getlist("availability[]")
	hours = request.POST.get("hours")
	if hours == "part":
		hours = 20
	else:
		hours = 40

	worker = Worker.objects.create(name=name, preferred_hours=hours)
	for shift in availability:
		worker.shift_availability.add(shift)
		worker.save()

	return redirect(home_page)

def generate_schedule(request):
	full_time_workers = Worker.objects.filter(preferred_hours=40)
	shifts = Shift.objects.filter(full_time_shift=True)

	for worker in full_time_workers:
		for shift in shifts:
			schedule = ScheduledWorker.objects.create(worker=worker, shift=shift)

	part_time_workers = Worker.objects.filter(preferred_hours=20)
	part_time_shifts = Shift.objects.filter(part_time_workers__gte=0)

	for shift in part_time_shifts:
		n = 1
		for worker in part_time_workers:
			if shift in worker.shift_availability.all():
				scheduled = ScheduledWorker.objects.filter(worker=worker)
				if scheduled.count() < 4:
					schdeule = ScheduledWorker.objects.create(worker=worker, shift=shift)
					if shift.part_time_workers == n:
						break
					else:
						n += 1

	scheduled_shifts = ScheduledWorker.objects.all().order_by('shift')

	return render(request, 'generate_schedule.html')

def delete_schedule(request):
	scheduled_shifts = ScheduledWorker.objects.all()
	scheduled_shifts.delete()
	return redirect(home_page)







