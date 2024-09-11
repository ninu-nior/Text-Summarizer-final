import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.0"
# repo name from git
REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "ninu-nior"
# the project name inside src is your source repo name
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "nehalsmantri@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small text summarizer project",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    packages=setuptools.find_packages(where="src"),
    package_dir={"": "src"},
)
