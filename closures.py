def html_tag(tag):
	def wrap_text(msg):
		print('<' + tag + '>' + msg + '</' + tag + '>')

	return wrap_text

html_tag('h1')('My name is adel')

#or

print_h1 = html_tag('h1')
print_h1('This is my message')

html_tag('b')("This is such a long text This is such a long textThis is such a long textThis is such a long textThis is such a long textThis is such a long textThis is such a long textThis is such a long textThis is such a long textThis is such a long text")
