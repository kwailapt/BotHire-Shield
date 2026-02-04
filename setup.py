from setuptools import setup, find_packages

setup(
    name="shield-crewai-governance",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["crewai", "requests"],
    author="The Shield Protocol Team",
    description="Blockchain-based governance plugin for CrewAI agents."
)
