require 'sqlite3'



db = SQLite3::Database.new("eulogy.sqlite")

#db.execute("delete from people")
#db.execute("delete from dogs")

db.execute("create table skills(id, name, mp cost, damage formula)")
db.execute("create table weapons(id, name, attack)")
db.execute("create table actors(id, name, skills, weapon)")

insert_skill = "insert into skills(id, name, mp cost, damage formula) values(?, ?, ?, ?)"
insert_weapon = "insert into weapons(id, name, attack) values(?, ?, ?)"
insert_actor = "insert into actors(id, name, skills, weapon) values(?, ?, ?, ?)"

physical_damage_formula = "a.atk*%i-b.def*%i"
magical_damage_formula = "a.mat*%i-b.mdf*%i"

actor_id = 0
skill_id = 0
weapon_id = 0
db.execute(insert_skill, skill_id += 1, "Skill" rand(25), blahiboebejriejgb))

r = db.execute("select * from dogs order by name")
r.each {|p| puts p.inspect}

#todo: learn more advanced stuff. merge tables, separate tables, unique keys, add attributes to entry