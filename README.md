# gandi-v5

CLI tool for [Gandi.net](https://www.gandi.net/) API v5.

- Manage domains, DNS records, email, SSL certificates, and organizations
- Multiple output formats: table, JSON, plain text
- Sandbox mode for safe testing
- Config file or environment variable authentication

## Quick Start

Run directly without installing:

```bash
uvx gandi-v5 --help
```

## Install

```bash
pip install gandi-v5
```

Or install from source:

```bash
pip install git+https://github.com/lyhcode/gandi-v5
```

## Authentication

Set your [Gandi Personal Access Token (PAT)](https://admin.gandi.net/organizations/account/pat):

```bash
export GANDI_PAT=your-token-here
```

Or save it to config:

```bash
gandi-v5 auth login
gandi-v5 auth status      # verify authentication
gandi-v5 auth set-org     # set default organization
gandi-v5 auth logout      # remove saved token
```

## Usage

```bash
# Domains
gandi-v5 domain list
gandi-v5 domain info example.com
gandi-v5 domain check myname.com

# DNS Records
gandi-v5 dns list example.com
gandi-v5 dns list example.com --type A --name www
gandi-v5 dns get example.com www A
gandi-v5 dns create example.com www A 1.2.3.4
gandi-v5 dns update example.com www A --value 5.6.7.8
gandi-v5 dns delete example.com www A
gandi-v5 dns export example.com

# Email Forwarding
gandi-v5 email forward list example.com
gandi-v5 email forward create example.com info user@gmail.com
gandi-v5 email forward delete example.com info

# Mailboxes
gandi-v5 email mailbox list example.com
gandi-v5 email mailbox info example.com <mailbox-id>

# SSL Certificates
gandi-v5 cert list
gandi-v5 cert info <cert-id>

# Organizations
gandi-v5 org list
gandi-v5 org info <org-id>
gandi-v5 org whoami

# Output formats
gandi-v5 -o json domain list
gandi-v5 -o plain domain list
gandi-v5 -o table domain list   # default
```

## Sandbox

Use `--sandbox` to test against the [Gandi Sandbox API](https://api.sandbox.gandi.net/docs/):

```bash
gandi-v5 --sandbox domain list
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
