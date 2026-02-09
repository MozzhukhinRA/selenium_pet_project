from faker import Faker

z = 1 + 2
print(z)

fake = Faker()
city_name = fake.city()
print(city_name)