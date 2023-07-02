# Slides

This repo contains slides from public talks.
So far, we mostly use [Marp](https://marp.app) for building slide decks.

Marp renders markdown code into HTML or PDF.

## Working on VS Code

One only needs to install the relevant
[extension](https://github.com/marp-team/marp-vscode), which works out of the
box.

## CLI

I have supplied a setup in a `docker-compose.yaml`.
By default, it serves the root folder as a service on `localhost:8080`.

In order to start the service:

```bash
docker compose up -d
```

Perhaps the fastest way to build the slide deck into static HTML is to invoke
the CLI tool with `npx`:

```bash
npx @marp-team/marp-cli@latest slides.md
```

## Deployment instructions

This repository is cloned as a submodule in ber2.github.io.
In order to publish some slides:

- Push changes to the `main` branch in this repo.
- Pull changes in the `ber2.github.io/slides` repo submodule.

