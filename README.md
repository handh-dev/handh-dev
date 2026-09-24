# handh.dev

technology and infrastructure for howeth and harp, bubbas fireworks, and related companies.

## architecture

```text
github
   │
   ▼
github actions
   │
   ▼
aws
└── ec2
    ├── docker containers
    │   ├── handh website
    │   ├── hhq
    │   ├── bubbas website
    │   └── bubbashq
    │
    └── postgresql
        └── ebs
             ├── daily backup → in-house server
             └── offsite backup → s3
```

## repositories

| repo | purpose |
|---|---|
| `handh-infra` | aws, opentofu, ansible, docker, and server configuration |
| `handh-website` | howeth and harp public website + hhq |
| `bubbas-website` | bubbas fireworks public website |
| `bubbashq` | bubbas operator application |

## infrastructure

- one aws ec2 server
- docker compose for application services
- postgresql hosted on ec2
- persistent data stored on ebs
- automated deployments through github actions
- daily database backups to the in-house server
- encrypted offsite backups to s3
- one repo per product
- frontend and backend stay together when practical

## philosophy

keep the system simple, cheap, portable, and automation-friendly.

important business functionality should be accessible through reusable application logic and APIs rather than existing only inside user interfaces. this keeps the platform ready for future cli, mcp, and ai integrations without building unnecessary infrastructure early.
