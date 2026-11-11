# handh.dev

digital infrastructure that feels magical.

handh.dev builds and runs the technical side of howeth and harp, bubbas fireworks, fat man wholesale, and related companies.

## mission

the owner says what a company needs in plain words, and it is live. no code, no approvals, no waiting, and anything can be undone.

every piece of work is judged by one test: did it shorten the distance between the owner saying something and it being real?

## principles

1. **agents first.** agents build, merge, deploy, fix and maintain everything, on their own authority. nothing technical waits on a person. see [decision 1](docs/adr/0001-agents-act-without-approval.md).
2. **undo replaces approval.** safety comes from being able to reverse anything quickly. the one thing nobody can touch, agent or owner, is the protected backups.
3. **the owner gives outcomes.** what is wanted, a reaction to the visible result, and business calls. never how it is built. see [decision 2](docs/adr/0002-owner-gives-outcomes-and-business-calls.md).
4. **new costs are the owner's call.** anything that adds a line to the bill stops and waits.
5. **ship, check live, undo if unhealthy.** short outages are acceptable. the same way of working applies every day, for every company. see [decision 3](docs/adr/0003-ship-then-undo.md).
6. **every service looks the same.** adding, removing, deploying and checking a service is the same command for all of them, wherever its code lives.
7. **simple, cheap, portable.** one server, proven tools, nothing built that can be borrowed.
8. **say what is true now.** documents describe the present. history lives in git.

the shared vocabulary is in [CONTEXT.md](CONTEXT.md). use those words and avoid the ones it lists.

## how it runs

- one aws ec2 server, created with opentofu
- each service is a container, run with docker compose
- caddy handles https and sends each web address to its service
- one postgresql server, with a database per service
- backups go offsite to s3

## where it stands

the principles above were set on november 10, 2026. the system does not match them yet. known gaps, all in `handh-infra`:

- agents are limited to read-only access to production
- each service is written into the tooling by hand, so adding one means writing code
- releases run from one prepared workstation
- a routine release takes about two minutes, most of it checks before shipping
- backups are not yet protected from deletion
- many documents are dated records of past approvals

[docs/local-sdlc.md](docs/local-sdlc.md) describes how releases work today and is superseded by the decisions above.

## repositories

| company | repo | what it is |
|---|---|---|
| handh.dev | `handh-dev` | mission, principles, vocabulary, decisions, brand |
| handh.dev | `handh-infra` | the server, its configuration, and the tooling that runs services |
| handh.dev | [`handh-email`](https://github.com/handh-dev/handh-email) | hosted email dashboard, provider plan, and operating guidance |
| howeth and harp | `handh-website` | public website and hhq |
| howeth and harp | `hh-wiki` | private standards wiki |
| bubbas fireworks | `bubbas-mono` | maintained bubba applications |
| bubbas fireworks | `bubbas` | service map and architecture notes |
| bubbas fireworks | `bubbas-website` | public website |
| bubbas fireworks | `bubbashq` | operator application |
| bubbas fireworks | `bubbas-mobile-app` | mobile app |
| bubbas fireworks | `bubbas-ui` | shared interface components |
| bubbas fireworks | `bubbas-brand-studio` | brand catalog and assets |
| bubbas fireworks | `bubbas-arcade` | web arcade |
| fat man wholesale | `fatman-wholesale` | company website |
| warecasa | `WareCasa` | inventory and operations for a fireworks business |

archived: `bubbas-info-links`, `bubbas-social`, [`handh-mail`](https://github.com/handh-dev/handh-mail) (guidance consolidated into `handh-email`).

## brand

give any agent the full handh.dev brand in under 1k tokens:

```bash
curl -fsSL https://raw.githubusercontent.com/handh-dev/handh-dev/main/brand/AGENTS.md
```
