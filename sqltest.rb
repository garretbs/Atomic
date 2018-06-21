require 'sqlite3'

first_names = ["Robert", "Andress", "Paula", "Ferdinand"]
last_names = ["Sanchez", "White", "Thomson", "Bickerman"]
sex = ["Male", "Female", "Female", "Male"]
towns = ["Portsmouth", "New York", "Toronto", "Beijing"]
occupations = ["Plumber", "Psychiatrist", "Engineer", "Pianist"]
dog_names = ["Rex", "Sasha", "Fido", "Olette"]
dog_breeds = ["Cocker spaniel", "Mutt", "Husky", "Golden retriever"]

File.delete("example.sqlite")
db = SQLite3::Database.new("example.sqlite")

#db.execute("delete from people")
#db.execute("delete from dogs")

db.execute("create table people(id, name, age, sex, town, occupation, dog)")
db.execute("create table dogs(id, name, age, sex, breed)")

insert_person = "insert into people(id, name, age, sex, town, occupation, dog) values(?, ?, ?, ?, ?, ?, ?)"
insert_dog = "insert into dogs(id, name, age, sex, breed) values(?, ?, ?, ?, ?)"

i = 0
person_id = 0
dog_id = 0
first_names.each do |f|
	last_names.each do |l|
		db.execute(insert_dog, dog_id += 1, dog_names.sample, rand(15), sex.sample, dog_breeds.sample)
		db.execute(insert_person, person_id += 1, f+" "+l, rand(50)+20, sex[i], towns.sample, occupations.sample, dog_id)
	end
	i += 1
end

r = db.execute("select * from dogs order by name")
r.each {|p| puts p.inspect}

#todo: learn more advanced stuff. merge tables, separate tables, unique keys, etc.