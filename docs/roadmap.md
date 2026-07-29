# Roadmap

1. **Foundation** - project scaffolding and basic site shell
  - UV for python/flask
  - `GET /` that renders `<h1>Hello World</h1>
  - Dockerized 
  - Makefile with a `make run` action
  - Update README.md (how to install & run)
2. **Testing & linting** - unit and browser tests
  - pytest for unit and api tests
  - playwright for browser tests
  - flake8 and black for python linting
  - eslint for javascript linting
  - Makefile actions: `make lint`, `make test`, `make api-test` and `make browser-test`
  - Add browser test
  - Update README.md (how to lint & test)
3. **API backend** - new route `POST /api/quote` (api-key requirement)
4. **Security** - api-key presentation & validation
5. **Functional frontend** - basic form that uses `fetch` to call the API with the required parameters
6. **Simulation** - have `/api/quote` occasionally (randomly) throw an error
7. **Improved frontend** - introduce a react app for frontend responsibilities