# gandi-cli

CLI tool for [Gandi.net](https://www.gandi.net/) API.

- Manage domains, DNS records, email, SSL certificates, and organizations
- Multiple output formats: table, JSON, plain text
- Sandbox mode for safe testing
- Config file or environment variable authentication

## Quick Start

Run directly without installing:

```bash
uvx agent-gandi-cli gandi --help
```

## Install

```bash
pip install agent-gandi-cli
```

Or install from source:

```bash
pip install git+https://github.com/lyhcode/agent-gandi-cli
```

## Authentication

Set your [Gandi Personal Access Token (PAT)](https://admin.gandi.net/organizations/account/pat):

```bash
export GANDI_PAT=your-token-here
```

Or save it to config:

```bash
gandi auth login
gandi auth status      # verify authentication
gandi auth set-org     # set default organization
gandi auth logout      # remove saved token
```

## Usage

```bash
# Domains
gandi domain list
gandi domain info example.com
gandi domain check myname.com

# DNS Records
gandi dns list example.com
gandi dns list example.com --type A --name www
gandi dns get example.com www A
gandi dns create example.com www A 1.2.3.4
gandi dns update example.com www A --value 5.6.7.8
gandi dns delete example.com www A
gandi dns export example.com

# Email Forwarding
gandi email forward list example.com
gandi email forward create example.com info user@gmail.com
gandi email forward delete example.com info

# Mailboxes
gandi email mailbox list example.com
gandi email mailbox info example.com <mailbox-id>

# SSL Certificates
gandi cert list
gandi cert info <cert-id>

# Organizations
gandi org list
gandi org info <org-id>
gandi org whoami

# Output formats
gandi -o json domain list
gandi -o plain domain list
gandi -o table domain list   # default
```

## Sandbox

Use `--sandbox` to test against the [Gandi Sandbox API](https://api.sandbox.gandi.net/docs/):

```bash
gandi --sandbox domain list
```

## Configuration

Config file: `~/.config/gandi-cli/config.toml`

```toml
[auth]
pat = "your-token"

[defaults]
output = "table"
sharing_id = "your-org-id"
```

## Claude Code Skills

The `skills/` directory contains [Claude Code](https://claude.com/claude-code) skill files for developing and extending this CLI. They include API endpoint references, command patterns, and business rules for each Gandi API area.

## License

MIT
