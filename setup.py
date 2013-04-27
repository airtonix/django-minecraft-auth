from setuptools import setup, find_packages

import minecraftauth as app

setup(name="django-minecraft-auth",
	version=app.__version__,
	description="Django authentication backend that tests against the minecraft authentication server.",
	author="Zenobius Jiricek",
	author_email="airtonix@gmail.com",
	packages=find_packages(),
	include_package_data=True,
	install_requires=[
		'django-appconf==0.4.1',
	],
)

