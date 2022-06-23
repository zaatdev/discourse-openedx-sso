import io
import os
from setuptools import setup, find_packages

HERE = os.path.abspath(os.path.dirname(__file__))


def load_readme():
    with io.open(os.path.join(HERE, "README.md"), "rt", encoding="utf8") as f:
        return f.read()


setup(
    name="discourse-openedx-sso",
    version="0.0.1",
    url="https://github.com/zaatdev/discourse-openedx-sso",
    project_urls={
        "Code": "https://github.com/zaatdev/discourse-openedx-sso/tree/main/contrib/edx-platform",
        "Issue tracker": "https://github.com/zaatdev/discourse-openedx-sso/issues",
    },
    license="AGPLv3",
    author="Ghassan Maslamani",
    description="Open edX plugin app for integrating with discourse sso",
    long_description=load_readme(),
    packages=find_packages(exclude=["tests*"]),
    include_package_data=True,
    entry_points={
        "lms.djangoapp": [
            "discourse_openedx_sso = discourse_openedx_sso.apps:DiscourseOpenedxSSO"
        ],
    },
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)