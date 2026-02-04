from setuptools import setup, find_packages

setup(
    name="bothire-shield-sdk",
    version="0.4.2",
    author="Commander & Gemini Trinity-Navigator",
    packages=find_packages(),
    install_requires=[
        "web3>=6.0.0",
        "requests>=2.28.0",
        "eth-account>=0.8.0"
    ],
    python_requires='>=3.9',
)
