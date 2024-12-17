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
            "crewai-run = basicAgent.main:run",        # Correct path for main.py
            "crewai-train = basicAgent.main:train",    # Same correction
            "crewai-replay = basicAgent.main:replay",
            "crewai-test = basicAgent.main:test",
        ],
    },
    python_requires=">=3.10",
)
