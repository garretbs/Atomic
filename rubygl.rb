#this was made using ruby-opengl from https://github.com/vaiorabbit/ruby-opengl/
#following this tutorial http://www.opengl-tutorial.org/beginners-tutorials/

require 'opengl'
require 'glfw'

OpenGL.load_lib()
GLFW.load_lib()

include OpenGL
include GLFW

# Press ESC to exit.
key_callback = GLFW::create_callback(:GLFWkeyfun) do |window_handle, key, scancode, action, mods|
	if key == GLFW_KEY_ESCAPE && action == GLFW_PRESS
		glfwSetWindowShouldClose(window_handle, 1)
	end
end

if __FILE__ == $0
	glfwInit()
	
	glfwWindowHint(GLFW_SAMPLES, 4) #4x antialiasing
	#glfwWindowHint(GLFW_CONTEXT_VERSION_MAJOR, 3) #opengl 3.x
	#glfwWindowHint(GLFW_CONTEXT_VERSION_MINOR, 3) #opengl x.3
	#glfwWindowHint(GLFW_OPENGL_FORWARD _COMPAT, GL_TRUE) #for mac
	#glfwWindowHint(GLFW_OPENGL_PROFILE, GLFW_OPENGL_CORE_PROFILE) #prevent old ogl
	window = glfwCreateWindow(640, 480, "OpenGL Practice", nil, nil)
	glfwMakeContextCurrent(window) #initialize glfw
	glewExperimental = true #needed in core profile
	
	VertexArrayID = ' ' * 4
	glGenVertexArrays(1, VertexArrayID)
	vertArray = VertexArrayID.unpack('L')[0]
	glBindVertexArray(vertArray)
	
	tsize = 0.1
	
	g_vertex_buffer_data = [
		-tsize, -tsize, 0.0,
		tsize, -tsize, 0.0,
		0.0, tsize, 0.0
	]
	
	vertexbufferptr = ' ' * 4
	glGenBuffers(1, vertexbufferptr)
	vertexbuffer = vertexbufferptr.unpack('L')[0]
	glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer)
	glBufferData(GL_ARRAY_BUFFER, 4*g_vertex_buffer_data.size, g_vertex_buffer_data.pack('F*'), GL_STATIC_DRAW)
	
	width_ptr = ' ' * 8
	height_ptr = ' ' * 8
	glfwGetFramebufferSize(window, width_ptr, height_ptr)
	width = width_ptr.unpack('L')[0]
	height = height_ptr.unpack('L')[0]
	ratio = width.to_f/height.to_f
	glClearColor(0.0, 0.0, 0.4, 0.0)
	
	glViewport(0, 0, width, height)
	
	current_time = glfwGetTime()
	fps = 60.0
	sleep_time = 1.0/fps
	
	while glfwWindowShouldClose(window) == 0
		glClear(GL_COLOR_BUFFER_BIT)
		
		glEnableVertexAttribArray(0)
		glBindBuffer(GL_ARRAY_BUFFER, vertexbuffer)
		glVertexAttribPointer(
			0,			#attribute 0. No particular reason for 0, but must match the layout in the shader 
			3,			#size
			GL_FLOAT,	#type
			GL_FALSE,	#normalized?
			0,			#stride
			0			#array buffer offset
		)
		
		glDrawArrays(GL_TRIANGLES, 0, 3)
		glDisableVertexAttribArray(0)

		glLoadIdentity()
		glRotatef(glfwGetTime() * 45, 0.0, 0.0, 1.0)
		glColor3f(1.0, 0.0, 0.0)
		
		#puts((new_time = glfwGetTime()) - current_time)
		#current_time = new_time
		#sleep(sleep_time)

		glfwSwapBuffers(window)
		glfwPollEvents() #necessary to check if window is closed
	end


	glfwDestroyWindow(window)
	glfwTerminate()
end