# Tech stack

## Language and Framework

I've chosen Python with client-side Javascript for my submission: I wanted some type safety and I haven't been writing much Typescript of late, so this felt like a reasonable compromise.

- Flask: Python for the API and client-side Javascript for the webapp
- UV for managing Python

## Testing

I don't think there's anything controversial here. I like using `black` when writing Python: there are more pressing things to worry about than formatting so I really appreciate having an opinionated formatter. This is something I learned to appreciate when developing in Golang with `gofmt`.

- pytest for unit and api tests
- playwright for browser tests
- flake8 and black for python linting
- eslint for javascript linting