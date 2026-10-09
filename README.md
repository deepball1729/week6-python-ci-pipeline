# Week 6 Task: Integrating Continuous Integration (CI) in Python Projects

A small, self-contained Python project demonstrating CI with **GitHub Actions**, **Ruff** linting, **pytest**, and **coverage reports**.

## Project overview

The sample package, `calculator`, provides a few basic arithmetic functions. The goal is not the calculator itself; it is to demonstrate a clean project structure and an automated quality-check pipeline that can be adapted to another Python project.

## Project structure

```text
week6_ci_python_project/
├── .github/
│   └── workflows/
│       └── ci.yml
├── src/
│   └── calculator/
│       ├── __init__.py
│       └── operations.py
├── tests/
│   └── test_operations.py
├── .gitignore
├── pyproject.toml
├── requirements-dev.txt
└── README.md
```

## CI pipeline

The workflow in `.github/workflows/ci.yml` runs on every push and pull request targeting any branch. It:

1. Checks out the repository.
2. Sets up Python 3.11.
3. Installs the development dependencies.
4. Runs Ruff linting. A lint failure stops the job.
5. Runs pytest and creates JUnit XML plus coverage XML and HTML reports.
6. Uploads reports as a GitHub Actions artifact, even if tests fail.

The workflow uses `pytest --cov-fail-under=80`; the job fails if tests fail or coverage is below 80%. This sample currently has tests for normal inputs and edge cases. Reports are generated under `reports/` and uploaded as the `ci-test-reports` artifact.

## Run the checks locally

Use Python 3.11 or newer. From the project root:

### Windows (PowerShell)

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
ruff check .
pytest
```

### macOS / Linux

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements-dev.txt
ruff check .
pytest
```

To generate the same reports locally:

```bash
mkdir -p reports
pytest --junitxml=reports/junit.xml \
  --cov=calculator --cov-report=term-missing \
  --cov-report=xml:reports/coverage.xml \
  --cov-report=html:reports/htmlcov \
  --cov-fail-under=80
```

On Windows PowerShell, create the folder first with `New-Item -ItemType Directory -Force reports`.

## Set up GitHub Actions

1. Create a new GitHub repository.
2. Extract this ZIP archive and open a terminal in the extracted project folder.
3. Initialize Git and commit the files:

   ```bash
   git init
   git add .
   git commit -m "Add Python project and CI workflow"
   git branch -M main
   git remote add origin https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
   git push -u origin main
   ```

   Replace the example remote URL with your repository URL.

4. Open the repository on GitHub and select **Actions**. The workflow named **Python CI** should start after the push.
5. Open the run to inspect each step's logs. Under the run's **Artifacts** section, download `ci-test-reports` to inspect the JUnit and coverage reports.

## Verify that CI triggers

After the first successful run, make a small change (for example, edit a docstring in `src/calculator/operations.py`), then run:

```bash
git add .
git commit -m "Verify CI trigger"
git push
```

Open **Actions** again and confirm a new run appears for the new commit. For a deliberate failure test, temporarily change an expected result in a test, commit and push it, and verify that the test step fails. Revert the test change and push again; the pipeline should return to green.

**Important:** CI cannot be triggered or verified against your GitHub account from this ZIP alone. Complete the repository setup and push steps above, then add your own Actions screenshot or run URL here as evidence. Do not claim a remote run succeeded until you have observed it.

## How the pipeline protects code quality

- **Ruff:** detects common Python style and correctness issues.
- **pytest:** executes automated unit tests.
- **Coverage threshold:** prevents the pipeline from passing if measured coverage falls below 80%.
- **JUnit XML and coverage reports:** provide machine-readable test results and coverage details.
- **Fail-fast behavior:** lint or test failures produce a non-zero exit code, making the workflow fail.
- **Pull-request checks:** the same workflow runs before changes are merged.

## Challenges and troubleshooting

These are common issues to check if a run fails; they are not claims that these issues occurred during a remote run.

- **Import errors:** the workflow installs the project in editable mode (`pip install -e .`) through `requirements-dev.txt` and `pyproject.toml`, so `src/` package imports resolve consistently.
- **Dependency or Python-version differences:** use the workflow's Python version locally when investigating failures.
- **Lint failures:** run `ruff check .` locally and fix the reported file and line.
- **Coverage below threshold:** inspect the terminal coverage summary and add tests for uncovered behavior, or adjust the threshold only when justified.
- **Missing report artifact:** inspect the test step logs. The artifact upload step uses `if: always()` so reports can still be uploaded after a test failure, when files were created.
- **PowerShell directory creation:** use `New-Item -ItemType Directory -Force reports` instead of the Unix `mkdir -p` command.

## Replication checklist

- [ ] Install Python 3.11 or newer.
- [ ] Install dependencies from `requirements-dev.txt`.
- [ ] Run `ruff check .` and `pytest` locally.
- [ ] Push the project to GitHub.
- [ ] Confirm a run appears under **Actions**.
- [ ] Download and inspect the `ci-test-reports` artifact.
- [ ] Capture a screenshot of a successful run and add it to the submission if required by your instructor.

## Submission note

This archive includes the source code, tests, CI workflow, and setup documentation. The remote GitHub Actions run and screenshot must be completed by the submitter after pushing to their own GitHub repository.
