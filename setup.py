from setuptools import setup, find_packages
import subprocess
from pathlib import Path
from typing import List


def run_cmd(cmd):
    if isinstance(cmd, str):
        cmd = cmd.split(" ")
    return subprocess.check_output(cmd).decode(encoding="UTF-8").split("\n")


def get_greatest_version(versions: List[str]) -> str:
    versions = [list(map(int, v[1:].split("."))) for v in versions]
    greatest = None
    for v in versions:
        if greatest is None:
            greatest = v
        else:
            lower = False
            for i in range(len(v)):
                if len(greatest) < i + 1:
                    greatest = v
                    break
                if v[i] > greatest[i]:
                    greatest = v
                    break
                if v[i] < greatest[i]:
                    lower = True
                    break
            if not lower:
                greatest = v
    return f"v{'.'.join([str(s_) for s_ in greatest])}"


def get_last_tag() -> str:
    result = [v for v in run_cmd("git tag -l v*") if not v == ""]
    if len(result) == 0:
        run_cmd("git tag v0.1")
    result = [v for v in run_cmd("git tag -l v*") if not v == "" and v.startswith("v")]
    return get_greatest_version(result)


def get_nb_commits_until(tag: str) -> int:
    return len(run_cmd(f'git log {tag}..HEAD --oneline'))


def get_version() -> str:
    last_tag = get_last_tag()
    return f"{'.'.join(last_tag.split('.'))}.{get_nb_commits_until(last_tag)}"


# git_installed = subprocess.call('command -v git >> /dev/null', shell=True)
git_installed = 0
try:
    long_description = Path("README.md").read_text()
except UnicodeDecodeError:
    with open("README.md", "rb") as ifile:
        lines = [line.decode("utf-8") for line in ifile.readlines()]
        long_description = "".join(lines)

optional_requirements = {}
requirements = []
all_reqs = []

for afile in Path("").glob("*requirements.txt.txt"):
    if str(afile) == "requirements.txt.txt":
        requirements = afile.read_text().splitlines()
        all_reqs = list(set(all_reqs) | set(afile.read_text().splitlines()))
    else:
        option = afile.stem.replace("-requirements.txt", "")
        optional_requirements[option] = afile.read_text().splitlines()
        all_reqs = list(set(all_reqs) | set(optional_requirements[option]))

if len(optional_requirements) > 0:
    optional_requirements["all"] = all_reqs


version = None
if git_installed == 0:
    try:
        version = get_version()
        with open("VERSION.txt", "w") as vfile:
            vfile.write(version)
    except FileNotFoundError as e:
        pass
if version is None:
    # noinspection PyBroadException
    try:
        with open("VERSION.txt", "r") as vfile:
            version = vfile.readline()
    except:
        version = None


if __name__ == "__main__":
    setup(
        name="vector",
        version=version,
        install_requires=requirements,
        author="solal grimbert",
        author_email="solal.grimbet@gmail.com",
        include_package_data=True,
        description="implementation de la notion mathematique de vecteur",
        url="https://github.com/sosothek/vector",
        packages=find_packages(),
        package_data={
            "": ["*", ".*"]
        },
        python_requires=">=3.7",
        long_description=long_description,
        long_description_content_type="text/markdown"
    )
