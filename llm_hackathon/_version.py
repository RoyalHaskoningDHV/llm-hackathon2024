__version__ = "1.0.0"

# This is used in all build/* branches, during a build like that we:
# Remove the version above: sed -i '/__version__/d' aqsml_mine/_version.py
# Rename this to 'version': sed -i 's/__dev_version__/__version__/g' aqsml_mine/_version.py
# Tested valid versions for python are 0.2.15.dev0, 0.2.15.dev2, 0.2.15.dev46 etc.
__dev_version__ = "1.0.0.dev0"
