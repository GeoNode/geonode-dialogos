from distutils.core import setup


setup(
    name = "dialogos",
    version = "0.6",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    description = "a flaggable comments app",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "https://github.com/GeoNode/geonode-dialogos",
    packages = [
        "dialogos",
        "dialogos.templatetags",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ]
)
