from django.db import models
from datetime import datetime

# Create your models here.
class Car(models.Model):

	state_choice = (
		  ('N0', 'Carlow'),
		  ('N1', 'Cavan'),
		  ('N2', 'Clare'),
		  ('N3', 'Cork'),
		  ('N4', 'Donegal'),
		  ('N5', 'Dublin'),
		  ('N6', 'Galway'),
		  ('N8', 'Kerry'),
		  ('N9', 'Kildare'),
		  ('NA', 'Kilkenny'),
		  ('NG', 'Laois'),
		  ('NI', 'Leitrim'),
		  ('NK', 'Limerick'),
		  ('NL', 'Longford'),
		  ('NM', 'Louth'),
		  ('NN', 'Mayo'),
		  ('NO', 'Meath'),
		  ('NP', 'Monaghan'),
		  ('NQ', 'Offaly'),
		  ('NR', 'Roscommon'),
		  ('NW', 'Sligo'),
		  ('NX', 'Tipperary NR'),
		  ('NY', 'Tipperary SR'),
		  ('NZ', 'Waterford'),
		  ('10', 'Westmeath'),
		  ('11', 'Wexford'),
		  ('12', 'Wicklow'),
	 )

	year_choice=[]
	for r in range(2000, (datetime.now().year+1)):
		year_choice.append((r,r))
	features_choices = (
		  ('Cruise Control', 'Cruise Control'),
		  ('Audio Interface', 'Audio Interface'),
		  ('Airbags', 'Airbags'),
		  ('Air Conditioning', 'Air Conditioning'),
		  ('Seat Heating', 'Seat Heating'),
		  ('Alarm System', 'Alarm System'),
		  ('ParkAssist', 'ParkAssist'),
		  ('Power Steering', 'Power Steering'),
		  ('Reversing Camera', 'Reversing Camera'),
		  ('Direct Fuel Injection', 'Direct Fuel Injection'),
		  ('Auto Start/Stop', 'Auto Start/Stop'),
		  ('Wind Deflector', 'Wind Deflector'),
		  ('Bluetooth Handset', 'Bluetooth Handset'),
	 )
	door_choices = (
		  ('2', '2'),
		  ('3', '3'),
		  ('4', '4'),
		  ('5', '5'),
		  ('6', '6'),
	 )
	car_title= models.CharField(max_length=200)
	state = models.CharField(choices=state_choice, max_length=100)
	city = models.CharField(max_length=100)
	color = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	year = models.IntegerField(('year'), choices=year_choice)
	condition = models.CharField(max_length=100)
	price = models.IntegerField()
	description = models.TextField(max_length=400)
	car_photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
	car_photo1 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo2 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo3 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo4 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	features = models.CharField(choices=features_choices ,max_length=100)
	body_style = models.CharField(max_length=100)
	engine = models.CharField(max_length=100)
	transmission = models.CharField(max_length=100)
	interior = models.CharField(max_length=100)
	miles = models.IntegerField()
	doors = models.CharField(choices=door_choices,max_length=100)
	passengers = models.IntegerField()
	vin_no = models.CharField(max_length=100)
	milage = models.IntegerField()
	fuel_type = models.CharField(max_length=100)
	no_of_owners = models.CharField(max_length=100)
	is_featured = models.BooleanField(max_length=100)
	created_date = models.DateTimeField(default=datetime.now, blank=True)