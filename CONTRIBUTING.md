# Contributing to Quibble

Thank you for your interest in contributing to Quibble! We’re excited to build a respectful and engaging platform together. Please follow these guidelines to make the process smooth and efficient.

## Getting Started

1. **Fork the Repository**\
   Start by forking the [Quibble repository](https://github.com/quibble-dev/Quibble).

3. **Clone Your Fork**
   ```bash
   git clone https://github.com/your-username/Quibble.git
   cd Quibble
   ```

4. **Set Up Environment**\
   Install the required tools for both the backend and frontend.\
   `backend`: [`poetry`](https://python-poetry.org/)\
   `frontend`: npm

5. **Setup Pre-commit Hooks**\
   Quibble uses `pre-commit` hooks to automate code quality checks. Before you start contributing, please ensure the following steps are completed to install and configure the pre-commit hooks.

    If you don't have `pre-commit` installed, you can run the following Python script to install it:

    ```bash
    python3 ./scripts/pre-commit.py
    ```
## Project Structure

- `backend` - Django app.
- `frontend` - Svelte/kit app.
- `docker` - Container files for docker apps.

## Setting Up the Backend (Django)

1. **Navigate to the Backend Directory**
   ```bash
   cd backend
   ```

2. **Install Dependencies with Poetry**
   ```bash
   poetry install
   ```

3. **Set Up Environment Variables**\
   Copy `.env.example` to `.env` and update environment variables as needed.

4. **Run Database Migrations**
   ```bash
   poetry run poe mksync
   poetry run poe sync
   # if you have poethepoet installed
   poe mksync && poe sync
   ```

5. **Start the Development Server**
   ```bash
   poetry run poe dev
   # if you have poethepoet installed
   poe dev
   ```

## Run postgresql db server

You can run postgres on background and create a database called `quibble_db` (default) or whatever you specific in `backend/.env`.\
Or you can run this docker/podman container with:

```bash
# podman
podman compose -f docker/compose-db.yml up --build
# docker
docker compose -f docker/compose-db.yml up --build
```

Add `-d` if you want to run it on detatched mode.

## Setting Up the Frontend (Svelte/kit)

1. **Navigate to the Frontend Directory**
   ```bash
   cd frontend
   ```

2. **Install Dependencies**
   ```bash
   npm install
   ```

3. **Run the Development Server**
   ```bash
   npm run dev
   ```

## Making Changes

1. **Create a New Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**\
   Ensure your changes adhere to the project’s coding standards.

3. **Lint and Format Your Code**
   - For the backend, ensure your code meets PEP8 standards.
   - For the frontend, use ESLint and Prettier.

4. **Write Tests**\
   Aim to write tests for any new functionality.

5. **Run Tests**
   - **Backend**: Run tests with `poetry run pytest`
   - **Frontend**: Run tests with `npm test`

6. **Commit Your Changes**\
   Use meaningful commit messages:

   ```bash
   git commit -m "Add feature description"
   ```

7. **Push Your Changes**
   ```bash
   git push origin feature/your-feature-name
   ```

## Submitting a Pull Request

1. **Open a Pull Request**\
   Go to the Pull Requests tab on GitHub and open a new PR.

2. **Describe Your Changes**\
   Clearly describe the changes you made and link any relevant issues.

3. **Request a Review**\
   Tag project maintainers or team members for a review.

## Code of Conduct

Please respect others and foster a welcoming environment. We expect all contributors to adhere to the [Code of Conduct](https://github.com/quibble-dev/Quibble/blob/main/CODE_OF_CONDUCT.md).

## Additional Notes

- **Documentation**: Ensure new features or changes are documented.
- **Commit Hygiene**: Keep your commit history clean; squash commits if necessary.

Thank you for contributing to Quibble! We look forward to your input.
