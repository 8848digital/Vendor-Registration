from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in vendor_registration/__init__.py
from vendor_registration import __version__ as version

setup(
	name="vendor_registration",
	version=version,
	description="Vendor can register based on that supplier/customer will be created. We will have workflow based field value update of Supplier/Customer.",
	author="Deepak Kumar",
	author_email="deepakkumar@8848digital.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
