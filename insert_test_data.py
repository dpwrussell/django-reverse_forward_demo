# Insert some test data
# python manage.py shell < insert_test_data.py

from demo.models import Car, Part, Manufacturer

car = Car(name='Dune Buggy')
car.save()

manufacturer1 = Manufacturer(name='Froggy')
manufacturer1.save()
manufacturer2 = Manufacturer(name='Spidey')
manufacturer2.save()

part1 = Part(name='wheel', car=car, manufacturer=manufacturer1)
part1.save()

part2 = Part(name='suspension', car=car, manufacturer=manufacturer2)
part2.save()