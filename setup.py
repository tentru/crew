from setuptools import setup, find_packages

def load_requirements():
    with open("requirements.txt", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip() and not line.startswith("#")]

setup(
    name="crewai",
    version="0.1.0",
    description="Crew AI execution package",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    packages=find_packages(),  
    package_dir={"": "basicAgent"},
    install_requires=load_requirements(),  
    entry_points={
        "console_scripts": [
            "crewai-run = basicAgent.main:run",
            "crewai-train = basicAgent.main:train",
            "crewai-replay = basicAgent.main:replay",
            "crewai-test = basicAgent.main:test",
        ],
    },
    python_requires=">=3.10",
)
