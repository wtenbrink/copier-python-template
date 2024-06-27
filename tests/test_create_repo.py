from pathlib import Path

import yaml
from copier import Worker

REPO_ROOT = Path(__file__).parents[1]


def test_create_repo(tmp_path):
    """Test case for creating a new repository with copier, using the answers from test-repo-answers.yml."""

    with open(REPO_ROOT / "tests/test-repo-answers.yml") as f:
        test_answers = yaml.safe_load(f)
    copier_worker = Worker(
        src_path=REPO_ROOT.as_posix(),
        dst_path=tmp_path / "test_create_repo",
        data=test_answers,
        vcs_ref="HEAD",
    )
    copier_worker.run_copy()

    assert True
