#first class functions. 
# A function is described as first class when it's treated in the realm of the prgramming languag as first class citizen. Meaning it can be returned, passed as an argument or assigned to a variable


def html_tag(tag):

	def wrap_text(msg):
		print('<{0}>{1}</{0}>'.format(tag, msg))

	return wrap_text

print_h1 = html_tag('h1')
print(">>> wrap_text unction is waiting to be execnted:",print_h1)

print_h1('Test Headline')
print_h1('Another line')


print_p = html_tag('p')
print_p('A paragraph test')