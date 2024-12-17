from setuptools import setup, find_packages

setup(
    name="crewai",
    version="0.1.0",
    description="Crew AI execution package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=["crewai","crewai-tools"],  # Add dependencies here
    entry_points={
        "console_scripts": [
            "crewai-run = main:run",
            "crewai-train = main:train",
            "crewai-replay = main:replay",
            "crewai-test = main:test",
        ],
    },
    python_requires=">=3.10",
)
