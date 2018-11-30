try: 
	from setuptools import setup
except: 
	from distutils.core import setup

config = {
	'description': 'My Project',
	'author': 'Adel Shehadeh',
	'url': 'URL to get it at.',
	'download_url': 'Where to download it at',
	'author_email': 'adel.sh@gmail.com',
	'version': '0.1',
	'install_requires': ['nose'],
	'packages': ['myproject'],
	'scripts': ['bin/myscript'],
	'name': 'projectname'
}

setup(**config)
