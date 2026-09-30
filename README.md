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
| `handh-infra` | rust operations/tooling, aws, opentofu, docker, and server configuration |
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

## language standard

rust is required for all non-application services and tooling: cli, operations,
mcp, collectors, dashboards, workstation setup, installers, deployment, backups,
recovery, and secret synchronization. shared implementations and tests live in
the [handh-infra cargo workspace](https://github.com/handh-dev/handh-infra).

application code stays with its product and framework. configuration stays in
its native format: opentofu, compose yaml, caddy, systemd, sql, and workflow yaml.
legacy deployment paths may be symlinks to rust binaries. custom infrastructure
logic belongs in rust. see the [full standard](https://github.com/handh-dev/handh-infra/blob/main/docs/rust-standard.md).

## philosophy

keep the system simple, cheap, portable, and automation-friendly.

important business functionality should be accessible through reusable application logic and APIs rather than existing only inside user interfaces. this keeps the platform ready for future cli, mcp, and ai integrations without building unnecessary infrastructure early.
