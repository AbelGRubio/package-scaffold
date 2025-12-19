import shutil
from pathlib import Path

use_git = "{{ cookiecutter.use_git }}"

# Paths
gitlab_ci = Path(".gitlab-ci.yml")
github_actions = Path(".github")

if use_git == "gitlab":
    # Keep GitLab CI, remove GitHub Actions
    if github_actions.exists():
        shutil.rmtree(github_actions)
else:
    # Keep GitHub Actions, remove GitLab CI
    if gitlab_ci.exists():
        gitlab_ci.unlink()


use_config_file = "{{ cookiecutter.use_config_file }}"

config_dir = Path("config")

if use_config_file.lower() == "yes":
    # Keep GitLab CI, remove GitHub Actions
    if config_dir.exists():
        shutil.rmtree(config_dir)