# Contributor Communication

> Communication strategy and framework for the Model Context Protocol community

This document explains how to communicate and collaborate within the Model Context Protocol (MCP) project.

## Communication Channels

In short:

* **[Discord][discord-join]**: For real-time or ad-hoc discussions.
* **[GitHub Discussions](https://github.com/modelcontextprotocol/modelcontextprotocol/discussions)**: For structured, longer-form discussions.
* **[GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues)**: For actionable tasks, bug reports, and feature requests.
* **For security-sensitive issues**: Follow the process in [SECURITY.md](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md).

All communication is governed by our [Code of Conduct](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/CODE_OF_CONDUCT.md). We expect all participants to maintain respectful, professional, and inclusive interactions across all channels.

### Discord

For real-time contributor discussion and collaboration. The server is designed around **MCP contributors** and is not intended
to be a place for general MCP support.

The Discord server will have both public and private channels.

[Join the Discord server here][discord-join].

#### Public Channels (Default)

* **Purpose**: Open community engagement, collaborative development, and transparent project coordination.
* Primary use cases:
  * **Public SDK and tooling development**: All development, from ideation to release planning, happens in public channels (e.g., `#typescript-sdk-dev`, `#inspector-dev`).
  * **[Working and Interest Group](/community/working-interest-groups) discussions**
  * **Community onboarding** and contribution guidance.
  * **Community feedback** and collaborative brainstorming.
  * Public **office hours** and **maintainer availability**.
* Avoid:
  * MCP user support: participants are expected to read official documentation and start new GitHub Discussions for questions or support.
  * Service or product marketing: interactions on this Discord are expected to be vendor-neutral and not used for brand-building or sales. Mentions of brands or products are discouraged outside of being used as examples or responses to conversations that start off focused on the specification.

#### Private channels (Exceptions)

* **Purpose**: Confidential coordination and sensitive matters that cannot be discussed publicly. Access will be restricted to designated maintainers.
* **Strict criteria for private use**:
  * **Security incidents** (CVEs, protocol vulnerabilities).
  * **People matters** (maintainer-related discussions, code of conduct policies).
  * Select channels will be configured to be **read-only**. This can be good for example for maintainer decision making.
  * Coordination requiring **immediate** or otherwise **focused response** with a limited audience.
* **Transparency**:
  * **All technical and governance decisions** affecting the community **must be documented** in GitHub Discussions and/or Issues, and will be labeled with `notes`.
  * **Some matters related to individual contributors** may remain private when appropriate (e.g., personal circumstances, disciplinary actions, or other sensitive individual matters).
  * Private channels are to be used as **temporary "incident rooms,"** not for routine development.

Any significant discussion on Discord that leads to a potential decision or proposal must be moved to a GitHub Discussion or GitHub Issue to create a persistent, searchable record. Proposals will then be promoted to full-fledged PRs with associated work items (GitHub Issues) as needed.

### GitHub Discussions

For structured, long-form discussion and debate on project direction, features, improvements, and community topics.

When to use:

* Project roadmap planning and milestone discussions
* Announcements and release communications
* Community polls and consensus-building processes
* Feature requests with context and rationale
  * If a particular repository does not have GitHub Discussions enabled, feel free to open a GitHub Issue instead.

### GitHub Issues

For bug reports, feature tracking, and actionable development tasks.

When to use:

* Submit SEP proposals (following the [SEP guidelines](./sep-guidelines))
* Bug reports with reproducible steps
* Documentation improvements with specific scope
* CI/CD problems and infrastructure issues
* Release tasks and milestone tracking

### Security Issues

**Do not post security issues publicly.** Instead:

1. Use the private security reporting process. For protocol-level security issues, follow the process in [SECURITY.md in the modelcontextprotocol GitHub repository](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/SECURITY.md).
2. Contact lead and/or [core maintainers](./governance#current-core-maintainers) directly.
3. Follow responsible disclosure guidelines.

## Decision Records

All MCP decisions are documented and captured in public channels.

* **Technical decisions**: [GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues) and SEPs.
* **Specification changes**: [On the Model Context Protocol website](https://modelcontextprotocol.io/specification/draft/changelog).
* **Process changes**: [Community documentation](https://modelcontextprotocol.io/community/governance).
* **Governance decisions and updates**: [GitHub Issues](https://github.com/modelcontextprotocol/modelcontextprotocol/issues) and SEPs.

When documenting decisions, we will retain as much context as possible:

* Decision makers
* Background context and motivation
* Options that were considered
* Rationale for the chosen approach
* Implementation steps

[discord-join]: https://discord.gg/6CSzBmMkjX

# Governance and Stewardship

> Learn about the Model Context Protocol's governance structure and how to participate in the community

The Model Context Protocol (MCP) follows a formal governance model to ensure transparent decision-making and community participation. This document outlines how the project is organized and how decisions are made.

## Technical Governance

The MCP project adopts a hierarchical structure, similar to Python, PyTorch and other open source projects:

* A community of **contributors** who file issues, make pull requests, and contribute to the project.
* A small set of **maintainers** drive components within the MCP project, such as SDKs, documentation, and others.
* Contributors and maintainers are overseen by **core maintainers**, who drive the overall project direction.
* The core maintainers have two **lead core maintainers** who are the catch-all decision makers.
* Maintainers, core maintainers, and lead core maintainers form the **MCP steering group**.

All maintainers are expected to have a strong bias towards MCP's design philosophy. Membership in the technical governance process is for individuals, not companies. That is, there are no seats reserved for specific companies, and membership is associated with the person rather than the company employing that person. This ensures that maintainers act in the best interests of the protocol itself and the open source community.

### Channels

Technical Governance is facilitated through a shared [Discord server](/community/communication#discord) of all **maintainers, core maintainers** and **lead maintainers**. Each maintainer group can choose additional communication channels, but all decisions and their supporting discussions must be recorded and made transparently available on the Discord server.

### Maintainers

Maintainers are responsible for [Working or Interest Groups](/community/working-interest-groups) within the MCP project. These generally are independent repositories such as language-specific SDKs, but can also extend to subdirectories of a repository, such as the MCP documentation. Maintainers may adopt their own rules and procedures for making decisions. Maintainers are expected to make decisions for their respective projects independently, but can defer or escalate to the core maintainers when needed.

Maintainers are responsible for the:

* Thoughtful and productive engagement with community contributors,
* Maintaining and improving their respective area of the MCP project,
* Supporting documentation, roadmaps and other adjacent parts of the MCP project,
* Present ideas from community to core.

Maintainers are encouraged to propose additional maintainers when needed. Maintainers can only be appointed and removed by core maintainers or lead core maintainers at any time and without reason.

Maintainers have write and/or admin access to their respective repositories.

### Core Maintainers

The core maintainers are expected to have a deep understanding of the Model Context Protocol and its specification. Their responsibilities include:

* Designing, reviewing and steering the evolution of the MCP specification, as well as all other parts of the MCP project, such as documentation,
* Articulating a cohesive long-term vision for the project,
* Mediating and resolving contentious issues with fairness and transparency, seeking consensus where possible while making decisive choices when necessary,
* Appoint or remove maintainers,
* Stewardship of the MCP project in the best interest of MCP.

The core maintainers as a group have the power to veto any decisions made by maintainers by majority vote. The core maintainers have power to resolve disputes as they see fit. The core maintainers should publicly articulate their decision-making. The core group is responsible for adopting their own procedures for making decisions.

Core maintainers generally have write and admin access to all MCP repositories, but should use the same contribution (usually pull-requests) mechanism as outside contributors. Exceptions can be made based on security considerations.

### Lead Maintainers (BDFL)

MCP has two lead maintainers: Justin Spahr-Summers and David Soria Parra. Lead Maintainers can veto any decision by core maintainers or maintainers. This model is also commonly known as Benevolent Dictator for Life (BDFL) in the open source community. The Lead Maintainers should publicly articulate their decision-making and give clear reasoning for their decisions. Lead maintainers are part of the core maintainer group.

The Lead Maintainers are responsible for confirming or removing core maintainers.

Lead Maintainers are administrators on all infrastructure for the MCP project where possible. This includes but is not restricted to all communication channels, GitHub organizations and repositories.

### Decision Process

The core maintainer group meets every two weeks to discuss and vote on proposals, as well as discuss any topics needed. The shared Discord server can be used to discuss and vote on smaller proposals if needed.

The lead maintainer, core maintainer, and maintainer group should attempt to meet in person every three to six months.

## Processes

Core and lead maintainers are responsible for all aspects of Model Context Protocol, including documentation, issues, suggestions for content, and all other parts under the [MCP project](https://github.com/modelcontextprotocol). Maintainers are responsible for documentation, issues, and suggestions of content for their area of the MCP project, but are encouraged to partake in general maintenance of the MCP projects. Maintainers, core maintainers, and lead maintainers should use the same contribution process as external contributors, rather than making direct changes to repos. This provides insight into intent and opportunity for discussion.

### Working and Interest Groups

MCP collaboration and contributions are organized around two structures: [Working Groups and Interest Groups](/community/working-interest-groups).

Interest Groups are responsible for identifying and articulating problems that MCP should address, primarily by facilitating open discussions within the community. In contrast, Working Groups focus on developing concrete solutions by collaboratively producing deliverables, such as SEPs or community-owned implementations of the specification. While input from Interest Groups can help justify the formation of a Working Group, it is not a strict requirement. Similarly, contributions from either Interest Groups or Working Groups are encouraged, but not mandatory, when submitting SEPs or other community proposals.

We strongly encourage all contributors interested in working on a specific SEP to first collaborate within an Interest Group. This collaborative process helps ensure that the proposed SEP aligns with protocol needs and is the right direction for its adopters.

#### Governance Principles

All groups are self-governed while adhering to these core principles:

1. Clear contribution and decision-making processes
2. Open communication and transparent decisions

Both must:

* Document their contribution process
* Maintain transparent communication
* Make decisions publicly (groups must publish meeting notes and proposals)

Projects and working groups without specified processes default to:

* GitHub pull requests and issues for contributions
* A public channel in the official [MCP Contributor Discord](/community/communication#discord)

#### Maintenance Responsibilities

Components without dedicated maintainers (such as documentation) fall under core maintainer responsibility. These follow standard contribution guidelines through pull requests, with maintainers handling reviews and escalating to core maintainer review for any significant changes.

Core maintainers and maintainers are encouraged to improve any part of the MCP project, regardless of formal maintenance assignments.

### Specification Project

#### Specification Enhancement Proposal (SEP)

Proposed changes to the specification must come in the form of a written version, starting with a summary of the proposal, outlining the **problem** it tries to solve, propose **solution**, **alternatives**, **considerations, outcomes** and **risks**. The [SEP Guidelines](/community/sep-guidelines) outline information on the expected structure of SEPs. SEP's should be created as issues in the [specification repository](https://github.com/modelcontextprotocol/specification) and tagged with the labels `proposal, sep`.

All proposals must have a **sponsor** from the MCP steering group (maintainer, core maintainer or lead core maintainer). The sponsor is responsible for ensuring that the proposal is actively developed, meets the quality standard for proposals and is responsible for presenting and discussing it in meetings of core maintainers. Maintainer and Core Maintainer groups should review open proposals without sponsors in regular intervals. Proposals that do not find a sponsor within six months are automatically rejected.

Once proposals have a sponsor, they are assigned to the sponsor and are tagged `draft`.

## Communication

### Core Maintainer Meetings

The core maintainer group meets on a bi-weekly basis to discuss proposals and the project. Notes on proposals should be made public. The core maintainer group will strive to meet in person every 3-6 months.

### Public Chat

The MCP project maintains a [public Discord server](/community/communication#discord) with open chats for interest groups. The MCP project may have private channels for certain communications.

## Nominating, Confirming and Removing Maintainers

### The Principles

* Membership in module maintainer groups is given to **individuals** on merit basis after they demonstrated strong expertise of their area of work through contributions, reviews, and discussions and are aligned with the overall MCP direction.
* For membership in the **maintainer** group the individual has to demonstrate strong and continued alignment with the overall MCP principles.
* No term limits for module maintainers or core maintainers
* Light criteria of moving working-group or sub-project maintenance to 'emeritus' status if they don't actively participate over long periods of time. Each maintainer group may define the inactive period that's appropriate for their area.
* The membership is for an individual, not a company.

### Nomination and Removal

* Core Maintainers are responsible for adding and removing maintainers. They will take the consideration of existing maintainers into account.
* The lead maintainers are responsible for adding and removing core maintainers.

#### Nomination Process

If a Maintainer (or Core / Lead Maintainer) wishes to propose a nomination for the Core / Lead Maintainers’ consideration, they should follow the following process:

1. Collect evidence for the nomination. This will generally come in the form of a history of merged PRs on the repositories for which maintainership is being considered.
2. Discuss among maintainers of the relevant group(s) as to whether they would be supportive of approving the nomination.
3. DM a Community Moderator or Core Maintainer to create a private channel in Discord, in the format `nomination-{name}-{group}`. Add all core maintainers, lead maintainers, and co-maintainers on the relevant group.
4. Provide context for the individual under nomination. See below for suggestions on what to include here.
5. Create a Discord Poll and ask Core / Lead Maintainers to vote Yes / No on the nomination. Reaching consensus is encouraged though not required.
6. After Core / Lead Maintainers discuss and/or vote, if the nomination is favorable, relevant members with permissions to update GitHub an Discord roles will add the nominee to the appropriate groups. The nominator should announce the new maintainership in the relevant Discord channel.
7. The temporary Discord channel will be deleted a week later.

Suggestions for the kind of information to share with core maintainers when nominating someone:

* GitHub profile link, LinkedIn profile link, Discord username
* For what group(s) are you nominating the individual for maintainership
* Whether the group(s) agree that this person should be elevated to maintainership
* Description of their contributions to date (including links to most substantial contributions)
* Description of expected contributions moving forward (e.g. Are they eager to be a maintainer? Will they have capacity to do so?)
* Other context about the individual (e.g. current employer, motivations behind MCP involvement)
* Anything else you think may be relevant to consider for the nomination

## Current Core Maintainers

* Inna Harper
* Basil Hosmer
* Paul Carleton
* Nick Cooper
* Nick Aldridge
* Che Liu
* Den Delimarsky

## Current Maintainers and Working Groups

Refer to [the maintainer list](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md).

# SEP Guidelines

> Specification Enhancement Proposal (SEP) guidelines for proposing changes to the Model Context Protocol

## What is a SEP?

SEP stands for Specification Enhancement Proposal. A SEP is a design document providing information to the MCP community, or describing a new feature for the Model Context Protocol or its processes or environment. The SEP should provide a concise technical specification of the feature and a rationale for the feature.

We intend SEPs to be the primary mechanisms for proposing major new features, for collecting community input on an issue, and for documenting the design decisions that have gone into MCP. The SEP author is responsible for building consensus within the community and documenting dissenting opinions.

Because the SEPs are maintained as text files in a versioned repository (GitHub Issues), their revision history is the historical record of the feature proposal.

## What qualifies a SEP?

The goal is to reserve the SEP process for changes that are substantial enough to require broad community discussion, a formal design document, and a historical record of the decision-making process. A regular GitHub issue or pull request is often more appropriate for smaller, more direct changes.

Consider proposing a SEP if your change involves any of the following:

* **A New Feature or Protocol Change**: Any change that adds, modifies, or removes features in the Model Context Protocol. This includes:
  * Adding new API endpoints or methods.
  * Changing the syntax or semantics of existing data structures or messages.
  * Introducing a new standard for interoperability between different MCP-compatible tools.
  * Significant changes to how the specification itself is defined, presented, or validated.
* **A Breaking Change**: Any change that is not backwards-compatible.
* **A Change to Governance or Process**: Any proposal that alters the project's decision-making, contribution guidelines (like this document itself).
* **A Complex or Controversial Topic**: If a change is likely to have multiple valid solutions or generate significant debate, the SEP process provides the necessary framework to explore alternatives, document the rationale, and build community consensus before implementation begins.

## SEP Types

There are three kinds of SEP:

1. **Standards Track** SEP describes a new feature or implementation for the Model Context Protocol. It may also describe an interoperability standard that will be supported outside the core protocol specification.
2. **Informational** SEP describes a Model Context Protocol design issue, or provides general guidelines or information to the MCP community, but does not propose a new feature. Informational SEPs do not necessarily represent an MCP community consensus or recommendation.
3. **Process** SEP describes a process surrounding MCP, or proposes a change to (or an event in) a process. Process SEPs are like Standards Track SEPs but apply to areas other than the MCP protocol itself.

## Submitting a SEP

The SEP process begins with a new idea for the Model Context Protocol. It is highly recommended that a single SEP contain a single key proposal or new idea. Small enhancements or patches often don't need a SEP and can be injected into the MCP development workflow with a pull request to the MCP repo. The more focused the SEP, the more successful it tends to be.

Each SEP must have an **SEP author** -- someone who writes the SEP using the style and format described below, shepherds the discussions in the appropriate forums, and attempts to build community consensus around the idea. The SEP author should first attempt to ascertain whether the idea is SEP-able. Posting to the MCP community forums (Discord, GitHub Discussions) is the best way to go about this.

### SEP Workflow

SEPs should be submitted as a GitHub Issue in the [specification repository](https://github.com/modelcontextprotocol/modelcontextprotocol). The standard SEP workflow is:

1. You, the SEP author, create a [well-formatted](#sep-format) GitHub Issue with the `SEP` and `proposal` tags. The SEP number is the same as the GitHub Issue number, the two can be used interchangably.
2. Find a Core Maintainer or Maintainer to sponsor your proposal. Core Maintainers and Maintainers will regularly go over the list of open proposals to determine which proposals to sponsor. You can tag relevant maintainers from [the maintainer list](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) in your proposal.
3. Once a sponsor is found, the GitHub Issue is assigned to the sponsor. The sponsor will add the `draft` tag, ensure the SEP number is in the title, and assign a milestone.
4. The sponsor will informally review the proposal and may request changes based on community feedback. When ready for formal review, the sponsor will add the `in-review` tag.
5. After the `in-review` tag is added, the SEP enters formal review by the Core Maintainers team. The SEP may be accepted, rejected, or returned for revision.
6. If the SEP has not found a sponsor within three months, Core Maintainers may close the SEP as `dormant`.

### SEP Format

Each SEP should have the following parts:

1. **Preamble** -- A short descriptive title, the names and contact info for each author, the current status.
2. **Abstract** -- A short (\~200 word) description of the technical issue being addressed.
3. **Motivation** -- The motivation should clearly explain why the existing protocol specification is inadequate to address the problem that the SEP solves. The motivation is critical for SEPs that want to change the Model Context Protocol. SEP submissions without sufficient motivation may be rejected outright.
4. **Specification** -- The technical specification should describe the syntax and semantics of any new protocol feature. The specification should be detailed enough to allow competing, interoperable implementations. A PR with the changes to the specification should be provided.
5. **Rationale** -- The rationale explains why particular design decisions were made. It should describe alternate designs that were considered and related work. The rationale should provide evidence of consensus within the community and discuss important objections or concerns raised during discussion.
6. **Backward Compatibility** -- All SEPs that introduce backward incompatibilities must include a section describing these incompatibilities and their severity. The SEP must explain how the author proposes to deal with these incompatibilities.
7. **Reference Implementation** -- The reference implementation must be completed before any SEP is given status "Final", but it need not be completed before the SEP is accepted. While there is merit to the approach of reaching consensus on the specification and rationale before writing code, the principle of "rough consensus and running code" is still useful when it comes to resolving many discussions of protocol details.
8. **Security Implications** -- If there are security concerns in relation to the SEP, those concerns should be explicitly written out to make sure reviewers of the SEP are aware of them.

### SEP States

SEPs can be one one of the following states

* `proposal`: SEP proposal without a sponsor.
* `draft`: SEP proposal with a sponsor.
* `in-review`: SEP proposal ready for review.
* `accepted`: SEP accepted by Core Maintainers, but still requires final wording and reference implementation.
* `rejected`: SEP rejected by Core Maintainers.
* `withdrawn`: SEP withdrawn.
* `final`: SEP finalized.
* `superseded`: SEP has been replaced by a newer SEP.
* `dormant`: SEP that has not found sponsors and was subsequently closed.

### SEP Review & Resolution

SEPs are reviewed by the MCP Core Maintainers team on a bi-weekly basis.

For a SEP to be accepted it must meet certain minimum criteria:

* A prototype implementation demonstrating the proposal
* Clear benefit to the MCP ecosystem
* Community support and consensus

Once a SEP has been accepted, the reference implementation must be completed. When the reference implementation is complete and incorporated into the main source code repository, the status will be changed to "Final".

A SEP can also be "Rejected" or "Withdrawn". A SEP that is "Withdrawn" may be re-submitted at a later date.

## Reporting SEP Bugs, or Submitting SEP Updates

How you report a bug, or submit a SEP update depends on several factors, such as the maturity of the SEP, the preferences of the SEP author, and the nature of your comments. For SEPs not yet reaching `final` state, it's probably best to send your comments and changes directly to the SEP author. Once SEP is finalized, you may want to submit corrections as a GitHub comment on the issue or pull request to the reference implementation.

## Transferring SEP Ownership

It occasionally becomes necessary to transfer ownership of SEPs to a new SEP author. In general, we'd like to retain the original author as a co-author of the transferred SEP, but that's really up to the original author. A good reason to transfer ownership is because the original author no longer has the time or interest in updating it or following through with the SEP process, or has fallen off the face of the 'net (i.e. is unreachable or not responding to email). A bad reason to transfer ownership is because you don't agree with the direction of the SEP. We try to build consensus around a SEP, but if that's not possible, you can always submit a competing SEP.

## Copyright

This document is placed in the public domain or under the CC0-1.0-Universal license, whichever is more permissive.

# Working and Interest Groups

> Learn about the two forms of collaborative groups within the Model Context Protocol's governance structure - Working Groups and Interest Groups.

Within the MCP contributor community we maintain two types of collaboration formats - **Interest** and **Working** groups.

**Interest Groups** are responsible for identifying and articulating problems that MCP should address, primarily by facilitating open discussions within the community. In contrast, **Working Groups** focus on developing concrete solutions by collaboratively producing deliverables, such as SEPs or community-owned implementations of the specification.

While input from Interest Groups can help justify the formation of a Working Group, it is not a strict requirement. Similarly, contributions from either Interest Groups or Working Groups are encouraged, but not mandatory, when submitting SEPs or other community proposals.

We strongly encourage all contributors interested in working on a specific SEP to first collaborate within an Interest Group. This collaborative process helps ensure that the proposed SEP aligns with community needs and is the right direction for the protocol.

Long-term projects in the MCP ecosystem, such as SDKs, Inspector, or Registry are maintained by dedicated Working Groups.

## Purpose

These groups exist to:

* **Facilitate high-signal spaces for focused discussions** - contributors who opt into notifications, expertise sharing, and regular meetings can engage with topics that are highly relevant to them, enabling meaningful contributions and opportunities to learn from others.
* **Establish clear expectations and leadership roles** - guide collaborative efforts and ensure steady progress toward concrete deliverables that advance MCP evolution and adoption.

## Mechanisms

### Interest Groups (IGs)

**Goal:** Facilitate discussion and knowledge-sharing among MCP contributors who share interests in a specific MCP sub-topic or context. The primary focus is on identifying and gathering problems that may be worth addressing through SEPs or other community artifacts, while encouraging open exploration of protocol issues and opportunities.

**Expectations**:

* Regular conversations in the Interest Group Discord channel
* **AND/OR** a recurring live meeting regularly attended by Interest Group members

**Examples**:

* Security in MCP
* Auth in MCP
* Using MCP in enterprise settings
* Tooling and practices surrounding hosting MCP servers
* Tooling and practices surrounding implementing MCP clients

**Lifecycle**:

* Creation begins by filling out a template in the #wg-ig-group-creation [Discord](/community/communication#discord) channel
* A community moderator will review and call for a vote in the (private) #community-moderators Discord channel. Majority positive vote by members over a 72h period approves creation of the group.
  * The creation of the group can be reversed at any time (e.g., after new information surfaces). Core and lead maintainers can veto.
* Facilitator(s) and Maintainer(s) responsible for organizing IG into meeting expectations
  * Facilitator is an informal role responsible for shepherding or speaking for a group
  * Maintainer is an official representative from the MCP steering group. A maintainer is not required for every group, but can help advocate for specific changes or initiatives.
* IG is retired only when community moderators or Core or Lead Maintainers determine it's no longer active and/or needed
  * Successful IGs do not have a time limit or expiration date - as long as they are active and maintained, they will remain available

**Creation Template**:

* Facilitator(s)
* Maintainer(s) (optional)
* IGs with potentially similar goals/discussions
* How this IG differentiates itself from the related IGs
* First topic you to discuss within the IG

Participation in an Interest Group (IG) is not required to start a Working Group (WG) or to create a SEP. However, building consensus within IGs can be valuable when justifying the formation of a WG. Likewise, referencing support from IGs or WGs can strengthen a SEP and its chances of success.

### Working Groups (WG)

**Goal:** Facilitate collaboration within the MCP community on a SEP, a themed series of SEPs, or an otherwise officially endorsed project.

**Expectations**:

* Meaningful progress towards at least one SEP or spec-related implementation **OR** hold maintenance responsibilities for a project (e.g., Inspector, Registry, SDKs)
* Facilitators are responsible for keeping track of progress and communicating status when appropriate

**Examples**:

* Registry
* Inspector
* Tool Filtering
* Server Identity

**Lifecycle**:

* Creation begins by filling out a template in #wg-ig-group-creation Discord channel
* A community moderator will review and call for a vote in the (private) #community-moderators Discord channel. Majority positive vote by members over a 72h period approves creation of the group.
  * The creation of the group can be reversed at any time (e.g., after new information surfaces). Core and lead maintainers can veto.
* Facilitator(s) and Maintainer(s) responsible for organizing WG into meeting expectations
  * Facilitator is an informal role responsible for shepherding or speaking for a group
  * Maintainer is an official representative from the MCP steering group. A maintainer is not required for every group, but can help advocate for specific changes or initiatives
* WG is retired when either:
  * Community moderators or Core and Lead Maintainers decide it is no longer active and/or needed
  * The WG no longer has an active Issue/PR for a month or more, or has completed all Issues/PRs it intended to pursue.

**Creation Template**:

* Facilitator(s)
* Maintainer(s) (optional)
* Explanation of interest/use cases, ideally originating from an IG discussion; however that is not a requirement
* First Issue/PR/SEP that the WG will work on

## WG/IG Facilitators

A **Facilitator** role in a WG or IG does *not* result in a [maintainership role](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/main/MAINTAINERS.md) across the MCP organization. It is an informal role into which anyone can self-nominate.

A Facilitator is responsible for helping shepherd discussions and collaboration within an Interest or Working Group.

Lead and Core Maintainers reserve the right to modify the list of Facilitators and Maintainers for any WG/IG at any time.

## FAQ

### How do I get involved contributing to MCP?

These IG and WG abstractions help provide an elegant on-ramp:

1. [Join the Discord](/community/communication#discord) and follow conversations in IGs relevant to you. Attend live calls. Participate.
2. Offer to facilitate calls. Contribute your use cases in SEP proposals and other work.
3. When you're comfortable contributing to deliverables, jump in to contribute to WG work.
4. Active and valuable contributors will be nominated by WG maintainers as new maintainers.

### Where can I find a list of all current WGs and IGs?

On the [MCP Contributor Discord](/community/communication#discord) there is a section of channels for each Working and Interest Group.


# Roadmap

> Our plans for evolving Model Context Protocol

<Info>Last updated: **2025-07-22**</Info>

The Model Context Protocol is rapidly evolving. This page outlines our current thinking on key priorities and direction for approximately **the next six months**, though these may change significantly as the project develops. To see what's changed recently, check out the **[specification changelog](/specification/2025-06-18/changelog/)**.

<Note>
  The ideas presented here are not commitments—we may solve these challenges differently than described, or some may not materialize at all. This is also not an *exhaustive* list; we may incorporate work that isn't mentioned here.
</Note>

We value community participation! Each section links to relevant discussions where you can learn more and contribute your thoughts.

For a technical view of our standardization process, visit the [Standards Track](https://github.com/orgs/modelcontextprotocol/projects/2/views/2) on GitHub, which tracks how proposals progress toward inclusion in the official [MCP specification](https://spec.modelcontextprotocol.io).

## Agents

As MCP increasingly becomes part of agentic workflows, we're focusing on key improvements:

* **Asynchronous Operations**: supporting long-running operations that may take extended periods, with resilient handling of disconnections and reconnections

## Authentication and Security

We're evolving our authorization and security resources to improve user safety and provide a better developer experience:

* **Guides and Best Practices**: documenting specifics about deploying MCP securely in the form of guides and best practices to help developers avoid common pitfalls.
* **Alternatives to Dynamic Client Registration (DCR)**: exploring alternatives to DCR, attempting to address operational challenges while preserving a smooth user experience.
* **Fine-grained Authorization**: developing mechanisms and guidelines for primitive authorization for sensitive actions
* **Enterprise Managed Authorization**: adding the capability for enterprises to simplify MCP server authorization with the help of Single Sign-On (SSO)
* **Secure Authorization Elicitation**: enable developers to integrate secure authorization flows for downstream APIs outside the main MCP server authorization

## Validation

To foster a robust developer ecosystem, we plan to invest in:

* **Reference Client Implementations**: demonstrating protocol features with high-quality AI applications
* **Reference Server Implementation**: showcasing authentication patterns and remote deployment best practices
* **Compliance Test Suites**: automated verification that clients, servers, and SDKs properly implement the specification

These tools will help developers confidently implement MCP while ensuring consistent behavior across the ecosystem.

## Registry

For MCP to reach its full potential, we need streamlined ways to distribute and discover MCP servers.

We plan to develop an [**MCP Registry**](https://github.com/orgs/modelcontextprotocol/discussions/159) that will enable centralized server discovery and metadata. This registry will primarily function as an API layer that third-party marketplaces and discovery services can build upon.

## Multimodality

Supporting the full spectrum of AI capabilities in MCP, including:

* **Additional Modalities**: video and other media types
* **[Streaming](https://github.com/modelcontextprotocol/specification/issues/117)**: multipart, chunked messages, and bidirectional communication for interactive experiences

## Get Involved

We welcome your contributions to MCP's future! Join our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to share ideas, provide feedback, or participate in the development process.

# Example Clients

> A list of applications that support MCP integrations

This page provides an overview of applications that support the Model Context Protocol (MCP). Each client may support different MCP features, allowing for varying levels of integration with MCP servers.

## Feature support matrix

<div id="feature-support-matrix-wrapper">
  {/* prettier-ignore-start */}

  | Client                                                     | [Resources] | [Prompts] | [Tools] | [Discovery] | [Sampling] | [Roots] | [Elicitation] |
  | ---------------------------------------------------------- | ----------- | --------- | ------- | ----------- | ---------- | ------- | ------------- |
  | [5ire][5ire]                                               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [AgentAI][AgentAI]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [AgenticFlow][AgenticFlow]                                 | ✅           | ✅         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [AIQL TUUI][AIQL TUUI]                                     | ✅           | ✅         | ✅       | ✅           | ✅          | ❌       | ❓             |
  | [Amazon Q CLI][Amazon Q CLI]                               | ❌           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Amazon Q IDE][Amazon Q IDE]                               | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Amp][Amp]                                                 | ✅           | ❌         | ✅       | ❌           | ✅          | ❌       | ❓             |
  | [Apify MCP Tester][Apify MCP Tester]                       | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [Augment Code][AugmentCode]                                | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [BeeAI Framework][BeeAI Framework]                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [BoltAI][BoltAI]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Call Chirp][Call Chirp]                                   | ❌           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Chatbox][Chatbox]                                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             |
  | [ChatGPT][ChatGPT]                                         | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [ChatWise][ChatWise]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Claude.ai][Claude.ai]                                     | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Claude Code][Claude Code]                                 | ✅           | ✅         | ✅       | ❌           | ❌          | ✅       | ❓             |
  | [Claude Desktop App][Claude Desktop]                       | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Chorus][Chorus]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Cline][Cline]                                             | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [CodeGPT][CodeGPT]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Continue][Continue]                                       | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Copilot-MCP][CopilotMCP]                                  | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Cursor][Cursor]                                           | ✅           | ✅         | ✅       | ❌           | ✅          | ✅       | ✅             |
  | [Daydreams Agents][Daydreams]                              | ✅           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Emacs Mcp][Mcp.el]                                        | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [fast-agent][fast-agent]                                   | ✅           | ✅         | ✅       | ✅           | ✅          | ✅       | ✅             |
  | [FlowDown][FlowDown]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❌             |
  | [FLUJO][FLUJO]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Genkit][Genkit]                                           | ⚠️          | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Glama][Glama]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Gemini CLI][Gemini CLI]                                   | ❌           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [GenAIScript][GenAIScript]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [GitHub Copilot coding agent][GitHubCopilotCodingAgent]    | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❌             |
  | [Goose][Goose]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [gptme][gptme]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [HyperAgent][HyperAgent]                                   | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Jenova][Jenova]                                           | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [JetBrains AI Assistant][JetBrains AI Assistant]           | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Kilo Code][Kilo Code]                                     | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [Klavis AI Slack/Discord/Web][Klavis AI]                   | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Langflow][Langflow]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [LibreChat][LibreChat]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [LM Studio][LM Studio]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Lutra][Lutra]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [mcp-agent][mcp-agent]                                     | ✅           | ✅         | ✅       | ❓           | ⚠️         | ✅       | ✅             |
  | [mcp-client-chatbot][mcp-client-chatbot]                   | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [mcp-use][mcp-use]                                         | ✅           | ✅         | ✅       | ✅           | ✅          | ❌       | ✅             |
  | [modelcontextchat.com][modelcontextchat.com]               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [MCPHub][MCPHub]                                           | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [MCPOmni-Connect][MCPOmni-Connect]                         | ✅           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             |
  | [Memex][Memex]                                             | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Microsoft Copilot Studio]                                 | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [MindPal][MindPal]                                         | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Mistral AI: Le Chat][Mistral AI: Le Chat]                 | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [MooPoint][MooPoint]                                       | ❌           | ❌         | ✅       | ❓           | ✅          | ❌       | ❓             |
  | [Msty Studio][Msty Studio]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [NVIDIA Agent Intelligence toolkit][AIQ toolkit]           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [OpenSumi][OpenSumi]                                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [oterm][oterm]                                             | ❌           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             |
  | [Postman][postman]                                         | ✅           | ✅         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [RecurseChat][RecurseChat]                                 | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Roo Code][Roo Code]                                       | ✅           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Shortwave][Shortwave]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Simtheory][Simtheory]                                     | ✅           | ✅         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [Slack MCP Client][Slack MCP Client]                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Sourcegraph Cody][Cody]                                   | ✅           | ❌         | ❌       | ❓           | ❌          | ❌       | ❓             |
  | [SpinAI][SpinAI]                                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Superinterface][Superinterface]                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Superjoin][Superjoin]                                     | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [systemprompt][systemprompt]                               | ✅           | ✅         | ✅       | ❓           | ✅          | ❌       | ❓             |
  | [Tambo][Tambo]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Tencent CloudBase AI DevKit][Tencent CloudBase AI DevKit] | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [TheiaAI/TheiaIDE][TheiaAI/TheiaIDE]                       | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Tome][Tome]                                               | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [TypingMind App][TypingMind App]                           | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [VS Code GitHub Copilot][VS Code]                          | ✅           | ✅         | ✅       | ✅           | ✅          | ✅       | ✅             |
  | [Warp][Warp]                                               | ✅           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [WhatsMCP][WhatsMCP]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Windsurf Editor][Windsurf]                                | ❌           | ❌         | ✅       | ✅           | ❌          | ❌       | ❓             |
  | [Witsy][Witsy]                                             | ❌           | ❌         | ✅       | ❓           | ❌          | ❌       | ❓             |
  | [Zed][Zed]                                                 | ❌           | ✅         | ✅       | ❌           | ❌          | ❌       | ❓             |
  | [Zencoder][Zencoder]                                       | ❌           | ❌         | ✅       | ❌           | ❌          | ❌       | ❓             |

  {/* prettier-ignore-end */}

  [Resources]: /docs/concepts/resources

  [Prompts]: /docs/concepts/prompts

  [Tools]: /docs/concepts/tools

  [Discovery]: /docs/concepts/tools#tool-discovery-and-updates

  [Sampling]: /docs/concepts/sampling

  [Roots]: /docs/concepts/roots

  [Elicitation]: /docs/concepts/elicitation

  [5ire]: https://github.com/nanbingxyz/5ire

  [AgentAI]: https://github.com/AdamStrojek/rust-agentai

  [AgenticFlow]: https://agenticflow.ai/mcp

  [AIQ toolkit]: https://github.com/NVIDIA/AIQToolkit

  [AIQL TUUI]: https://github.com/AI-QL/tuui

  [Amazon Q CLI]: https://github.com/aws/amazon-q-developer-cli

  [Amazon Q IDE]: https://aws.amazon.com/q/developer

  [Amp]: https://ampcode.com

  [Apify MCP Tester]: https://apify.com/jiri.spilka/tester-mcp-client

  [AugmentCode]: https://augmentcode.com

  [BeeAI Framework]: https://i-am-bee.github.io/beeai-framework

  [BoltAI]: https://boltai.com

  [Call Chirp]: https://www.call-chirp.com

  [Chatbox]: https://chatboxai.app

  [ChatGPT]: https://chatgpt.com

  [ChatWise]: https://chatwise.app

  [Claude.ai]: https://claude.ai

  [Claude Code]: https://claude.com/product/claude-code

  [Claude Desktop]: https://claude.ai/download

  [Chorus]: https://chorus.sh

  [Cline]: https://github.com/cline/cline

  [CodeGPT]: https://codegpt.co

  [Continue]: https://github.com/continuedev/continue

  [CopilotMCP]: https://github.com/VikashLoomba/copilot-mcp

  [Cursor]: https://cursor.com

  [Daydreams]: https://github.com/daydreamsai/daydreams

  [Klavis AI]: https://www.klavis.ai/

  [Mcp.el]: https://github.com/lizqwerscott/mcp.el

  [fast-agent]: https://github.com/evalstate/fast-agent

  [FlowDown]: https://github.com/Lakr233/FlowDown

  [FLUJO]: https://github.com/mario-andreschak/flujo

  [Glama]: https://glama.ai/chat

  [Gemini CLI]: https://goo.gle/gemini-cli

  [Genkit]: https://github.com/firebase/genkit

  [GenAIScript]: https://microsoft.github.io/genaiscript/reference/scripts/mcp-tools/

  [GitHubCopilotCodingAgent]: https://docs.github.com/en/enterprise-cloud@latest/copilot/concepts/about-copilot-coding-agent

  [Goose]: https://block.github.io/goose/docs/goose-architecture/#interoperability-with-extensions

  [Jenova]: https://www.jenova.ai

  [JetBrains AI Assistant]: https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant

  [Kilo Code]: https://github.com/Kilo-Org/kilocode

  [Langflow]: https://github.com/langflow-ai/langflow

  [LibreChat]: https://github.com/danny-avila/LibreChat

  [LM Studio]: https://lmstudio.ai

  [Lutra]: https://lutra.ai

  [mcp-agent]: https://github.com/lastmile-ai/mcp-agent

  [mcp-client-chatbot]: https://github.com/cgoinglove/mcp-client-chatbot

  [mcp-use]: https://github.com/pietrozullo/mcp-use

  [modelcontextchat.com]: https://modelcontextchat.com

  [MCPHub]: https://github.com/ravitemer/mcphub.nvim

  [MCPOmni-Connect]: https://github.com/Abiorh001/mcp_omni_connect

  [Memex]: https://memex.tech/

  [Microsoft Copilot Studio]: https://learn.microsoft.com/en-us/microsoft-copilot-studio/agent-extend-action-mcp

  [MindPal]: https://mindpal.io

  [Mistral AI: Le Chat]: https://chat.mistral.ai

  [MooPoint]: https://moopoint.io

  [Msty Studio]: https://msty.ai

  [OpenSumi]: https://github.com/opensumi/core

  [oterm]: https://github.com/ggozad/oterm

  [Postman]: https://postman.com/downloads

  [RecurseChat]: https://recurse.chat/

  [Roo Code]: https://roocode.com

  [Shortwave]: https://www.shortwave.com

  [Simtheory]: https://simtheory.ai

  [Slack MCP Client]: https://github.com/tuannvm/slack-mcp-client

  [Cody]: https://sourcegraph.com/cody

  [SpinAI]: https://spinai.dev

  [Superinterface]: https://superinterface.ai

  [Superjoin]: https://superjoin.ai

  [systemprompt]: https://systemprompt.io

  [Tambo]: https://tambo.co

  [Tencent CloudBase AI DevKit]: https://docs.cloudbase.net/ai/agent/mcp

  [TheiaAI/TheiaIDE]: https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/

  [Tome]: https://github.com/runebookai/tome

  [TypingMind App]: https://www.typingmind.com

  [VS Code]: https://code.visualstudio.com/

  [Windsurf]: https://codeium.com/windsurf

  [gptme]: https://github.com/gptme/gptme

  [Warp]: https://www.warp.dev/

  [WhatsMCP]: https://wassist.app/mcp/

  [Witsy]: https://github.com/nbonamy/witsy

  [Zed]: https://zed.dev

  [Zencoder]: https://zencoder.ai

  [HyperAgent]: https://github.com/hyperbrowserai/HyperAgent
</div>

## Client details

### 5ire

[5ire](https://github.com/nanbingxyz/5ire) is an open source cross-platform desktop AI assistant that supports tools through MCP servers.

**Key features:**

* Built-in MCP servers can be quickly enabled and disabled.
* Users can add more servers by modifying the configuration file.
* It is open-source and user-friendly, suitable for beginners.
* Future support for MCP will be continuously improved.

### AgentAI

[AgentAI](https://github.com/AdamStrojek/rust-agentai) is a Rust library designed to simplify the creation of AI agents. The library includes seamless integration with MCP Servers.

[Example of MCP Server integration](https://github.com/AdamStrojek/rust-agentai/blob/master/examples/tools_mcp.rs)

**Key features:**

* Multi-LLM – We support most LLM APIs (OpenAI, Anthropic, Gemini, Ollama, and all OpenAI API Compatible).
* Built-in support for MCP Servers.
* Create agentic flows in a type- and memory-safe language like Rust.

### AgenticFlow

[AgenticFlow](https://agenticflow.ai/) is a no-code AI platform that helps you build agents that handle sales, marketing, and creative tasks around the clock. Connect 2,500+ APIs and 10,000+ tools securely via MCP.

**Key features:**

* No-code AI agent creation and workflow building.
* Access a vast library of 10,000+ tools and 2,500+ APIs through MCP.
* Simple 3-step process to connect MCP servers.
* Securely manage connections and revoke access anytime.

**Learn more:**

* [AgenticFlow MCP Integration](https://agenticflow.ai/mcp)

### AIQL TUUI

[AIQL TUUI] is a native, cross-platform desktop AI chat application with MCP support. It supports multiple AI providers (e.g., Anthropic, Cloudflare, Deepseek, OpenAI, Qwen), local AI models (via vLLM, Ray, etc.), and aggregated API platforms (such as Deepinfra, Openrouter, and more).

**Key features:**

* **Dynamic LLM API & Agent Switching**: Seamlessly toggle between different LLM APIs and agents on the fly.
* **Comprehensive Capabilities Support**: Built-in support for tools, prompts, resources, and sampling methods.
* **Configurable Agents**: Enhanced flexibility with selectable and customizable tools via agent settings.
* **Advanced Sampling Control**: Modify sampling parameters and leverage multi-round sampling for optimal results.
* **Cross-Platform Compatibility**: Fully compatible with macOS, Windows, and Linux.
* **Free & Open-Source (FOSS)**: Permissive licensing allows modifications and custom app bundling.

**Learn more:**

* [TUUI document](https://www.tuui.com/)
* [AIQL GitHub repository](https://github.com/AI-QL)

### Amazon Q CLI

[Amazon Q CLI](https://github.com/aws/amazon-q-developer-cli) is an open-source, agentic coding assistant for terminals.

**Key features:**

* Full support for MCP servers.
* Edit prompts using your preferred text editor.
* Access saved prompts instantly with `@`.
* Control and organize AWS resources directly from your terminal.
* Tools, profiles, context management, auto-compact, and so much more!

**Get Started**

```bash
brew install amazon-q
```

### Amazon Q IDE

[Amazon Q IDE](https://aws.amazon.com/q/developer) is an open-source, agentic coding assistant for IDEs.

**Key features:**

* Support for the VSCode, JetBrains, Visual Studio, and Eclipse IDEs.
* Control and organize AWS resources directly from your IDE.
* Manage permissions for each MCP tool via the IDE user interface.

### Apify MCP Tester

[Apify MCP Tester](https://github.com/apify/tester-mcp-client) is an open-source client that connects to any MCP server using Server-Sent Events (SSE).
It is a standalone Apify Actor designed for testing MCP servers over SSE, with support for Authorization headers.
It uses plain JavaScript (old-school style) and is hosted on Apify, allowing you to run it without any setup.

**Key features:**

* Connects to any MCP server via SSE.
* Works with the [Apify MCP Server](https://apify.com/apify/actors-mcp-server) to interact with one or more Apify [Actors](https://apify.com/store).
* Dynamically utilizes tools based on context and user queries (if supported by the server).

### Amp

[Amp](https://ampcode.com) is an agentic coding tool built by Sourcegraph. It runs in VS Code (and compatible forks like Cursor, Windsurf, and VSCodium) and as a command-line tool. It’s also multiplayer — you can share threads and collaborate with your team.

**Key features:**

* Granular control over enabled tools and permissions
* Support for MCP servers defined in VS Code `mcp.json`

### Augment Code

[Augment Code](https://augmentcode.com) is an AI-powered coding platform for VS Code and JetBrains with autonomous agents, chat, and completions. Both local and remote agents are backed by full codebase awareness and native support for MCP, enabling enhanced context through external sources and tools.

**Key features:**

* Full MCP support in local and remote agents.
* Add additional context through MCP servers.
* Automate your development workflows with MCP tools.
* Works in VS Code and JetBrains IDEs.

### BeeAI Framework

[BeeAI Framework](https://i-am-bee.github.io/beeai-framework) is an open-source framework for building, deploying, and serving powerful agentic workflows at scale. The framework includes the **MCP Tool**, a native feature that simplifies the integration of MCP servers into agentic workflows.

**Key features:**

* Seamlessly incorporate MCP tools into agentic workflows.
* Quickly instantiate framework-native tools from connected MCP client(s).
* Planned future support for agentic MCP capabilities.

**Learn more:**

* [Example of using MCP tools in agentic workflow](https://i-am-bee.github.io/beeai-framework/#/typescript/tools?id=using-the-mcptool-class)

### BoltAI

[BoltAI](https://boltai.com) is a native, all-in-one AI chat client with MCP support. BoltAI supports multiple AI providers (OpenAI, Anthropic, Google AI...), including local AI models (via Ollama, LM Studio or LMX)

**Key features:**

* MCP Tool integrations: once configured, user can enable individual MCP server in each chat
* MCP quick setup: import configuration from Claude Desktop app or Cursor editor
* Invoke MCP tools inside any app with AI Command feature
* Integrate with remote MCP servers in the mobile app

**Learn more:**

* [BoltAI docs](https://boltai.com/docs/plugins/mcp-servers)
* [BoltAI website](https://boltai.com)

### Call Chirp

[Call Chirp] [https://www.call-chirp.com](https://www.call-chirp.com) uses AI to capture every critical detail from your business conversations, automatically syncing insights to your CRM and project tools so you never miss another deal-closing moment.

**Key features:**

* Save transcriptions from Zoom, Google Meet, and more
* MCP Tools for voice AI agents
* Remote MCP servers support

### Chatbox

Chatbox is a better UI and desktop app for ChatGPT, Claude, and other LLMs, available on Windows, Mac, Linux, and the web. It's open-source and has garnered 37K stars⭐ on GitHub.

**Key features:**

* Tools support for MCP servers
* Support both local and remote MCP servers
* Built-in MCP servers marketplace

### ChatGPT

ChatGPT is OpenAI's AI assistant that provides MCP support for remote servers to conduct deep research.

**Key features:**

* Support for MCP via connections UI in settings
* Access to search tools from configured MCP servers for deep research
* Enterprise-grade security and compliance features

### ChatWise

ChatWise is a desktop-optimized, high-performance chat application that lets you bring your own API keys. It supports a wide range of LLMs and integrates with MCP to enable tool workflows.

**Key features:**

* Tools support for MCP servers
* Offer built-in tools like web search, artifacts and image generation.

### Claude Code

Claude Code is an interactive agentic coding tool from Anthropic that helps you code faster through natural language commands. It supports MCP integration for resources, prompts, tools, and roots, and also functions as an MCP server to integrate with other clients.

**Key features:**

* Full support for resources, prompts, tools, and roots from MCP servers
* Offers its own tools through an MCP server for integrating with other MCP clients

### Claude.ai

[Claude.ai](https://claude.ai) is Anthropic's web-based AI assistant that provides MCP support for remote servers.

**Key features:**

* Support for remote MCP servers via integrations UI in settings
* Access to tools, prompts, and resources from configured MCP servers
* Seamless integration with Claude's conversational interface
* Enterprise-grade security and compliance features

### Claude Desktop App

The Claude desktop application provides comprehensive support for MCP, enabling deep integration with local tools and data sources.

**Key features:**

* Full support for resources, allowing attachment of local files and data
* Support for prompt templates
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security

### Chorus

[Chorus](https://chorus.sh) is a native Mac app for chatting with AIs. Chat with multiple models at once, run tools and MCPs, create projects, quick chat, bring your own key, all in a blazing fast, keyboard shortcut friendly app.

**Key features:**

* MCP support with one-click install
* Built in tools, like web search, terminal, and image generation
* Chat with multiple models at once (cloud or local)
* Create projects with scoped memory
* Quick chat with an AI that can see your screen

### Cline

[Cline](https://github.com/cline/cline) is an autonomous coding agent in VS Code that edits files, runs commands, uses a browser, and more–with your permission at each step.

**Key features:**

* Create and add tools through natural language (e.g. "add a tool that searches the web")
* Share custom MCP servers Cline creates with others via the `~/Documents/Cline/MCP` directory
* Displays configured MCP servers along with their tools, resources, and any error logs

### CodeGPT

[CodeGPT](https://codegpt.co) is a popular VS Code and Jetbrains extension that brings AI-powered coding assistance to your editor. It supports integration with MCP servers for tools, allowing users to leverage external AI capabilities directly within their development workflow.

**Key features:**

* Use MCP tools from any configured MCP server
* Seamless integration with VS Code and Jetbrains UI
* Supports multiple LLM providers and custom endpoints

**Learn more:**

* [CodeGPT Documentation](https://docs.codegpt.co/)

### Continue

[Continue](https://github.com/continuedev/continue) is an open-source AI code assistant, with built-in support for all MCP features.

**Key features:**

* Type "@" to mention MCP resources
* Prompt templates surface as slash commands
* Use both built-in and MCP tools directly in chat
* Supports VS Code and JetBrains IDEs, with any LLM

### Copilot-MCP

[Copilot-MCP](https://github.com/VikashLoomba/copilot-mcp) enables AI coding assistance via MCP.

**Key features:**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities

### Cursor

[Cursor](https://docs.cursor.com/context/mcp#protocol-support) is an AI code editor.

**Key features:**

* Support for MCP tools in Cursor Composer
* Support for roots
* Support for prompts
* Support for elicitation
* Support for both STDIO and SSE

### Daydreams

[Daydreams](https://github.com/daydreamsai/daydreams) is a generative agent framework for executing anything onchain

**Key features:**

* Supports MCP Servers in config
* Exposes MCP Client

### Emacs Mcp

[Emacs Mcp](https://github.com/lizqwerscott/mcp.el) is an Emacs client designed to interface with MCP servers, enabling seamless connections and interactions. It provides MCP tool invocation support for AI plugins like [gptel](https://github.com/karthink/gptel) and [llm](https://github.com/ahyatt/llm), adhering to Emacs' standard tool invocation format. This integration enhances the functionality of AI tools within the Emacs ecosystem.

**Key features:**

* Provides MCP tool support for Emacs.

### fast-agent

[fast-agent](https://github.com/evalstate/fast-agent) is a Python Agent framework, with simple declarative support for creating Agents and Workflows, with full multi-modal support for Anthropic and OpenAI models.

**Key features:**

* PDF and Image support, based on MCP Native types
* Interactive front-end to develop and diagnose Agent applications, including passthrough and playback simulators
* Built in support for "Building Effective Agents" workflows.
* Deploy Agents as MCP Servers

### FlowDown

[FlowDown](https://github.com/Lakr233/FlowDown) is a blazing fast and smooth client app for using AI/LLM, with a strong emphasis on privacy and user experience. It supports MCP servers to extend its capabilities with external tools, allowing users to build powerful, customized workflows.

**Key features:**

* **Seamless MCP Integration**: Easily connect to MCP servers to utilize a wide range of external tools.
* **Privacy-First Design**: Your data stays on your device. We don't collect any user data, ensuring complete privacy.
* **Lightweight & Efficient**: A compact and optimized design ensures a smooth and responsive experience with any AI model.
* **Broad Compatibility**: Works with all OpenAI-compatible service providers and supports local offline models through MLX.
* **Rich User Experience**: Features beautifully formatted Markdown, blazing-fast text rendering, and intelligent, automated chat titling.

**Learn more:**

* [FlowDown website](https://flowdown.ai/)
* [FlowDown documentation](https://apps.qaq.wiki/docs/flowdown/)

### FLUJO

Think n8n + ChatGPT. FLUJO is an desktop application that integrates with MCP to provide a workflow-builder interface for AI interactions. Built with Next.js and React, it supports both online and offline (ollama) models, it manages API Keys and environment variables centrally and can install MCP Servers from GitHub. FLUJO has an ChatCompletions endpoint and flows can be executed from other AI applications like Cline, Roo or Claude.

**Key features:**

* Environment & API Key Management
* Model Management
* MCP Server Integration
* Workflow Orchestration
* Chat Interface

### Genkit

[Genkit](https://github.com/firebase/genkit) is a cross-language SDK for building and integrating GenAI features into applications. The [genkitx-mcp](https://github.com/firebase/genkit/tree/main/js/plugins/mcp) plugin enables consuming MCP servers as a client or creating MCP servers from Genkit tools and prompts.

**Key features:**

* Client support for tools and prompts (resources partially supported)
* Rich discovery with support in Genkit's Dev UI playground
* Seamless interoperability with Genkit's existing tools and prompts
* Works across a wide variety of GenAI models from top providers

### Glama

[Glama](https://glama.ai/chat) is a comprehensive AI workspace and integration platform that offers a unified interface to leading LLM providers, including OpenAI, Anthropic, and others. It supports the Model Context Protocol (MCP) ecosystem, enabling developers and enterprises to easily discover, build, and manage MCP servers.

**Key features:**

* Integrated [MCP Server Directory](https://glama.ai/mcp/servers)
* Integrated [MCP Tool Directory](https://glama.ai/mcp/tools)
* Host MCP servers and access them via the Chat or SSE endpoints
  – Ability to chat with multiple LLMs and MCP servers at once
* Upload and analyze local files and data
* Full-text search across all your chats and data

### GenAIScript

Programmatically assemble prompts for LLMs using [GenAIScript](https://microsoft.github.io/genaiscript/) (in JavaScript). Orchestrate LLMs, tools, and data in JavaScript.

**Key features:**

* JavaScript toolbox to work with prompts
* Abstraction to make it easy and productive
* Seamless Visual Studio Code integration

### Goose

[Goose](https://github.com/block/goose) is an open source AI agent that supercharges your software development by automating coding tasks.

**Key features:**

* Expose MCP functionality to Goose through tools.
* MCPs can be installed directly via the [extensions directory](https://block.github.io/goose/v1/extensions/), CLI, or UI.
* Goose allows you to extend its functionality by [building your own MCP servers](https://block.github.io/goose/docs/tutorials/custom-extensions).
* Includes built-in tools for development, web scraping, automation, memory, and integrations with JetBrains and Google Drive.

### GitHub Copilot coding agent

Delegate tasks to [GitHub Copilot coding agent](https://docs.github.com/en/copilot/concepts/about-copilot-coding-agent) and let it work in the background while you stay focused on the highest-impact and most interesting work

**Key features:**

* Delegate tasks to Copilot from GitHub Issues, Visual Studio Code, GitHub Copilot Chat or from your favorite MCP host using the GitHub MCP Server
* Tailor Copilot to your project by [customizing the agent's development environment](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/customizing-the-development-environment-for-copilot-coding-agent#preinstalling-tools-or-dependencies-in-copilots-environment) or [writing custom instructions](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/best-practices-for-using-copilot-to-work-on-tasks#adding-custom-instructions-to-your-repository)
* [Augment Copilot's context and capabilities with MCP tools](https://docs.github.com/en/enterprise-cloud@latest/copilot/how-tos/agents/copilot-coding-agent/extending-copilot-coding-agent-with-mcp), with support for both local and remote MCP servers

### gptme

[gptme](https://github.com/gptme/gptme) is a open-source terminal-based personal AI assistant/agent, designed to assist with programming tasks and general knowledge work.

**Key features:**

* CLI-first design with a focus on simplicity and ease of use
* Rich set of built-in tools for shell commands, Python execution, file operations, and web browsing
* Local-first approach with support for multiple LLM providers
* Open-source, built to be extensible and easy to modify

### HyperAgent

[HyperAgent](https://github.com/hyperbrowserai/HyperAgent) is Playwright supercharged with AI. With HyperAgent, you no longer need brittle scripts, just powerful natural language commands. Using MCP servers, you can extend the capability of HyperAgent, without having to write any code.

**Key features:**

* AI Commands: Simple APIs like page.ai(), page.extract() and executeTask() for any AI automation
* Fallback to Regular Playwright: Use regular Playwright when AI isn't needed
* Stealth Mode – Avoid detection with built-in anti-bot patches
* Cloud Ready – Instantly scale to hundreds of sessions via [Hyperbrowser](https://www.hyperbrowser.ai/)
* MCP Client – Connect to tools like Composio for full workflows (e.g. writing web data to Google Sheets)

### Jenova

[Jenova](https://jenova.ai) is the best MCP client for non-technical users, especially on mobile.

**Key features:**

* 30+ pre-integrated MCP servers with one-click integration of custom servers
* MCP recommendation capability that suggests the best servers for specific tasks
* Multi-agent architecture with leading tool use reliability and scalability, supporting unlimited concurrent MCP server connections through RAG-powered server metadata
* Model agnostic platform supporting any leading LLMs (OpenAI, Anthropic, Google, etc.)
* Unlimited chat history and global persistent memory powered by RAG
* Easy creation of custom agents with custom models, instructions, knowledge bases, and MCP servers
* Local MCP server (STDIO) support coming soon with desktop apps

### JetBrains AI Assistant

[JetBrains AI Assistant](https://plugins.jetbrains.com/plugin/22282-jetbrains-ai-assistant) plugin provides AI-powered features for software development available in all JetBrains IDEs.

**Key features:**

* Unlimited code completion powered by Mellum, JetBrains’ proprietary AI model.
* Context-aware AI chat that understands your code and helps you in real time.
* Access to top-tier models from OpenAI, Anthropic, and Google.
* Offline mode with connected local LLMs via Ollama or LM Studio.
* Deep integration into IDE workflows, including code suggestions in the editor, VCS assistance, runtime error explanation, and more.

### Kilo Code

[Kilo Code](https://github.com/Kilo-Org/kilocode) is an autonomous coding AI dev team in VS Code that edits files, runs commands, uses a browser, and more.

**Key features:**

* Create and add tools through natural language (e.g. "add a tool that searches the web")
* Discover MCP servers via the MCP Marketplace
* One click MCP server installs via MCP Marketplace
* Displays configured MCP servers along with their tools, resources, and any error logs

### Klavis AI Slack/Discord/Web

[Klavis AI](https://www.klavis.ai/) is an Open-Source Infra to Use, Build & Scale MCPs with ease.

**Key features:**

* Slack/Discord/Web MCP clients for using MCPs directly
* Simple web UI dashboard for easy MCP configuration
* Direct OAuth integration with Slack & Discord Clients and MCP Servers for secure user authentication
* SSE transport support
* Open-source infrastructure ([GitHub repository](https://github.com/Klavis-AI/klavis))

**Learn more:**

* [Demo video showing MCP usage in Slack/Discord](https://youtu.be/9-QQAhrQWw8)

### Langflow

Langflow is an open-source visual builder that lets developers rapidly prototype and build AI applications, it integrates with the Model Context Protocol (MCP) as both an MCP server and an MCP client.

**Key features:**

* Full support for using MCP server tools to build agents and flows.
* Export agents and flows as MCP server
* Local & remote server connections for enhanced privacy and security

**Learn more:**

* [Demo video showing how to use Langflow as both an MCP client & server](https://www.youtube.com/watch?v=pEjsaVVPjdI)

### LibreChat

[LibreChat](https://github.com/danny-avila/LibreChat) is an open-source, customizable AI chat UI that supports multiple AI providers, now including MCP integration.

**Key features:**

* Extend current tool ecosystem, including [Code Interpreter](https://www.librechat.ai/docs/features/code_interpreter) and Image generation tools, through MCP servers
* Add tools to customizable [Agents](https://www.librechat.ai/docs/features/agents), using a variety of LLMs from top providers
* Open-source and self-hostable, with secure multi-user support
* Future roadmap includes expanded MCP feature support

### LM Studio

[LM Studio](https://lmstudio.ai) is a cross-platform desktop app for discovering, downloading, and running open-source LLMs locally. You can now connect local models to tools via Model Context Protocol (MCP).

**Key features:**

* Use MCP servers with local models on your computer. Add entries to `mcp.json` and save to get started.
* Tool confirmation UI: when a model calls a tool, you can confirm the call in the LM Studio app.
* Cross-platform: runs on macOS, Windows, and Linux, one-click installer with no need to fiddle in the command line
* Supports GGUF (llama.cpp) or MLX models with GPU acceleration
* GUI & terminal mode: use the LM Studio app or CLI (lms) for scripting and automation

**Learn more:**

* [Docs: Using MCP in LM Studio](https://lmstudio.ai/docs/app/plugins/mcp)
* [Create a 'Add to LM Studio' button for your server](https://lmstudio.ai/docs/app/plugins/mcp/deeplink)
* [Announcement blog: LM Studio + MCP](https://lmstudio.ai/blog/mcp)

### Lutra

[Lutra](https://lutra.ai) is an AI agent that transforms conversations into actionable, automated workflows.

**Key features:**

* Easy MCP Integration: Connecting Lutra to MCP servers is as simple as providing the server URL; Lutra handles the rest behind the scenes.
* Chat to Take Action: Lutra understands your conversational context and goals, automatically integrating with your existing apps to perform tasks.
* Reusable Playbooks: After completing a task, save the steps as reusable, automated workflows—simplifying repeatable processes and reducing manual effort.
* Shareable Automations: Easily share your saved playbooks with teammates to standardize best practices and accelerate collaborative workflows.

**Learn more:**

* [Lutra AI agent explained](https://www.youtube.com/watch?v=W5ZpN0cMY70)

### mcp-agent

[mcp-agent] is a simple, composable framework to build agents using Model Context Protocol.

**Key features:**

* Automatic connection management of MCP servers.
* Expose tools from multiple servers to an LLM.
* Implements every pattern defined in [Building Effective Agents](https://www.anthropic.com/research/building-effective-agents).
* Supports workflow pause/resume signals, such as waiting for human feedback.

### mcp-client-chatbot

[mcp-client-chatbot](https://github.com/cgoinglove/mcp-client-chatbot) is a local-first chatbot built with Vercel's Next.js, AI SDK, and Shadcn UI.

**Key features:**

* It supports standard MCP tool calling and includes both a custom MCP server and a standalone UI for testing MCP tools outside the chat flow.
* All MCP tools are provided to the LLM by default, but the project also includes an optional `@toolname` mention feature to make tool invocation more explicit—particularly useful when connecting to multiple MCP servers with many tools.
* Visual workflow builder that lets you create custom tools by chaining LLM nodes and MCP tools together. Published workflows become callable as `@workflow_name` tools in chat, enabling complex multi-step automation sequences.

### mcp-use

[mcp-use] is an open source python library to very easily connect any LLM to any MCP server both locally and remotely.

**Key features:**

* Very simple interface to connect any LLM to any MCP.
* Support the creation of custom agents, workflows.
* Supports connection to multiple MCP servers simultaneously.
* Supports all langchain supported models, also locally.
* Offers efficient tool orchestration and search functionalities.

### modelcontextchat.com

[modelcontextchat.com](https://modelcontextchat.com) is a web-based MCP client designed for working with remote MCP servers, featuring comprehensive authentication support and integration with OpenRouter.

**Key features:**

* Web-based interface for remote MCP server connections
* Header-based Authorization support for secure server access
* OAuth authentication integration
* OpenRouter API Key support for accessing various LLM providers
* No installation required - accessible from any web browser

### MCPHub

[MCPHub] is a powerful Neovim plugin that integrates MCP (Model Context Protocol) servers into your workflow.

**Key features:**

* Install, configure and manage MCP servers with an intuitive UI.
* Built-in Neovim MCP server with support for file operations (read, write, search, replace), command execution, terminal integration, LSP integration, buffers, and diagnostics.
* Create Lua-based MCP servers directly in Neovim.
* Inegrates with popular Neovim chat plugins Avante.nvim and CodeCompanion.nvim

### MCPOmni-Connect

[MCPOmni-Connect](https://github.com/Abiorh001/mcp_omni_connect) is a versatile command-line interface (CLI) client designed to connect to various Model Context Protocol (MCP) servers using both stdio and SSE transport.

**Key features:**

* Support for resources, prompts, tools, and sampling
* Agentic mode with ReAct and orchestrator capabilities
* Seamless integration with OpenAI models and other LLMs
* Dynamic tool and resource management across multiple servers
* Support for both stdio and SSE transport protocols
* Comprehensive tool orchestration and resource analysis capabilities

### Memex

[Memex](https://memex.tech/) is the first MCP client and MCP server builder - all-in-one desktop app. Unlike traditional MCP clients that only consume existing servers, Memex can create custom MCP servers from natural language prompts, immediately integrate them into its toolkit, and use them to solve problems—all within a single conversation.

**Key features:**

* **Prompt-to-MCP Server**: Generate fully functional MCP servers from natural language descriptions
* **Self-Testing & Debugging**: Autonomously test, debug, and improve created MCP servers
* **Universal MCP Client**: Works with any MCP server through intuitive, natural language integration
* **Curated MCP Directory**: Access to tested, one-click installable MCP servers (Neon, Netlify, GitHub, Context7, and more)
* **Multi-Server Orchestration**: Leverage multiple MCP servers simultaneously for complex workflows

**Learn more:**

* [Memex Launch 2: MCP Teams and Agent API](https://memex.tech/blog/memex-launch-2-mcp-teams-and-agent-api-private-preview-125f)

### Microsoft Copilot Studio

[Microsoft Copilot Studio] is a robust SaaS platform designed for building custom AI-driven applications and intelligent agents, empowering developers to create, deploy, and manage sophisticated AI solutions.

**Key features:**

* Support for MCP tools
* Extend Copilot Studio agents with MCP servers
* Leveraging Microsoft unified, governed, and secure API management solutions

### MindPal

[MindPal](https://mindpal.io) is a no-code platform for building and running AI agents and multi-agent workflows for business processes.

**Key features:**

* Build custom AI agents with no-code
* Connect any SSE MCP server to extend agent tools
* Create multi-agent workflows for complex business processes
* User-friendly for both technical and non-technical professionals
* Ongoing development with continuous improvement of MCP support

**Learn more:**

* [MindPal MCP Documentation](https://docs.mindpal.io/agent/mcp)

### MooPoint

[MooPoint](https://moopoint.io)

MooPoint is a web-based AI chat platform built for developers and advanced users, letting you interact with multiple large language models (LLMs) through a single, unified interface. Connect your own API keys (OpenAI, Anthropic, and more) and securely manage custom MCP server integrations.

**Key features:**

* Accessible from any PC or smartphone—no installation required
* Choose your preferred LLM provider
* Supports `SSE`, `Streamable HTTP`, `npx`, and `uvx` MCP servers
* OAuth and sampling support
* New features added daily

### Mistral AI: Le Chat

[Mistral AI: Le Chat](https://mistral.ai) is Mistral AI assistant with MCP support for remote servers and enterprise workflows.

**Key features:**

* Remote MCP server integration
* Enterprise-grade security
* Low-latency, high-throughput interactions with structured data

**Learn more:**

* [Mistral MCP Documentation](https://help.mistral.ai/en/collections/911943-connectors)

### Msty Studio

[Msty Studio](https://msty.ai) is a privacy-first AI productivity platform that seamlessly integrates local and online language models (LLMs) into customizable workflows. Designed for both technical and non-technical users, Msty Studio offers a suite of tools to enhance AI interactions, automate tasks, and maintain full control over data and model behavior.

**Key features:**

* **Toolbox & Toolsets**: Connect AI models to local tools and scripts using MCP-compliant configurations. Group tools into Toolsets to enable dynamic, multi-step workflows within conversations.
* **Turnstiles**: Create automated, multi-step AI interactions, allowing for complex data processing and decision-making flows.
* **Real-Time Data Integration**: Enhance AI responses with up-to-date information by integrating real-time web search capabilities.
* **Split Chats & Branching**: Engage in parallel conversations with multiple models simultaneously, enabling comparative analysis and diverse perspectives.

**Learn more:**

* [Msty Studio Documentation](https://docs.msty.studio/features/toolbox/tools)

### NVIDIA Agent Intelligence (AIQ) toolkit

[NVIDIA Agent Intelligence (AIQ) toolkit](https://github.com/NVIDIA/AIQToolkit) is a flexible, lightweight, and unifying library that allows you to easily connect existing enterprise agents to data sources and tools across any framework.

**Key features:**

* Acts as an MCP **client** to consume remote tools
* Acts as an MCP **server** to expose tools
* Framework agnostic and compatible with LangChain, CrewAI, Semantic Kernel, and custom agents
* Includes built-in observability and evaluation tools

**Learn more:**

* [AIQ toolkit GitHub repository](https://github.com/NVIDIA/AIQToolkit)
* [AIQ toolkit MCP documentation](https://docs.nvidia.com/aiqtoolkit/latest/workflows/mcp/index.html)

### OpenSumi

[OpenSumi](https://github.com/opensumi/core) is a framework helps you quickly build AI Native IDE products.

**Key features:**

* Supports MCP tools in OpenSumi
* Supports built-in IDE MCP servers and custom MCP servers

### oterm

[oterm] is a terminal client for Ollama allowing users to create chats/agents.

**Key features:**

* Support for multiple fully customizable chat sessions with Ollama connected with tools.
* Support for MCP tools.

### Roo Code

[Roo Code](https://roocode.com) enables AI coding assistance via MCP.

**Key features:**

* Support for MCP tools and resources
* Integration with development workflows
* Extensible AI capabilities

### Postman

[Postman](https://postman.com/downloads) is the most popular API client and now supports MCP server testing and debugging.

**Key features:**

* Full support of all major MCP features (tools, prompts, resources, and subscriptions)
* Fast, seamless UI for debugging MCP capabilities
* MCP config integration (Claude, VSCode, etc.) for fast first-time experience in testing MCPs
* Integration with history, variables, and collections for reuse and collaboration

### RecurseChat

[RecurseChat](https://recurse.chat) is a powerful, fast, local-first chat client with MCP support. RecurseChat supports multiple AI providers including LLaMA.cpp, Ollama, and OpenAI, Anthropic.

**Key features:**

* Local AI: Support MCP with Ollama models.
* MCP Tools: Individual MCP server management. Easily visualize the connection states of MCP servers.
* MCP Import: Import configuration from Claude Desktop app or JSON

**Learn more:**

* [RecurseChat docs](https://recurse.chat/docs/features/mcp/)

### Shortwave

[Shortwave](https://www.shortwave.com) is an AI-powered email client that supports MCP tools to enhance email productivity and workflow automation.

**Key features:**

* MCP tool integration for enhanced email workflows
* Rich UI for adding, managing and interacting with a wide range of MCP servers
* Support for both remote (Streamable HTTP and SSE) and local (Stdio) MCP servers
* AI assistance for managing your emails, calendar, tasks and other third-party services

### Simtheory

Simtheory is an agentic AI workspace that unifies multiple AI models, tools, and capabilities under a single subscription. It provides comprehensive MCP support through its MCP Store, allowing users to extend their workspace with productivity tools and integrations.

**Key features:**

* **MCP Store**: Marketplace for productivity tools and MCP server integrations
* **Parallel Tasking**: Run multiple AI tasks simultaneously with MCP tool support
* **Model Catalogue**: Access to frontier models with MCP tool integration
* **Hosted MCP Servers**: Plug-and-play MCP integrations with no technical setup
* **Advanced MCPs**: Specialized tools like Tripo3D (3D creation), Podcast Maker, and Video Maker
* **Enterprise Ready**: Flexible workspaces with granular access control for MCP tools

**Learn more:**

* [Simtheory website](https://simtheory.ai)

### Slack MCP Client

[Slack MCP Client](https://github.com/tuannvm/slack-mcp-client) acts as a bridge between Slack and Model Context Protocol (MCP) servers. Using Slack as the interface, it enables large language models (LLMs) to connect and interact with various MCP servers through standardized MCP tools.

**Key features:**

* **Supports Popular LLM Providers:** Integrates seamlessly with leading large language model providers such as OpenAI, Anthropic, and Ollama, allowing users to leverage advanced conversational AI and orchestration capabilities within Slack.
* **Dynamic and Secure Integration:** Supports dynamic registration of MCP tools, works in both channels and direct messages and manages credentials securely via environment variables or Kubernetes secrets.
* **Easy Deployment and Extensibility:** Offers official Docker images, a Helm chart for Kubernetes, and Docker Compose for local development, making it simple to deploy, configure, and extend with additional MCP servers or tools.

### Sourcegraph Cody

[Cody](https://openctx.org/docs/providers/modelcontextprotocol) is Sourcegraph's AI coding assistant, which implements MCP through OpenCTX.

**Key features:**

* Support for MCP resources
* Integration with Sourcegraph's code intelligence
* Uses OpenCTX as an abstraction layer
* Future support planned for additional MCP features

### SpinAI

[SpinAI](https://spinai.dev) is an open-source TypeScript framework for building observable AI agents. The framework provides native MCP compatibility, allowing agents to seamlessly integrate with MCP servers and tools.

**Key features:**

* Built-in MCP compatibility for AI agents
* Open-source TypeScript framework
* Observable agent architecture
* Native support for MCP tools integration

### Superinterface

[Superinterface](https://superinterface.ai) is AI infrastructure and a developer platform to build in-app AI assistants with support for MCP, interactive components, client-side function calling and more.

**Key features:**

* Use tools from MCP servers in assistants embedded via React components or script tags
* SSE transport support
* Use any AI model from any AI provider (OpenAI, Anthropic, Ollama, others)

### Superjoin

[Superjoin](https://superjoin.ai) brings the power of MCP directly into Google Sheets extension. With Superjoin, users can access and invoke MCP tools and agents without leaving their spreadsheets, enabling powerful AI workflows and automation right where their data lives.

**Key features:**

* Native Google Sheets add-on providing effortless access to MCP capabilities
* Supports OAuth 2.1 and header-based authentication for secure and flexible connections
* Compatible with both SSE and Streamable HTTP transport for efficient, real-time streaming communication
* Fully web-based, cross-platform client requiring no additional software installation

### systemprompt

[systemprompt](https://systemprompt.io) is a voice-controlled mobile app that manages your MCP servers. Securely leverage MCP agents from your pocket. Available on iOS and Android.

**Key features:**

* **Native Mobile Experience**: Access and manage your MCP servers anytime, anywhere on both Android and iOS devices
* **Advanced AI-Powered Voice Recognition**: Sophisticated voice recognition engine enhanced with cutting-edge AI and Natural Language Processing (NLP), specifically tuned to understand complex developer terminology and command structures
* **Unified Multi-MCP Server Management**: Effortlessly manage and interact with multiple Model Context Protocol (MCP) servers from a single, centralized mobile application

### Tambo

[Tambo](https://tambo.co) is a platform for building custom chat experiences in React, with integrated custom user interface components.

**Key features:**

* Hosted platform with React SDK for integrating chat or other LLM-based experiences into your own app.
* Support for selection of arbitrary React components in the chat experience, with state management and tool calling.
* Support for MCP servers, from Tambo's servers or directly from the browser.
* Supports OAuth 2.1 and custom header-based authentication.
* Support for MCP tools, with additional MCP features coming soon.

### Tencent CloudBase AI DevKit

[Tencent CloudBase AI DevKit](https://docs.cloudbase.net/ai/agent/mcp) is a tool for building AI agents in minutes, featuring zero-code tools, secure data integration, and extensible plugins via MCP.

**Key features:**

* Support for MCP tools
* Extend agents with MCP servers
* MCP servers hosting: serverless hosting and authentication support

### TheiaAI/TheiaIDE

[Theia AI](https://eclipsesource.com/blogs/2024/10/07/introducing-theia-ai/) is a framework for building AI-enhanced tools and IDEs. The [AI-powered Theia IDE](https://eclipsesource.com/blogs/2024/10/08/introducting-ai-theia-ide/) is an open and flexible development environment built on Theia AI.

**Key features:**

* **Tool Integration**: Theia AI enables AI agents, including those in the Theia IDE, to utilize MCP servers for seamless tool interaction.
* **Customizable Prompts**: The Theia IDE allows users to define and adapt prompts, dynamically integrating MCP servers for tailored workflows.
* **Custom agents**: The Theia IDE supports creating custom agents that leverage MCP capabilities, enabling users to design dedicated workflows on the fly.

Theia AI and Theia IDE's MCP integration provide users with flexibility, making them powerful platforms for exploring and adapting MCP.

**Learn more:**

* [Theia IDE and Theia AI MCP Announcement](https://eclipsesource.com/blogs/2024/12/19/theia-ide-and-theia-ai-support-mcp/)
* [Download the AI-powered Theia IDE](https://theia-ide.org/)

### Tome

[Tome](https://github.com/runebookai/tome) is an open source cross-platform desktop app designed for working with local LLMs and MCP servers. It is designed to be beginner friendly and abstract away the nitty gritty of configuration for people getting started with MCP.

**Key features:**

* MCP servers are managed by Tome so there is no need to install uv or npm or configure JSON
* Users can quickly add or remove MCP servers via UI
* Any tool-supported local model on Ollama is compatible

### TypingMind App

[TypingMind](https://www.typingmind.com) is an advanced frontend for LLMs with MCP support. TypingMind supports all popular LLM providers like OpenAI, Gemini, Claude, and users can use with their own API keys.

**Key features:**

* **MCP Tool Integration**: Once MCP is configured, MCP tools will show up as plugins that can be enabled/disabled easily via the main app interface.
* **Assign MCP Tools to Agents**: TypingMind allows users to create AI agents that have a set of MCP servers assigned.
* **Remote MCP servers**: Allows users to customize where to run the MCP servers via its MCP Connector configuration, allowing the use of MCP tools across multiple devices (laptop, mobile devices, etc.) or control MCP servers from a remote private server.

**Learn more:**

* [TypingMind MCP Document](https://www.typingmind.com/mcp)
* [Download TypingMind (PWA)](https://www.typingmind.com/)

### VS Code GitHub Copilot

[VS Code](https://code.visualstudio.com/) integrates MCP with GitHub Copilot through [agent mode](https://code.visualstudio.com/docs/copilot/chat/chat-agent-mode), allowing direct interaction with MCP-provided tools within your agentic coding workflow. Configure servers in Claude Desktop, workspace or user settings, with guided MCP installation and secure handling of keys in input variables to avoid leaking hard-coded keys.

**Key features:**

* Support for stdio and server-sent events (SSE) transport
* Per-session selection of tools per agent session for optimal performance
* Easy server debugging with restart commands and output logging
* Tool calls with editable inputs and always-allow toggle
* Integration with existing VS Code extension system to register MCP servers from extensions

### Warp

[Warp](https://www.warp.dev/) is the intelligent terminal with AI and your dev team's knowledge built-in. With natural language capabilities integrated directly into an agentic command line, Warp enables developers to code, automate, and collaborate more efficiently -- all within a terminal that features a modern UX.

**Key features:**

* **Agent Mode with MCP support**: invoke tools and access data from MCP servers using natural language prompts
* **Flexible server management**: add and manage CLI or SSE-based MCP servers via Warp's built-in UI
* **Live tool/resource discovery**: view tools and resources from each running MCP server
* **Configurable startup**: set MCP servers to start automatically with Warp or launch them manually as needed

### WhatsMCP

[WhatsMCP](https://wassist.app/mcp/) is an MCP client for WhatsApp. WhatsMCP lets you interact with your AI stack from the comfort of a WhatsApp chat.

**Key features:**

* Supports MCP tools
* SSE transport, full OAuth2 support
* Chat flow management for WhatsApp messages
* One click setup for connecting to your MCP servers
* In chat management of MCP servers
* Oauth flow natively supported in WhatsApp

### Windsurf Editor

[Windsurf Editor](https://codeium.com/windsurf) is an agentic IDE that combines AI assistance with developer workflows. It features an innovative AI Flow system that enables both collaborative and independent AI interactions while maintaining developer control.

**Key features:**

* Revolutionary AI Flow paradigm for human-AI collaboration
* Intelligent code generation and understanding
* Rich development tools with multi-model support

### Witsy

[Witsy](https://github.com/nbonamy/witsy) is an AI desktop assistant, supporting Anthropic models and MCP servers as LLM tools.

**Key features:**

* Multiple MCP servers support
* Tool integration for executing commands and scripts
* Local server connections for enhanced privacy and security
* Easy-install from Smithery.ai
* Open-source, available for macOS, Windows and Linux

### Zed

[Zed](https://zed.dev/docs/assistant/model-context-protocol) is a high-performance code editor with built-in MCP support, focusing on prompt templates and tool integration.

**Key features:**

* Prompt templates surface as slash commands in the editor
* Tool integration for enhanced coding workflows
* Tight integration with editor features and workspace context
* Does not support MCP resources

### Zencoder

[Zencoder](https://zecoder.ai) is a coding agent that's available as an extension for VS Code and JetBrains family of IDEs, meeting developers where they already work. It comes with RepoGrokking (deep contextual codebase understanding), agentic pipeline, and the ability to create and share custom agents.

**Key features:**

* RepoGrokking - deep contextual understanding of codebases
* Agentic pipeline - runs, tests, and executes code before outputting it
* Zen Agents platform - ability to build and create custom agents and share with the team
* Integrated MCP tool library with one-click installations
* Specialized agents for Unit and E2E Testing

**Learn more:**

* [Zencoder Documentation](https://docs.zencoder.ai)

## Adding MCP support to your application

If you've added MCP support to your application, we encourage you to submit a pull request to add it to this list. MCP integration can provide your users with powerful contextual AI capabilities and make your application part of the growing MCP ecosystem.

Benefits of adding MCP support:

* Enable users to bring their own context and tools
* Join a growing ecosystem of interoperable AI applications
* Provide users with flexible integration options
* Support local-first AI workflows

To get started with implementing MCP in your application, check out our [Python](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK Documentation](https://github.com/modelcontextprotocol/typescript-sdk)

## Updates and corrections

This list is maintained by the community. If you notice any inaccuracies or would like to update information about MCP support in your application, please submit a pull request or [open an issue in our documentation repository](https://github.com/modelcontextprotocol/modelcontextprotocol/issues).


# Example Servers

> A list of example servers and implementations

This page showcases various Model Context Protocol (MCP) servers that demonstrate the protocol's capabilities and versatility. These servers enable Large Language Models (LLMs) to securely access tools and data sources.

## Reference implementations

These official reference servers demonstrate core MCP features and SDK usage:

### Current reference servers

* **[Everything](https://github.com/modelcontextprotocol/servers/tree/main/src/everything)** - Reference / test server with prompts, resources, and tools
* **[Fetch](https://github.com/modelcontextprotocol/servers/tree/main/src/fetch)** - Web content fetching and conversion for efficient LLM usage
* **[Filesystem](https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem)** - Secure file operations with configurable access controls
* **[Git](https://github.com/modelcontextprotocol/servers/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
* **[Memory](https://github.com/modelcontextprotocol/servers/tree/main/src/memory)** - Knowledge graph-based persistent memory system
* **[Sequential Thinking](https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking)** - Dynamic and reflective problem-solving through thought sequences
* **[Time](https://github.com/modelcontextprotocol/servers/tree/main/src/time)** - Time and timezone conversion capabilities

### Archived servers (historical reference)

⚠️ **Note**: The following servers have been moved to the [servers-archived repository](https://github.com/modelcontextprotocol/servers-archived) and are no longer actively maintained. They are provided for historical reference only.

#### Data and file systems

* **[PostgreSQL](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)** - Read-only database access with schema inspection capabilities
* **[SQLite](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sqlite)** - Database interaction and business intelligence features
* **[Google Drive](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gdrive)** - File access and search capabilities for Google Drive

#### Development tools

* **[Git](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/git)** - Tools to read, search, and manipulate Git repositories
* **[GitHub](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/github)** - Repository management, file operations, and GitHub API integration
* **[GitLab](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/gitlab)** - GitLab API integration enabling project management
* **[Sentry](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/sentry)** - Retrieving and analyzing issues from Sentry.io

#### Web and browser automation

* **[Brave Search](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/brave-search)** - Web and local search using Brave's Search API
* **[Puppeteer](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/puppeteer)** - Browser automation and web scraping capabilities

#### Productivity and communication

* **[Slack](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack)** - Channel management and messaging capabilities
* **[Google Maps](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/google-maps)** - Location services, directions, and place details

#### AI and specialized tools

* **[EverArt](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/everart)** - AI image generation using various models
* **[AWS KB Retrieval](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/aws-kb-retrieval-server)** - Retrieval from AWS Knowledge Base using Bedrock Agent Runtime

## Official integrations

Visit the [MCP Servers Repository (Official Integrations section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#%EF%B8%8F-official-integrations) for a list of MCP servers maintained by companies for their platforms.

## Community implementations

Visit the [MCP Servers Repository (Community section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-community-servers) for a list of MCP servers maintained by community members.

## Getting started

### Using reference servers

TypeScript-based servers can be used directly with `npx`:

```bash
npx -y @modelcontextprotocol/server-memory
```

Python-based servers can be used with `uvx` (recommended) or `pip`:

```bash
# Using uvx
uvx mcp-server-git

# Using pip
pip install mcp-server-git
python -m mcp_server_git
```

### Configuring with Claude

To use an MCP server with Claude, add it to your configuration:

```json
{
  "mcpServers": {
    "memory": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-memory"]
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "/path/to/allowed/files"
      ]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "<YOUR_TOKEN>"
      }
    }
  }
}
```

## Additional resources

Visit the [MCP Servers Repository (Resources section)](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#-resources) for a collection of other resources and projects related to MCP.

Visit our [GitHub Discussions](https://github.com/orgs/modelcontextprotocol/discussions) to engage with the MCP community.

