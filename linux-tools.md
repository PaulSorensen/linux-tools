# 🐧 LINUX TOOLS

## 🖥️ Desktop Tools

### Application Launchers

* [**ULauncher**](https://ulauncher.io) - Modern and extensible application launcher with plugin support and custom theming. Offers fast fuzzy search, shortcut-based actions, and a minimal UI designed for keyboard-driven workflows.  
  **Tags:** `launcher`, `ui`

### Backup

* [**BorgBackup**](https://www.borgbackup.org) - Secure and efficient deduplicating backup tool for files and directories. Supports fast incremental backups, compression, authenticated encryption, and remote targets over SSH. Archives act as point-in-time snapshots. Not designed for disk imaging or bare-metal recovery.  
  **Tags:** `backup`, `deduplication`
* [**Btrbk**](https://github.com/digint/btrbk) - Backup and snapshot management tool for Btrfs filesystems. Supports atomic snapshots, configurable retention policies, and local or remote (SSH) backups. Designed for efficient, incremental backups using native Btrfs features.  
  **Tags:** `backup`, `btrfs`, `snapshots`
* [**Btrfs Assistant**](https://gitlab.com/btrfs-assistant/btrfs-assistant) - GUI management tool to configure and automate local incremental snapshots of btrfs subvolumes, allowing you to set various intervals (e.g., daily, hourly) and retention policies, customized to fit your needs.  
  **Tags:** `backup`, `btrfs`, `snapshots`
* [**Pika Backup**](https://gitlab.gnome.org/world/pika-backup) - Simple GUI for BorgBackup. It enables encrypted, deduplicated backups to local or remote locations. Focused on ease of use with minimal configuration.  
  **Tags:** `backup`, `deduplication`
* [**Rsync**](https://rsync.samba.org) - Open-source CLI utility for efficient file synchronization and backup. Performs incremental transfers by copying only changed blocks, minimizing data transfer. Supports local and remote operations over SSH, optional preservation of file attributes (permissions, timestamps, ownership), and resuming interrupted transfers. Includes compression, deletion of extraneous files, and dry-run mode.  
  **Tags:** `backup`, `sync`
* [**Snapper**](https://snapper.io) - Snapshot management tool for Btrfs and LVM volumes. Supports automatic and manual snapshots, timeline-based retention, diffing between snapshots, and reverting changes. Commonly integrated with package managers like zypper for pre/post snapshots.  
  **Tags:** `backup`, `btrfs`, `lvm`, `snapshots`
* [**Timeshift**](https://github.com/linuxmint/timeshift?tab=readme-ov-file) - User-friendly system restore tool that creates incremental snapshots of the root filesystem, enabling full system backups and restores. It offers scheduled snapshots (hourly, daily, etc.) and allows restoration from a live environment. Note: Timeshift requires a specific subvolume layout: @ for root and @home for the home directory. Ubuntu and its derivatives (Mint, Pop!_OS, etc.) follow this layout, whereas most other distributions use / and /home directly. As a result, Timeshift cannot perform full system restores on these other distributions without manually renaming subvolumes.  
  **Tags:** `backup`, `restore`, `snapshots`
* [**Yadm**](https://yadm.io) - Powerful dotfile manager using Git, perfect for restoring your custom configs quickly.  
  **Tags:** `backup`, `config`, `dotfiles`, `git`

### Browsers

* [**Midori**](https://astian.org/midori-browser) - Open-source, privacy-focused, telemetry-free browser from Astian, Inc (Astian Foundation). Built on Gecko with built-in ad and tracker blocking, workspace-based tab organization, appearance customization, and support for Firefox add-ons.  
  **Tags:** `mozilla`, `privacy`
* [**Mullvad Browser**](https://mullvad.net/en/browser) - Sweden-based privacy-focused browser developed by Mullvad and the Tor Project. A hardened Mozilla Firefox fork designed to resist tracking, fingerprinting, and surveillance. Includes preconfigured privacy settings, disables telemetry, and isolates site data for anonymous browsing without requiring a VPN.  
  **Tags:** `anonymity`, `mozilla`, `privacy`, `tor`
* [**Vivaldi**](https://vivaldi.com) - Norwegian-based highly customizable privacy-focused browser built on Chromium. Offers advanced tab management, UI flexibility, built-in ad and tracker blocking, mail, calendar, and RSS reader. Can sync tabs, bookmarks, and notes with end-to-end encryption (E2EE) via Vivaldi's own servers hosted in Iceland.  
  **Tags:** `chromium`, `e2ee`, `privacy`

### Cloud Storage

* [**Filen**](https://filen.io) - Germany-based cloud storage provider offering true end-to-end encryption (E2EE). Only you can access your data, and not even Filen has the ability to decrypt it, making it a fully zero-knowledge platform. Supporting continuous sync, selective sync, flexible sync options (one-way, two-way, etc), network drive, WebDav, and Rclone. Mobile app let's you edit numerous files directly. Integrated encrypted notes.  
  **Tags:** `backup`, `e2ee`, `privacy`, `sync`

### Development

* [**Git**](https://git-scm.com) - Open-source distributed version control system for tracking changes to any type of file. Supports local and remote repositories, fast branching and merging, rebasing, stashing, patch workflows, and efficient handling of large projects. Created by Linus Torvalds and maintained by the Git community.  
  **Tags:** `git`
* [**Pycharm**](https://www.jetbrains.com/pycharm/download) - Feature-rich Python IDE by JetBrains with advanced editing, debugging, and project management features. Offers a free Community edition for personal and open-source use.  
  **Tags:** `code`, `dev`, `editor`, `ide`, `python`
* [**Rider**](https://www.jetbrains.com/rider) - Powerful .NET and Unity IDE alternative to Visual Studio. Feature-rich and extensible, with full NuGet support and deep language tooling. Offers a free version for personal and open-source use, but collects anonymized usage data.  
  **Tags:** `code`, `dev`, `dotnet`, `editor`, `ide`, `unity`
* [**Sublime Merge**](https://www.sublimemerge.com) - Git client with built-in merge conflict resolution, line-by-line staging, and syntax-highlighted diffs. Offers full Git command visibility, powerful history search, submodule management, and Git Flow support.  
  **Tags:** `git`
* [**Sublime Text**](https://www.sublimetext.com) - Lightweight and extensible code editor with a fast interface and powerful features like multi-cursor editing, split panes, and a rich plugin ecosystem.  
  **Tags:** `code`, `dev`, `editor`
* [**VSCodium**](https://vscodium.com) - Open-source community-driven version of VSCode without telemetry or proprietary additions, hence Settings Sync and other Microsoft features are not available. Compatible with most VSCode extensions via the Open VSX registry or manual installation. Some Microsoft extensions (e.g., Copilot, Live Share, Python, Remote tools) are restricted by license or code checks. Replacements exist for common use cases like C/C++, Python, and SSH remote editing.  
  **Tags:** `code`, `dev`, `editor`, `vscode`
* [**Visual Studio Code**](https://code.visualstudio.com) - Popular code editor with a strong extension ecosystem and deep GitHub integration, including Copilot. Supports debugging, terminals, and language servers out of the box.  
  **Tags:** `code`, `copilot`, `dev`, `editor`, `vscode`
* [**Zed**](https://zed.dev) - Open-source code editor with multibuffer editing, built-in terminal, native Git support, remote development, and Vim bindings. Includes AI-assisted coding via inline transformations and a context-aware assistant panel powered by Claude Sonnet and Zed’s own open-source LLM, Zeta.  
  **Tags:** `code`, `dev`, `editor`

### Download Managers

* [**KTorrent**](https://apps.kde.org/ktorrent) - BitTorrent client developed by KDE, offering queuing, prioritization, selective downloading, DHT, UDP tracker support, IP filtering, plugin system, per-torrent speed limits, file preview, and peer management including kick/ban functionality.  
  **Tags:** `download`, `p2p`, `torrent`
* [**Persepolis**](https://persepolisdm.github.io) - Open-source GUI download manager built on top of aria2. Supports multi-segment downloading, scheduling, queues, and video downloads from sites like YouTube and Vimeo. Integration for Firefox and Chromium-based browsers.  
  **Tags:** `aria2`, `download`, `http`

### Fan, Sensors & RGB

* [**CoolerControl**](https://docs.coolercontrol.org) - Feature-rich fan, pump, and RGB control tool. Supports system sensors, GPU fan control, AIOs, profiles, modes, alerts, and custom sensors. Includes a GUI, system daemon, and Web UI for real-time monitoring and automation.  
  **Tags:** `aio`, `fan`, `monitoring`, `rgb`, `sensors`
* [**Lm-sensors**](https://github.com/lm-sensors/lm-sensors) - Collection of tools for monitoring temperatures, voltages, and fan speeds from supported hardware sensors. Includes the sensors command for reading sensor data and sensors-detect for scanning available sensor modules. Commonly used by system monitors and fan control utilities.  
  **Tags:** `fan`, `monitoring`, `sensors`
* [**Mbpfan**](https://github.com/linux-on-mac/mbpfan) - Fan control daemon for Apple hardware using coretemp and applesmc kernel modules. Dynamically adjusts fan speed based on CPU temperatures, as well as support for custom configuration. Runs as a daemon or foreground process with verbose mode.  
  **Tags:** `apple`, `fan`, `monitoring`, `sensors`

### File Transfer

* [**Filezilla Pro**](https://filezillapro.com) - Powerful, feature-rich file transfer client supporting multiple protocols including FTP, FTPS, SFTP, S3, WebDAV, Azure Storage, Dropbox, and more.  
  **Tags:** `filetransfer`, `ftp`, `s3`, `sftp`, `webdav`
* [**LocalSend**](https://localsend.org) - Open-source, cross-platform tool for secure local file transfer over Wi-Fi. Uses end-to-end encrypted, peer-to-peer communication with no internet or central server required. Automatically discovers nearby devices with a clean, registration-free UI.  
  **Tags:** `filetransfer`, `p2p`, `privacy`

### Gaming

* [**Steam**](https://store.steampowered.com/about) - Game distribution platform by Valve. On Linux, it supports both native and Windows games using Proton, a built-in compatibility layer. You can also add non-Steam Windows games and run them through Proton, and even old DOS games in combination with DOSBox. Offers official .deb package. For Fedora, I recommend installing it via RPM Fusion.  
  **Tags:** `gaming`, `proton`

### Imaging

* [**GIMP**](https://www.gimp.org) - Open-source advanced image editor. Supports layers, masks, scripting, and a wide range of formats. Suitable for photo retouching, image composition, and graphic design. Not a direct comparison to Photoshop.  
  **Tags:** `design`, `image`
* [**Inkscape**](https://inkscape.org) - Open-source vector graphics editor supporting the full SVG standard. Offers advanced features like node editing, layers, gradients, text-on-path, and complex path operations. Imports raster and vector formats including EPS, PNG, JPEG, and exports to PNG and multiple vector formats.  
  **Tags:** `design`, `image`, `svg`, `vector`
* [**PhotoGIMP**](https://github.com/diolinux/photogimp) - Custom GIMP configuration that mimics Photoshop’s layout, appearance, and keyboard shortcuts. Aims to ease the transition for users familiar with Adobe Photoshop.  
  **Tags:** `design`, `image`, `photoshop`
* [**Photopea**](https://www.photopea.com) - Czech Republic-based, free advanced image editor with a Photoshop-like interface. Runs entirely in the browser, processing images locally without uploading to a server. Suitable for users familiar with Adobe Photoshop.  
  **Tags:** `design`, `image`, `photoshop`
* [**Qimgv**](https://github.com/easymodo/qimgv) - Open-source, fast, minimalist image viewer inspired by ACDSee/XnView/IrfanView. Supports keyboard shortcuts, folder browsing, basic image editing, and custom shell scripts for actions like setting wallpapers or batch processing.  
  **Tags:** `image`, `viewer`

### Media Creation

* [**BalenaEtcher**](https://etcher.balena.io) - Open-source ISO writer. Supports Linux, macOS, and Windows. Offers no advanced options but writes any bootable ISO to USB drives or SD cards.  
  **Tags:** `boot`, `iso`, `liveusb`, `media-creation`
* [**Fedora Media Writer**](https://docs.fedoraproject.org/en-us/fedora/latest/preparing-boot-media) - Open-source ISO writing tool developed by the Fedora Project. Officially recommended for creating Fedora boot media, it supports Linux, macOS, and Windows. Can download and write Fedora editions (KDE Plasma Desktop, Workstation, Server, Spins, Labs), or write any local ISO. Overwrites the drive's partition layout using a dd-like method.  
  **Tags:** `boot`, `iso`, `liveusb`, `media-creation`
* [**Ventoy**](https://www.ventoy.net) - Open-source tool for creating multiboot USB drives. Supports direct booting of ISO, WIM, IMG, VHD(x), and EFI files without extraction. Write Ventoy to a USB, copy files onto it, and boot from them via a dynamic GRUB-based menu. Compatible with BIOS and UEFI (Secure Boot), MBR and GPT, and tested with 1200+ OS images. Supports persistence, auto-install scripts, and plugin-based customization.  
  **Tags:** `boot`, `iso`, `liveusb`, `media-creation`

### Messaging

* [**Ferdium**](https://ferdium.org) - Open-source privacy-focused messaging tool that unifies multiple services (e.g. Signal, Telegram, Slack) into a single interface. Supports custom services, workspaces, and isolated sessions. No account required.  
  **Tags:** `messaging`, `privacy`
* [**Session**](https://getsession.org) - Fully anonymous, end-to-end encrypted messaging app built on a decentralized network. Open-source, with no tracking, data collection, phone number, or email required. Metadata-resistant and privacy-focused by design.  
  **Tags:** `anonymity`, `e2ee`, `messaging`, `privacy`

### Multimedia

* [**Grayjay**](https://grayjay.app) - Open-source, privacy-focused, ad-free multi-platform media streamer that lets you follow creators and stream content from YouTube, Rumble, Twitch, SoundCloud, Apple Podcasts, etc. without registering. Subscriptions and playlists are saved locally and can be synced across devices (Android, Linux, Windows, macOS).  
  **Tags:** `audio`, `media`, `player`, `podcast`, `video`
* [**Spotify**](https://www.spotify.com/de-en/download/linux) - Music and podcast streaming service. Official client available via Snap and .deb packages. No official RPM support, but a maintained RPM package is provided by negativo17.org. A community-maintained Flatpak version is also available via Flathub.  
  **Tags:** `audio`, `media`, `player`, `podcast`, `streaming`
* [**VLC**](https://www.videolan.org) - Open-source, cross-platform media player supporting nearly all audio and video codecs without external dependencies. Offers advanced playback controls, streaming support, subtitle synchronization, and broad format compatibility. Developed by the non-profit VideoLAN in France.  
  **Tags:** `audio`, `media`, `player`, `video`

### Networking

* [**Curl**](https://curl.se) - Open-source CLI tool for transferring data across a wide range of protocols, including HTTP(S), FTP(S), SFTP, SCP, SMTP(S), MQTT, and more. Supports proxy chains, authentication (Basic, Bearer, Kerberos, etc.), DNS-over-HTTPS, TLS with mutual authentication, parallel transfers, rate limiting, and custom headers. Commonly used for scripting, API testing, and automation.  
  **Tags:** `http`, `networking`, `transfer`
* [**Nmap**](https://nmap.org) - Open-source network scanner for mapping hosts and services. Supports TCP/UDP port scanning, OS detection, version detection, traceroute, scriptable service interrogation (NSE), and firewall evasion. Works on most platforms and can output to text, XML, JSON, or grepable formats. Commonly used for auditing, inventory, and debugging.  
  **Tags:** `networking`, `scanner`, `security`

### Office and Productivity

* [**Joplin**](https://joplinapp.org) - Open-source, privacy-first note-taking app with full end-to-end encryption (E2EE). It works across all major platforms and syncs seamlessly between devices. You can store your notes in Joplin Cloud or use Dropbox, OneDrive, Nextcloud, WebDAV, local file system, or S3-compatible storage – including free Cloudflare R2. It’s very flexible and secure.  
  **Tags:** `e2ee`, `notes`, `privacy`, `sync`
* [**LibreOffice**](https://www.libreoffice.org) - Open-source, full-featured office suite maintained by The Document Foundation. Includes Writer, Calc, Impress, Draw, and Math for working with documents, spreadsheets, presentations, vector graphics, and formulas. Offers native ODF support, and reasonable compatibility with Microsoft Office formats.  
  **Tags:** `documents`, `office`, `pdf`, `spreadsheets`
* [**MarkText**](https://www.marktext.cc) - Open-source Markdown editor with a clean, distraction-free interface. Supports CommonMark and GitHub Flavored Markdown, math expressions (KaTeX), diagrams (Flowchart, Sequence, Gantt), front matter, and export to HTML/PDF. Includes image pasting, themes, and editing modes like Typewriter and Focus.  
  **Tags:** `editor`, `markdown`
* [**OnlyOffice**](https://www.onlyoffice.com) - Latvia-based, privacy-first, open-source office suite with no telemetry. Offers encryption and integrates with platforms like Nextcloud. Offers documents, spreadsheets, presentations, and PDFs. Great support for Microsoft Office Word documents, and Excel sheets. Modern, sleek and familiar user-interface.  
  **Tags:** `documents`, `office`, `pdf`, `spreadsheets`

### Password Managers

* [**NordPass**](https://nordpass.com) - Zero-knowledge architecture, end-to-end encrypted using xChaCha20, built-in authenticator (TOTP), password health reports, data breach scanner, and passkey support. Developed by Nord Security. Offers a free plan with cross-platform sync.  
  **Tags:** `e2ee`, `password`, `privacy`, `security`

### Recovery

* [**TestDisk**](https://www.cgsecurity.org) - Open-source CLI tool for recovering lost partitions and repairing unbootable disks. Supports ext4, btrfs, xfs, LUKS, LVM, RAID, and other filesystems. Can rebuild partition tables, recover boot sectors, and undelete files. Includes PhotoRec, which performs raw signature-based file recovery even on formatted or severely damaged media.  
  **Tags:** `boot`, `partition`, `recovery`, `rescue`

### Shell

* [**Starship**](https://starship.rs) - Fast, minimal, and highly customizable shell prompt written in Rust. Displays contextual information like Git status, Python versions, runtime info, and exit codes. Works across shells and terminals with a single unified configuration file.  
  **Tags:** `shell`
* [**Tabby**](https://tabby.sh) - Modern, feature-rich, and highly customizable terminal emulator. Supports SSH profiles with key-based authentication for easy remote access and session management.  
  **Tags:** `shell`, `ssh`, `terminal`

### System Info

* [**Btop**](https://github.com/aristocratos/btop) - Open-source CLI resource monitor that displays system usage and stats for CPU, memory, disks, network, processes, and GPU. Offers an interactive UI with mouse support, sortable process views, themes, and extensive configuration options.  
  **Tags:** `sysinfo`
* [**Dysk**](https://dystroy.org/dysk) - Fast and minimal CLI tool written in Rust for exploring disk usage across mounted filesystems. Gives a quick overview of device types (e.g., SSD, HDD, LVM, encrypted), usage stats, and mount options. Supports JSON and CSV output, filtering, and SI/binary units.  
  **Tags:** `disk`, `filesystem`
* [**Fastfetch**](https://github.com/fastfetch-cli/fastfetch) - Open-source system information CLI tool inspired by Neofetch (archived in 2024). Displays system details with customizable ASCII or logo output and supports a wide range of configurations.  
  **Tags:** `sysinfo`

### VPN

* [**NordVPN**](https://nordvpn.com) - Panama-based, privacy-focused VPN provider with a strict no-log policy, strong encryption, and ~8000 servers in 118 countries. Owned by Nord Security, a Netherlands-based cybersecurity company. Known for consistent speed and a strong stance on privacy. Their client works great on Linux.  
  **Tags:** `encryption`, `privacy`, `vpn`

## 🛢️ Server Tools

### Automation

* [**AWX**](https://github.com/ansible/awx) - Open-source web-based interface, REST API, and task engine built on top of Ansible for managing playbooks, inventories, and credentials. Provides role-based access control, job scheduling, logging, and visual inventory management. AWX is the upstream project for Red Hat Ansible Automation Platform, originally developed and maintained by Ansible, Inc., and now maintained by Red Hat.  
  **Tags:** `automation`, `devops`, `infrastructure`, `orchestration`, `sysadmin`
* [**Ansible**](https://github.com/ansible/ansible) - Open-source automation tool for configuration management, software provisioning, and infrastructure orchestration. It allows administrators to define system state using YAML-based playbooks. Tasks include installing packages, configuring services, managing users, deploying applications, applying security policies, and provisioning cloud infrastructure. Ansible is agentless, and operates over SSH. Originally developed by Ansible, Inc., it's now maintained by Red Hat and widely adopted in enterprise environments.  
  **Tags:** `automation`, `devops`, `infrastructure`, `ssh`, `sysadmin`

### Containerization

* [**K3s**](https://k3s.io) - Open-source, lightweight, certified Kubernetes distribution optimized for edge, IoT, CI, and resource-constrained environments. Packaged as a single <70MB binary with minimal dependencies, it simplifies installation and reduces overhead. Includes a slim control plane, built-in components (containerd, Flannel, Traefik), and features like automatic TLS, node registration, and multi-arch support. Ideal for unattended deployments and remote locations. Originally developed by Rancher Labs and now a sandbox project under the CNCF.  
  **Tags:** `automation`, `containers`, `kubernetes`, `orchestration`, `pod`
* [**Kubernetes**](https://kubernetes.io) - Open-source system for automating the deployment, scaling, and management of containerized applications. Groups containers into pods and orchestrates service discovery, internal load balancing, storage via CSI drivers, secret and config management, health checks, rolling updates, autoscaling, and self-healing. Can run on-premises, in the cloud, or across hybrid environments. Originally developed by Google and now a graduated project under the CNCF.  
  **Tags:** `automation`, `containers`, `kubernetes`, `orchestration`, `pod`
* [**Podman**](https://podman.io) - Open-source container engine that runs pods and containers without a central daemon, improving security, preventing global failure from daemon crashes, and enabling rootless operation. Supports systemd integration, Docker-compatible CLI and images, Kubernetes-style pod workflows, YAML generation for deployment to Kubernetes environments. Developed by Red Hat and has replaced Docker in RHEL, CentOS Stream, and Fedora. Integrates with Cockpit and offers a standalone GUI via Podman Desktop.  
  **Tags:** `containers`, `devops`, `podman`, `sysadmin`
* [**Podman Desktop**](https://podman-desktop.io) - Open-source GUI for managing containers and Kubernetes workflows. Supports Podman, Docker, and other OCI-compliant runtimes. Enables container lifecycle management, Compose support, local cluster creation (Minikube, Kind), and deployment to Kubernetes. Includes logs, metrics, extensions, GPU acceleration, and integrates with VS Code. Originally developed by Red Hat and now a sandbox project under the CNCF.  
  **Tags:** `containers`, `docker`, `kubernetes`, `pod`, `podman`

### DNS

* [**Cloudflared**](https://github.com/cloudflare/cloudflared) - DNS-over-HTTPS (DoH) proxy and lightweight DNS forwarder to encrypt DNS traffic from LAN devices. Often integrated with Pi-hole to provide encrypted upstream DNS while maintaining local network-level ad blocking. Can also be used as a tunnel agent that connects local services to Cloudflare’s network via outbound connections. Proxy requires no account, while tunneling requires Cloudflare login and domain setup.  
  **Tags:** `cloudflare`, `dns`, `doh`, `proxy`, `tunnel`
* [**Pi-hole**](https://pi-hole.net) - Open-source network-wide ad blocker that acts as a DNS sinkhole, blocking ads, trackers, and malicious domains for all connected devices. Features include a web dashboard, per-client rules, regex and wildcard blocklists, built-in DHCP server, conditional forwarding, and multiple privacy modes. Easily extendable with custom blocklists and integrations like VPNs. Lightweight and ideal for home servers or Raspberry Pi.  
  **Tags:** `adblock`, `dns`, `lan`, `privacy`

### Database

* [**MariaDB**](https://mariadb.org) - Open-source, multi-threaded relational database developed by Michael "Monty" Widenius, the original creator of MySQL, after its acquisition by Oracle. Released under the GPL, MariaDB supports ACID transactions, multiple storage engines, replication, encryption, and modern SQL features like CTEs, window functions, and JSON. Includes clustering via Galera and remains fully SQL-compliant.  
  **Tags:** `rdb`, `sql`
* [**MongoDB**](https://www.mongodb.com) - Document-based NoSQL database with dynamic schema support, ACID transactions, indexing, full-text and geospatial search, and aggregation pipelines for filtering and transforming data. Key features include replica sets, sharding, encryption at rest and in transit, time-series support, a CLI shell, and tools like MongoDB Compass and VS Code integration. A free Community Edition is available.  
  **Tags:** `document`, `index`, `nosql`
* [**PostgreSQL**](https://www.postgresql.org) - Open-source, SQL-compliant relational database with full ACID support. Features include MVCC, advanced indexing (GIN, GiST, BRIN), table partitioning, window functions, and CTEs. Supports stored procedures in multiple languages, JSONB for semi-structured data, full-text search, and hstore for key-value storage. Allows custom data types, extensions, and logical replication.  
  **Tags:** `rdb`, `sql`
* [**RavenDB**](https://ravendb.net) - Open-source, document-based NoSQL database designed for high performance, scalability, and ease of use. RavenDB provides ACID guarantees, automatic indexing, full-text and spatial search, time-series support, and a SQL-like query language (Raven Query Language, RQL). Key features include real-time replication, automatic failover, encryption at rest and in transit, and a web-based UI. It supports distributed counters, data subscriptions, and flexible schema evolution.  
  **Tags:** `document`, `index`, `nosql`
* [**Reddis**](https://redis.io) - Open-source, in-memory data store designed for sub-millisecond latency. Redis supports key-value pairs and advanced data structures such as lists, sets, sorted sets, hashes, bitmaps, geospatial indexes, streams, and probabilistic types. Key features include persistence to disk, built-in replication, pub/sub messaging, and Lua scripting. It offers optional modules for full-text search, time-series, vector search, and JSON document storage. Commonly used for caching, session storage, message queues, and real-time analytics.  
  **Tags:** `caching`, `document`, `index`, `nosql`

### Database Management

* [**DBeaver**](https://dbeaver.io) - Universal database tool available in a free, open-source Community edition and a commercial PRO version. The Community edition supports all databases with a JDBC driver, including MySQL, PostgreSQL, Oracle, SQL Server, SQLite, and many more. It features a SQL editor, ER diagrams, data browser, schema tools, and import/export utilities. The PRO version adds advanced features like NoSQL and cloud database support, visual query building, metadata tools, and AI-assisted SQL.  
  **Tags:** `nosql`, `sql`

### Media

* [**Audiobookshelf**](https://www.audiobookshelf.org) - Open-source audiobook and podcast server with real-time streaming, metadata editing, multi-user playback sync, Chromecast support, and mobile apps. Includes chapter editing, e-book support, and automated metadata backups. Requires WebSocket support when reverse proxied.  
  **Tags:** `audio`, `audiobook`, `media`, `podcast`, `streaming`
* [**Jellyfin**](https://jellyfin.org) - Open-source media server for organizing and streaming movies, shows, music, books, and photos. Includes features like live TV, DVR, and SyncPlay, which lets multiple users watch content in sync. Offers a polished, Netflix-style UI and streams to nearly any device, including web, smart TVs, iOS, Android, Roku, Kodi, and more.  
  **Tags:** `audio`, `media`, `streaming`, `video`

### Monitoring

* [**Cert Expiry Bot**](https://github.com/paulsorensen/cert-expiry-bot) - Open-source lightweight Bash script that monitors SSL certificate expiration for multiple domains and sends Telegram alerts when certificates are nearing expiry. Other notification services can be easily implemented. It checks for expirations within configurable timeframes (defaulting to 14 and 7 days) and includes error handling for invalid domains or missing certificates. Easy to configure via a .conf file and designed to run unattended.  
  **Tags:** `alerting`, `automation`, `monitoring`, `ssl`, `sysadmin`
* [**Grafana**](https://grafana.com/oss/grafana) - Open-source platform for visualizing and correlating time-series data. While often referred to as a monitoring solution, Grafana itself does not collect data. It connects to external sources like Prometheus, Loki, InfluxDB, and Elasticsearch to display metrics, logs, and events in customizable dashboards. Includes powerful alerting, annotations, and user access control. Widely used as the visualization layer in modern observability stacks.  
  **Tags:** `alerting`, `dashboard`, `infrastructure`, `monitoring`, `sysadmin`
* [**Prometheus**](https://prometheus.io) - Open-source monitoring and alerting toolkit originally developed at SoundCloud and now a graduated project under the Cloud Native Computing Foundation. It collects time series metrics via a pull model, supports powerful queries with PromQL, and integrates with service discovery. Includes Alertmanager for alerting and pairs well with Grafana for visualization.  
  **Tags:** `alerting`, `dashboard`, `infrastructure`, `monitoring`, `sysadmin`
* [**Uptime Kuma**](https://uptime.kuma.pet) - Open-source monitoring tool with a modern web UI. It supports monitoring of HTTP(s), TCP, ICMP (ping), DNS, keyword and JSON responses, Steam game servers, Docker containers, and more. Features include customizable notifications (via Telegram, Discord, email, and over 90 services), multiple status pages, SSL certificate monitoring, and 2FA support. Easy to deploy via Docker or Node.js, it's ideal for home labs and private servers.  
  **Tags:** `alerting`, `dashboard`, `infrastructure`, `monitoring`, `sysadmin`
* [**Zabbix**](https://www.zabbix.com) - Latvia-based, open-source, monitoring solution for networks, servers, virtual machines, containers, IoT, applications, and cloud services. Offers real-time metrics collection, alerting, customizable dashboards, historical data analysis, and automated remediation. Scalable and extensible, with support for agent-based and agentless monitoring, SNMP, IPMI, JMX, and various APIs. Widely used in enterprise and infrastructure environments.  
  **Tags:** `alerting`, `dashboard`, `infrastructure`, `monitoring`, `sysadmin`

### System Management

* [**Cockpit**](https://cockpit-project.org) - Free, open-source web-based server admin interface sponsored by Red Hat. While primarily developed by Red Hat engineers, it’s community-driven and available on most major Linux distributions. Cockpit provides a browser-based UI to manage networking, firewall, storage, user accounts, virtual machines, containers, system logs (including SELinux), systemd services, hardware, performance, and overall system monitoring. It allows software upgrades, includes a built-in terminal, and supports add-ons and custom modules.  
  **Tags:** `cockpit`, `containers`, `devops`, `infrastructure`, `monitoring`, `podman`, `sysadmin`, `virtualization`
* [**Cockpit Sensors**](https://github.com/ocristopfer/cockpit-sensors) - Open-source Cockpit module that visualizes system sensor data via lm-sensors. Adds temperature, fan, and voltage monitoring to the Cockpit web UI.  
  **Tags:** `cockpit`, `monitoring`, `sensors`

### VPN

* [**NetBird**](https://netbird.io) - Open-source, WireGuard-based VPN platform combining Zero Trust Network Access with peer-to-peer overlay networking. Supports NAT traversal, granular access control, identity provider integration, and MFA. Designed for simplicity, cross-platform compatibility, and ease of self-hosting under a permissive BSD-3 license.  
  **Tags:** `encryption`, `privacy`, `vpn`
* [**PiVPN**](https://www.pivpn.io) - Open-source shell script toolkit for deploying a secure WireGuard or OpenVPN server on Raspberry Pi or any Debian/Ubuntu-based system. Designed for simplicity, it offers a one-command installer and a management utility (pivpn) to create, revoke, and manage clients. Supports custom ports, DNS, unattended upgrades, hardened crypto, and integration with Pi-hole and Bitwarden.  
  **Tags:** `encryption`, `privacy`, `vpn`
* [**WireGuard**](https://www.wireguard.com) - Open-source VPN protocol and software for both server and client use. Built into the Linux kernel since 5.6, offering unmatched performance and efficiency. Uses modern cryptography (Noise protocol, ChaCha20, Curve25519) with a minimal attack surface. Supports roaming, containerization, and acts as the core for many commercial VPN services.  
  **Tags:** `encryption`, `privacy`, `vpn`

### Virtualization

* [**Libvirt**](https://libvirt.org) - Abstraction layer and management API for virtual machines. Interacts with KVM and QEMU to manage VM lifecycle, storage, and networking. Provides a consistent interface for automation and system integration.  
  **Tags:** `emulation`, `kvm`, `virtualization`, `vm`
* [**Proxmox Virtual Environment**](https://www.proxmox.com/en/products/proxmox-virtual-environment/overview) - Open-source server virtualization platform that combines KVM for full virtualization and LXC for lightweight containers. Proxmox VE includes web-based management, clustering, live migration, high availability, software-defined networking, and storage support via ZFS, Ceph, and LVM.  
  **Tags:** `containers`, `infrastructure`, `kvm`, `virtualization`, `vm`
* [**QEMU**](https://www.qemu.org) - User-space emulator and virtualizer that provides full-system emulation. When paired with KVM - a Linux kernel module that enables hardware-assisted virtualization, QEMU can run VMs with near-native performance by executing code directly on the host CPU. Commonly used with libvirt, which provides an abstraction layer and management tools for virtual environments.  
  **Tags:** `emulation`, `kvm`, `virtualization`, `vm`
* [**Virtual Machine Manager**](https://virt-manager.org) - Graphical frontend for libvirt. Allows users to create, configure, and manage virtual machines using QEMU/KVM through a user-friendly interface. Supports snapshots, live migration, virtual networks, and storage pools.  
  **Tags:** `emulation`, `kvm`, `virtualization`, `vm`

### Web & Proxy

* [**Caddy**](https://caddyserver.com) - Open-source web server, reverse proxy, and load balancer with automatic HTTPS and modern TLS defaults out of the box. Designed for simplicity and security, Caddy automatically provisions and renews TLS certificates using Let's Encrypt or internal CAs. It supports HTTP, FastCGI, gRPC, WebSockets, and dynamic upstreams. Features include configuration via Caddyfile or JSON API, extensible middleware, request matching, and rate limiting. Especially well-suited for individuals or teams who want secure-by-default deployments with minimal configuration overhead.  
  **Tags:** `http`, `loadbalancer`, `proxy`, `tls`, `webserver`
* [**NGINX**](https://nginx.org) - Open-source, high-performance HTTP server, reverse proxy, IMAP/POP3/SMTP proxy, and load balancer. Known for exceptional stability and low resource use, with a modular architecture and asynchronous design. Supports static file serving, FastCGI, TLS/SSL, HTTP/2 and HTTP/3, virtual hosts, caching, rate limiting, geolocation, and scripting via njs or embedded Perl. The most widely used web server globally.  
  **Tags:** `http`, `loadbalancer`, `proxy`, `tls`, `webserver`
* [**Traefik**](https://traefik.io) - Open-source reverse proxy, ingress controller, and dynamic edge router built for containerized and cloud-native environments. Automatically discovers services and configures routing through integrations with Kubernetes, Docker, Consul, and more. Supports HTTP, TCP, UDP, Websockets, gRPC, and automatic TLS via Let's Encrypt. Provides middleware for load balancing, retries, circuit breakers, authentication, rate limiting, mirroring, and more. Ideal for dynamic microservice architectures.  
  **Tags:** `containers`, `kubernetes`, `loadbalancer`, `proxy`, `tls`

## 🛠️ Bootable Tools

### Rescue

* [**GParted**](https://gparted.org) - Open-source partition editor for managing disks via a graphical interface. Supports creating, deleting, resizing, and cloning partitions across many filesystems including ext4, btrfs, xfs, and NTFS. Often used from a live USB in rescue scenarios. Includes `dd`, enabling full disk restoration or duplication in critical scenarios.  
  **Tags:** `liveusb`, `partition`, `rescue`
* [**Rescatux**](https://www.supergrubdisk.org/rescatux) - Open-source Debian-based live USB with a GUI wizard (Rescapp) for repairing Linux and Windows systems. Supports GRUB1/2 restore, MBR and EFI boot repair, UEFI entry creation, Windows password reset, sudoers regeneration, and filesystem checks. Includes GPT repair tools and GParted, TestDisk, and PhotoRec. Designed to guide less technical users through common rescue tasks.  
  **Tags:** `boot`, `liveusb`, `partition`, `recovery`, `rescue`
* [**Rescuezilla**](https://rescuezilla.com) - Open-source live USB recovery tool offering a graphical front-end for Clonezilla. Enables full disk imaging, backup, and restore across Windows, Linux, and macOS. Supports VirtualBox, VMware, and QEMU images. Includes tools to recover deleted files, access data from unbootable systems, and browse the internet. Note: Cloning Btrfs often fails due to Clonezilla limitations - for those partitions, GParted with `dd` is more reliable in practice.  
  **Tags:** `backup`, `imaging`, `liveusb`, `rescue`
* [**Super Grub2 Disk**](https://www.supergrubdisk.org/super-grub2-disk) - Open-source boot-focused live tool that helps you start an OS when its bootloader is broken. Detects and boots Linux, Windows, macOS, and more by scanning for kernels, GRUB2 configs, or core.img files, even if MBR/EFI entries are damaged. Supports LVM, RAID, loopboot ISOs, and encrypted volumes. Does not fix bootloaders but can boot into your OS so you can repair it manually.  
  **Tags:** `boot`, `liveusb`, `rescue`
* [**SystemRescue**](https://www.system-rescue.org) - Open-source Arch-based live USB system rescue toolkit for Linux and Windows. Includes tools like GParted, Parted, FSArchiver, ddrescue, TestDisk, and rsync. Supports ext4, btrfs, xfs, NTFS, vfat, and network filesystems like Samba and NFS. Ideal for partitioning, recovery, backups, and system repair on desktops and servers without needing installation.  
  **Tags:** `backup`, `liveusb`, `partition`, `rescue`, `ssh`

## 💿 Distributions

### General Purpose

* [**Arch Linux**](https://archlinux.org) - Open-source, minimalist, and rolling-release distribution aimed at experienced users who want full control. Ships bleeding-edge software with frequent updates. Embraces a “keep it simple” philosophy, offering only the essentials by default. Highly customizable and backed by one of the most comprehensive and well-maintained Linux wikis, supported by a strong, technical community that encourages hands-on learning.  
  **Tags:** `arch`, `desktop`, `pacman`, `rolling`
* [**Debian**](https://www.debian.org) - Open-source and known for rock-solid stability, making it the distribution with the most derivatives (e.g., Ubuntu, Mint). Ideal for servers and desktops. Ships stable releases every ~2 years with 5+ years of LTS support. Prioritizes reliability over cutting-edge updates, making it a low-maintenance, “install and forget” choice for consistent, long-term use in production as well as personal environments.  
  **Tags:** `apt`, `debian`, `desktop`, `server`
* [**Fedora KDE Plasma Desktop**](https://fedoraproject.org/kde) - Open-source, cutting-edge, backed by Red Hat, and acts as upstream for RHEL. New technologies like SELinux, systemd, Wayland, and PipeWire land in Fedora first. Shares many core developers with Red Hat. Ships every 6 months with a 13-month lifecycle. KDE Plasma offers a modern, highly customizable desktop unlike the locked-down feel of GNOME. A perfect daily driver combining fast updates, solid stability, and strong community support. Fedora also offers excellent hardware support, especially for older MacBook Pros and wireless adapters.  
  **Tags:** `desktop`, `kde`, `rhel`, `rpm`

### Lightweight

* [**Alpine Linux**](https://www.alpinelinux.org) - Open-source, security-oriented Linux distribution designed for simplicity and minimalism. Built on musl libc and BusyBox, with a minimal container image size under 8MB and ~130MB for disk installs. Uses the apk package manager and OpenRC init. Popular in containerized environments for its low resource usage, small attack surface, and rolling release model.  
  **Tags:** `alpine`, `apk`, `lightweight`, `rolling`
* [**DietPi**](https://dietpi.com) - Open-source, lightweight Debian-based distribution designed for minimal resource use on low-power devices and virtual machines. Features a base image under 500MB and RAM usage as low as 30MB. Ships with no desktop by default but provides a menu-driven setup tool to install only what’s needed. Built on Debian Stable, it inherits a ~2-year release cycle with 5 years of upstream LTS. Ideal for headless servers, embedded systems, and VMs.  
  **Tags:** `apt`, `debian`, `lightweight`, `server`

### Enterprise

* [**AlmaLinux**](https://almalinux.org) - Open-source, enterprise-grade and binary-compatible with Red Hat Enterprise Linux (RHEL). Maintained by the AlmaLinux OS Foundation, a community-driven non-profit. Offers long-term support with each release maintained for 10 years. A stable, free alternative to RHEL for production environments, ideal for businesses, hosting, and infrastructure.  
  **Tags:** `rhel`, `rpm`, `server`
* [**Red Hat Enterprise Linux (RHEL)**](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) - Open-source at its core, though official binaries require a subscription. RHEL is the grandfather of enterprise Linux and the gold standard for production systems. One of the pioneers in the Linux world, Red Hat is a major upstream contributor to the Linux kernel, GNOME, systemd, Podman, Ansible, Cockpit, OpenShift, and more. Offers rock-solid stability and a 10-year support lifecycle. With a free developer account, you can run up to 16 RHEL instances. Lesser known, it also includes a Workstation edition.  
  **Tags:** `desktop`, `rhel`, `rpm`, `server`
* [**Rocky Linux**](https://rockylinux.org) - Open-source, enterprise-grade, and binary-compatible with Red Hat Enterprise Linux (RHEL). Led by original CentOS co-founder Gregory Kurtzer and maintained by the Rocky Enterprise Software Foundation (RESF). Each release is supported for 10 years, aligning with RHEL. A stable, free alternative to RHEL for production environments, ideal for businesses, hosting, and infrastructure.  
  **Tags:** `rhel`, `rpm`, `server`
* [**Ubuntu Server LTS**](https://ubuntu.com/server) - Open-source and based on Debian, Ubuntu LTS (Long-Term Support) provides 5 years of free security and maintenance updates, extended to 10 years with Ubuntu Pro. Prioritizes ease of use, broad hardware compatibility, and a vast package ecosystem. Widely adopted for servers, cloud deployments, and desktop environments across both enterprise and personal use.  
  **Tags:** `apt`, `debian`, `server`

### Security-focused

* [**Kali Linux**](https://www.kali.org) - Open-source Debian-based penetration testing distribution maintained by Offensive Security. Includes a comprehensive suite of preinstalled tools for vulnerability assessment, forensics, reverse engineering, wireless auditing, and cryptography. Available as a live system, installable on bare metal, in containers (Docker, LXD), cloud, WSL, or ARM devices. Offers undercover mode, package customization, and Win-KeX for full desktop access under WSL.  
  **Tags:** `apt`, `debian`, `desktop`, `pentest`, `privacy`, `security`
* [**ParrotOS Security Edition**](https://parrotsec.org/download) - Open-source Debian-based penetration testing distribution focused on security, privacy, and forensics. Ships with a full suite of preinstalled tools for vulnerability assessment, exploitation, reverse engineering, cryptography, and digital forensics. Can be used as a live system, WSL, deployed in Docker, or installed by converting an existing Debian system.  
  **Tags:** `apt`, `debian`, `desktop`, `pentest`, `privacy`, `security`

### Appliance OS

* [**PfSense**](https://www.pfsense.org) - Open-source firewall, router, and VPN platform based on FreeBSD, developed by Netgate. pfSense is widely deployed in home labs, enterprises, and cloud environments. It offers advanced firewall rules, routing features, traffic shaping, multi-WAN support, and built-in VPN protocols like OpenVPN, IPsec, and WireGuard. A fully open-source Community Edition (CE) is maintained alongside the commercial Plus edition.  
  **Tags:** `bsd`, `firewall`, `freebsd`, `networking`, `pkg`, `vpn`
* [**TrueNAS CORE**](https://www.truenas.com/truenas-core) - Open-source NAS and storage platform based on FreeBSD and built around OpenZFS. Designed for home and SMB use, it offers advanced RAID management, snapshots, replication, and encrypted remote backups. Includes a powerful web UI, plugin support (Nextcloud, Plex, Syncthing), advanced SMB/NFS/iSCSI sharing, and virtualization via bhyve. Known for ZFS data integrity, reliability, and hardware flexibility.  
  **Tags:** `bsd`, `freebsd`, `media`, `nas`, `networking`, `pkg`, `storage`, `streaming`, `virtualization`, `vm`
* [**TrueNAS SCALE**](https://www.truenas.com/truenas-scale) - Open-source NAS and storage platform based on Debian Linux and built around OpenZFS. Tailored for home and SMB environments, it supports advanced RAID configurations, snapshots, replication, and encrypted remote backups. Offers a modern web UI, plugin support (Nextcloud, Plex, Syncthing), SMB/NFS/iSCSI services, virtual machines via KVM, and container orchestration through K3s (lightweight Kubernetes).  
  **Tags:** `apt`, `containers`, `debian`, `kubernetes`, `kvm`, `media`, `nas`, `networking`, `orchestration`, `storage`, `streaming`, `virtualization`, `vm`

### Unix-like

* [**FreeBSD**](https://www.freebsd.org) - Open-source, Unix-like operating system descended from BSD UNIX at UC Berkeley. Offers a complete OS (kernel + userland), unlike Linux, which combines a kernel with external components. Known for its advanced networking, storage, security, and performance features. Extremely stable and popular in production, but aimed at experienced users and requires more manual configuration than most Linux distributions.  
  **Tags:** `bsd`, `freebsd`, `pkg`, `server`
