from setuptools import setup, find_packages
import versioneer


setup(
    name="work_log",
    description="Add and manage tasks in a database",
    author="Alex Boag-Munroe",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    include_package_data=True,
    package_dir={"": "src"},
    packages=find_packages("src"),
    python_requires='~=3.6',
    install_requires=[
        "click >=7.0,<8.0",
        "SQLAlchemy>=1.2.16",
        "pendulum>=2.0.4,<3.0",
    ],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Office/Business :: Scheduling",
    ],
    entry_points={"console_scripts": ["work_log = work_log.run:cli"]},
)
