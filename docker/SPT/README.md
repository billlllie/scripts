# SPT Server
These docker scripts organize the build of server side only version of SPT from source code.
It is applicable to all platforms (as long as builds pass), and it solely separates server from all other client files.

## File Structure
```
SPT/
├── config/            # Configuration directories mounted into container
│   ├── BepInEx/       # BepInEx plugin framework files
│   ├── SPT_Data/      # Server data files (auto-populated if empty)
│   └── user/          # User-specific configuration
├── scripts/           # Build and runtime scripts
│   ├── Dockerfile     # Multi-stage build configuration
│   ├── docker-compose.yml # Runtime configuration
│   ├── dc.sh          # Docker compose wrapper script
│   ├── entrypoint.sh  # Container startup script
│   ├── prepare-server.sh # Server repository setup
│   └── cleanup-config.sh # Configuration cleanup
└── server/            # Server files (auto-populated by prepare-server.sh)
```

## Usage

### Prerequisites
- Docker and Docker Compose installed
- Git LFS installed (for server repository)

### Setup
1. Clone this repository
2. Run `./scripts/prepare-server.sh` to download server files
3. Configure any needed files in `config/` directories

### Running the Server
```bash
# Build and start container
bash scripts/dc.sh up -d --build

# Stop container
bash scripts/dc.sh down

# View logs
bash scripts/dc.sh logs -f
```

### Configuration
- Server configuration files are in `config/SPT_Data/Server/config/`
- Server mod files are in `config/user/mods/`

### Cleanup
To reset configuration files:
```bash
./scripts/cleanup-config.sh
```

## Script Details
- **dc.sh**: Wrapper for docker-compose commands. Pass any docker-compose arguments to it.
- **entrypoint.sh**: Handles container startup, ensures required files exist.
- **prepare-server.sh**: Clones/pulls server repository using Git LFS.
- **cleanup-config.sh**: Removes contents from user and SPT_Data directories.
