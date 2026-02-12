# ⚡ Open Terminal

A lightweight API for running shell commands remotely — with real-time streaming and secure access.

## Getting Started

### Docker (recommended)

```bash
docker run -p 8000:8000 -e OPEN_TERMINAL_API_KEY=your-secret-key ghcr.io/open-webui/open-terminal
```

If no API key is provided, one is auto-generated and printed on startup.

### Build from Source

```bash
docker build -t open-terminal .
docker run -p 8000:8000 open-terminal
```

## Usage

### Run a Command

```bash
curl -X POST http://localhost:8000/execute \
  -H "Authorization: Bearer <api-key>" \
  -H "Content-Type: application/json" \
  -d '{"command": "echo hello"}'
```

### Stream Output

```bash
curl -X POST "http://localhost:8000/execute?stream=true" \
  -H "Authorization: Bearer <api-key>" \
  -H "Content-Type: application/json" \
  -d '{"command": "for i in 1 2 3; do echo $i; sleep 1; done"}'
```

Output streams as JSONL:

```jsonl
{"type": "stdout", "data": "1\n"}
{"type": "stdout", "data": "2\n"}
{"type": "stdout", "data": "3\n"}
{"type": "exit", "data": 0}
```

### Download a File

```bash
curl "http://localhost:8000/files?path=/tmp/output.csv" \
  -H "Authorization: Bearer <api-key>"
```

Returns a temporary download link (valid for 5 minutes, no auth needed):

```json
{"url": "http://localhost:8000/files/download/a1b2c3d4..."}
```

## API Docs

Interactive API documentation is available at [http://localhost:8000/docs](http://localhost:8000/docs).

## License

MIT — see [LICENSE](LICENSE) for details.
