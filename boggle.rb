class Boggle_Die
	attr_reader :current_face
	def initialize
		@faces = []
		alphabet = "ABCDEFGHIJKLMNOPRSTUVWXYZ"
		alphabet = (alphabet.split("")+["Qu"]).shuffle
		6.times {|i| @faces.push(alphabet.pop)}
		@current_face = @faces[0]
	end
	
	def shuffle
		@current_face = @faces.sample
	end
end

class Boggle
	attr_reader :dice
	
	def initialize(size)
		@dice = []
		@size = size
		(@size**2).times {|i| @dice.push(Boggle_Die.new)}
	end
	
	def shuffle
		@dice.each {|d| d.shuffle}
	end
	
	def show_grid
		@size.times do |i|
			@dice.slice(i*@size, @size).each {|d| print(d.current_face + "\t")}
			puts()
		end
	end
end

game = Boggle.new(4)
while true
	game.shuffle
	puts()
	game.show_grid
	puts "\nRemember: Words must be 3+ characters formed from connecting dice!"
	break if gets().length > 1
end

#todo proper letter distribution
#1 point for 3-4, 5 for 2, 3 for 6, 5 for 7, 11 for 8+
#words are formed from neighboring cubes (adjacent or diagonal)
#go all out, include official dictionary