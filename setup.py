from distutils.core import setup


setup(
    name = "geonode-dialogos",
    version = "1.0",
    author = "Eldarion",
    author_email = "development@eldarion.com",
    maintaner = "Geonode Developers",
    maintainer_email = "geonode-devel@lists.osgeo.org",
    description = "a flaggable comments app",
    long_description = open("README.rst").read(),
    license = "BSD",
    url = "https://github.com/GeoNode/geonode-dialogos",
    packages = [
        "dialogos",
        "dialogos.templatetags",
        "dialogos.migrations",
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
