# handh.dev

technology and infrastructure for howeth and harp, bubbas fireworks, and related companies.

## current architecture

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
    │   ├── hhq (within handh website)
    │   ├── bubbashq
    │   ├── bubbas info links
    │   └── caddy
    │
    └── postgresql + app files
        └── encrypted ebs
             └── daily backup → encrypted s3
```

the second backup copy to an in-house server is planned; that server is not built yet. see the [cutover status](https://github.com/handh-dev/handh-infra/blob/main/docs/cutover-status.md) for current deployment and recovery evidence.

## repositories

| repo | purpose |
|---|---|
| `handh-infra` | aws, opentofu, ansible, docker, and server configuration |
| `handh-website` | howeth and harp public website + hhq |
| `bubbashq` | bubbas operator application |
| `bubbas-info-links` | bubbas info links and sparkler signup |
| `bubbas-website` | planned bubbas fireworks public website |
| `handh-mail` | mail architecture and operations plan |

## infrastructure

- one aws ec2 server
- docker compose for application services
- postgresql hosted on ec2
- persistent data stored on ebs
- automated deployments through github actions
- encrypted offsite backups to s3
- a second in-house backup destination is planned
- one repo per product
- frontend and backend stay together when practical

## philosophy

keep the system simple, cheap, portable, and automation-friendly.

important business functionality should be accessible through reusable application logic and APIs rather than existing only inside user interfaces. this keeps the platform ready for future cli, mcp, and ai integrations without building unnecessary infrastructure early.
