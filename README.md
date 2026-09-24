# handh.dev

Software and infrastructure for Howeth & Harp, Bubba's Fireworks, and related companies.

## Architecture

```text
GitHub
   │
   │ push
   ▼
GitHub Actions
   │
   ▼
AWS
└── EC2
    ├── Docker containers
    │   ├── H&H Website
    │   ├── HHQ
    │   ├── Bubba's Website
    │   └── BubbasHQ
    │
    └── PostgreSQL
        └── EBS
             ├── daily backup → local server
             └── offsite backup → S3
```

## Repositories

| Repo | Purpose |
|---|---|
| `handh-infra` | AWS, OpenTofu, Ansible, server configuration |
| `HH-Website` | H&H public website + HHQ |
| `bubbas-website` | Bubba's public website |
| `bubbashq` | Bubba's operator application |

## Infrastructure

- One AWS EC2 server
- Docker Compose for application services
- PostgreSQL hosted on EC2
- Persistent data stored on EBS
- Automated GitHub deployments
- Daily database backups
- One repo per product; frontend/backend stay together when practical
