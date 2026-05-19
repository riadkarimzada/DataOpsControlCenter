# Design Decisions

## Why PostgreSQL?

I chose PostgreSQL because the project is meant to simulate a realistic data engineering dashboard. PostgreSQL is closer to production systems than SQLite and gives better practice with relational database design.

## Why FastAPI?

FastAPI is simple, modern, and works well for building REST APIs in Python. It also provides automatic OpenAPI documentation, which makes testing the backend easier.

## Why React and TypeScript?

React and TypeScript are useful for building dashboard-style developer tools. TypeScript also helps keep frontend data structures clearer.

## Why Docker Compose?

Docker Compose makes it easier to run the backend and database together without requiring manual PostgreSQL setup on every machine.