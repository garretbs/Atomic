require 'roo'
require 'set'

excel = Roo::Excelx.new("livestock/2017 Buyers with address.xlsx")
sheet = excel.sheet(0)

names = sheet.column(12)
names = names.uniq.sort_by{|w| w.downcase}

output = File.new("buyer names.txt", "w")
names.each {|n| output.puts(n)}
output.close

puts "Done, exported " + names.size.to_s + " buyer names"
