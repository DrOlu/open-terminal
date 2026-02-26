"# Open Terminal - Windows Binary Build

This fork includes a GitHub Actions workflow to build Windows executables using Nuitka.

## Building Windows Binary

The workflow automatically builds on every push to main.

## Download

Download the latest Windows binary from the Actions artifacts.

## Usage

```bash
open-terminal.exe run --host 0.0.0.0 --port 8000 --api-key abc123
```

## Features

- Self-contained Windows executable (no Python required)
- Single file (~15-25 MB)
- Full REST API support
- Built with Nuitka for performance"