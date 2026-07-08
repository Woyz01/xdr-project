# Contributing to XDR Project

Thank you for your interest in contributing to the XDR project! This document provides guidelines and instructions for contributing.

## Code of Conduct

Be respectful, inclusive, and professional. Harassment will not be tolerated.

## Getting Started

1. Fork the repository
2. Clone your fork locally
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Development Guidelines

### Code Style

**Python:**
- Follow PEP 8
- Use type hints
- Use `black` for formatting
- Use `pylint` for linting

```bash
black core/ api/ models/ agents/
pylint core/ api/ models/ agents/
```

**TypeScript/JavaScript:**
- Use ESLint for linting
- Use Prettier for formatting
- Use TypeScript strict mode

```bash
npm run lint
npm run format
```

### Commit Messages

- Use present tense: "Add feature" not "Added feature"
- Use imperative mood: "Move cursor to..." not "Moves cursor to..."
- Limit to 50 characters for the first line
- Reference issues when applicable: "Fixes #123"

### Pull Request Process

1. Update documentation for any new features
2. Add tests for new functionality
3. Ensure all tests pass: `make test`
4. Keep PRs focused on a single concern
5. Provide clear description of changes
6. Link related issues

## Testing

All contributions must include tests.

### Backend Tests

```bash
cd backend
pytest
```

### Frontend Tests

```bash
cd frontend
npm test
```

### Coverage

Aim for at least 80% code coverage.

```bash
cd backend
pytest --cov
```

## Documentation

Update relevant documentation:

- `docs/README.md` - General documentation
- `docs/ARCHITECTURE.md` - Architecture changes
- `docs/API.md` - API changes
- `docs/SETUP.md` - Setup/installation changes
- Code comments for complex logic
- Docstrings for all functions and classes

## Reporting Issues

When reporting issues:

1. Check if the issue already exists
2. Include a clear description
3. Provide steps to reproduce
4. Include environment information
5. Attach logs or error messages
6. Use the appropriate label/tag

## Feature Requests

For feature requests:

1. Clearly describe the feature
2. Explain the use case
3. Provide examples if possible
4. Discuss implementation approach

## Questions?

- Open an issue for questions
- Check existing documentation
- Review closed issues for answers

## License

By contributing, you agree your code will be licensed under the MIT License.
