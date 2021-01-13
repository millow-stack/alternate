import sys, os


global ext;
def start(x):
	ext = '.'+'';
	filename = x or input('Choose a name for your file: ')+ext;
	content_type = input('Enter the type of your file binary or text? [b/t]: ')
	if (len(filename and content_type) != 0 and content_type != 'b' or 't'):
		if (len(x) == 0):
			with open(filename, 'w'+content_type) as file:
				content = input('> ');
				file.write(content);
		else : 
			with open(filename, 'r'+content_type) as file:
				content = file.read();
				#some process with data from file.
				return content
	else :
		print('Invalid attempt, Please make sure all fields are filled.');
		exit();

def register():
	os.system('assoc '+ext+'=textfile')

try:
	start(sys.argv[1])
except Exception as e:
	raise