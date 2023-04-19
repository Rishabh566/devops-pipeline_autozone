from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField

# Create your models here.
class Car(models.Model):

	city_choice = (
		  ('Carlow','Carlow'),
		  ('Cavan','Cavan'),
		  ('Clare','Clare'),
		  ('Cork','Cork'),
		  ('Donegal','Donegal'),
		  ('Dublin','Dublin'),
		  ('Galway','Galway'),
		  ('Kerry', 'Kerry'),
		  ('Kildare','Kildare'),
		  ('Kilkenny','Kilkenny'),
		  ('Laois','Laois'),
		  ('Leitrim','Leitrim'),
		  ('Limerick','Limerick'),
		  ('Longford','Longford'),
		  ('Louth','Louth'),
		  ('Mayo','Mayo'),
		  ('Meath','Meath'),
		  ('Monaghan','Monaghan'),
		  ('Offaly', 'Offaly'),
		  ('Roscommon','Roscommon'),
		  ('Sligo','Sligo'),
		  ('Tipperary NR','Tipperary NR'),
		  ('Tipperary SR','Tipperary SR'),
		  ('Waterford','Waterford'),
		  ('Westmeath','Westmeath'),
		  ('Wexford','Wexford'),
		  ('Wicklow','Wicklow'),
		  ('Dublin2','Dublin2'),
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

	condition_choices = (
		  ('Excellent', 'Excellent'),
		  ('Fair', 'Fair'),
		  ('Good', 'Good'),
		  ('Like New', 'Like New'),
		  ('New', 'New'),
		  ('Salvage', 'Salvage'),
	 )

	fuel_choices = (
		  ('Diesel', 'Diesel'),
		  ('Electric', 'Electric'),
		  ('Gas', 'Gas'),
		  ('Hybrid', 'Hybrid'),
		  ('Petrol', 'Petrol'),
		  ('Other', 'Other'),
	 )

	transmission_choices = (
		  ('Automatic', 'Automatic'),
		  ('Mannual', 'Mannual'),
	 )
	engine_choices = (
		  ('3 Cylinders', '3 Cylinders'),
		  ('4 Cylinders', '4 Cylinders'),
		  ('5 Cylinders', '5 Cylinders'),
		  ('6 Cylinders', '6 Cylinders'),
		  ('8 Cylinders', '8 Cylinders'),
		  ('10 Cylinders', '10 Cylinders'),
		  ('12 Cylinders', '12 Cylinders'),
		  ('Other Cylinders', 'Other Cylinders'),
	 )
	body_style_choices = (
		  ('Bus', 'Bus'),
		  ('Convertible', 'Convertible'),
		   ('Coupe', 'Coupe'),
		   ('Hatchback', 'Hatchback'),
		  ('Mini-Van', 'Mini-Van'),
		  ('Offroad', 'Offroad'),
		  ('Pickup', 'Pickup'),
		  ('SUV', 'SUV'),
		  ('Sedan', 'Sedan'),
		  ('Truck', 'Truck'),
		  ('Van', 'Van'),
		  ('Wagon', 'Wagon'),
		  ('Others', 'Others'),
	 )


	car_title= models.CharField(max_length=200)
	city = models.CharField(choices=city_choice, max_length=100)
	country = models.CharField(default='Ireland', max_length=100)
	color = models.CharField(max_length=100)
	model = models.CharField(max_length=100)
	year = models.IntegerField(('year'), choices=year_choice)
	condition = models.CharField(choices=condition_choices, max_length=100)
	price = models.IntegerField()
	description = RichTextField()
	car_photo = models.ImageField(upload_to='photos/%Y/%M/%d/')
	car_photo1 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo2 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo3 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	car_photo4 =models.ImageField(upload_to='photos/%Y/%M/%d/', blank=True)
	features = MultiSelectField(choices=features_choices)
	body_style = models.CharField(choices=body_style_choices ,max_length=100)
	engine = models.CharField(choices=engine_choices ,max_length=100)
	transmission = models.CharField(choices=transmission_choices ,max_length=100)
	interior = models.CharField(max_length=100)
	miles = models.IntegerField()
	doors = models.CharField(choices=door_choices,max_length=10)
	passengers = models.IntegerField()
	vin_no = models.CharField(max_length=100)
	milage = models.IntegerField()
	fuel_type = models.CharField(choices=fuel_choices ,max_length=50)
	no_of_owners = models.CharField(max_length=100)
	is_featured = models.BooleanField(default=False)
	created_date = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.car_title