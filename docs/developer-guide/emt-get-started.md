# Get Started

Edge Microvisor Toolkit is a lightweight, container-first Linux distribution,
optimized for Intel® architecture. It provides a secure and high-performing
environment for deploying edge workloads across multiple deployment models.

## OS Versions

The microvisor OS considers two major usage scenarios for standalone edge node deployments,
or integration with Edge Manageability Framework, and comes pre-configured to produce
different images, as shown in the table below:

|  Feature         | Edge Microvisor Toolkit Developer Node | Edge Microvisor Toolkit Standalone Node & Orchestrated                                   |
| -----------------| -------------------- | ------------------------------------------------- |
| Capabilities | <ul><li>Easy to install, bootable ISO image with precompiled packages for developer evaluation.</li> <li> Includes installable rpms with TDNF for extending baseline functionality.</li> <li>Complete with toolkit to build image with an opt-in data integrity and security features.</li></ul> | <ul><li>Designed for Open Edge Platforms and can be used to onboard and provision edge nodes at scale.</li><li>Can be used independently on bare-metal and as guest OS.</li><li>Fast atomic updates & rollback support with small image footprint and short boot time.|
| Image Type       | Mutable ISO          | Immutable RAW + VHD                               |
| Update Mechanism | RPM package updates with TDNF | Image based A/B updates + Rollback       |
| Linux Kernel     | Intel® Kernel 6.12   | Intel® Kernel 6.12                                |
| Real time        | Available for opt-in | Two images provided: one with RT kernel and one without |
| Add-on packages  | Available for opt-in: Docker + K3s | Built into image: Docker + K3s |
| OS Bootloader    | GRUB                 | systemd-boot                                      |
| Secure Boot      | Available for opt-in | Enabled                                           |
| Full Disc Encryption | Available for opt-in | Enabled                                       |
| dm-verity        | Available for opt-in | Enabled                                           |
| SELinux          | Permissive           | Permissive |



## Standalone Edge Node Deployments

## Edge Microvisor Toolkit Developer Node

To create a custom developer build of Edge Microvisor Toolkit, follow these steps:

- [Download the mutable host ISO image](https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/iso/EdgeMicrovisorToolkit-3.0.iso) from
  Intel® Edge Software Catalog.
- Install the mutable host via ISO image. Choose one of several installation types that
  provide ready-to-use base environments:
  - **Standard Kernel** - that includes only essential pre-installed packages,
  - **RT Kernel** - that offers enhanced real-time performance with
    [Preempt RT Linux Kernel 6.12](./emt-architecture-overview.md#preempt-rt-kernel),
  - **Standard Kernel + Docker + K3s** - that is fitted with additional features:
    - Docker 25.07 - for deploying applications in lightweight and standalone containers,
    - K3s - Lightweight Kubernetes 1.32.4, installed as an RPM package, for a simplified
      deployment on resource-constrained edge devices,
  - **RT Kernel + Docker + K3s** - that supports real-time workloads and offers small
    footprint deployment.
- Install additional RPM packages, using DNF to tailor the OS to your specific needs.
- Update installed RPMs regularly to stay up-to-date in the OS in terms of package updates,
  kernel updates, security vulnerability fixes and bug fixes.
- Use the OS toolkit and available packages to build a custom OS image, which enables you to:
  - Configure the system for specialized workloads or environments.
  - Experiment with simplified or enhanced configurations tailored for your specific workloads.
  - Explore - use built-in monitoring tools to track system performance, resource
    usage, and log data for deeper insights into operational behavior.

| Item              | Details                                         |
| ------------------| ----------------------------------------------- |
| Packages          | approximately ~400                              |
| Core system tools | bash, coreutils, util-linux, tar, gzip          |
| Networking        | curl, wget, iproute2, iptables, openssh         |
| Package Management | tdnf, rpm                                      |
| Development       | gcc, make, python3, perl, cmake, git            |
| Security          | openssl, gnupg, selinux, cryptsetup, tpm2-tools |
| Filesystem        | e2fsprogs, mount                                |
| Included in kernel | iGPU, dGPU (Intel® Arc&trade;), SR-IOV, WiFi, Ethernet, Bluetooth, GPIO, UART, I2C, CAN, USB, PCIe, PWM, SATA, NVMe, MMC/SD, TPM, Manageability Engine, Power Management, Watchdog, RAS |

The supported package repository offers additional `rpm` for tailoring the image
to specific needs of container runtime, virtualization, orchestration software,
monitoring tools, standard cloud-edge (CNCF) software, and more.

## Edge Microvisor Toolkit Standalone Node

[Go to the Edge Microvisor Toolkit Standalone Node repository](https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node).


### Deployment with Edge Manageability Framework

Two versions of Edge Microvisor Toolkit Standalone Node support deployment with Edge
Manageability Framework:

- Non-RT Immutable Image
- RT Immutable Image (with Real Time extensions)

For details on deploying Microvisor with Edge Manageability Framework, refer to
the [Edge Manageability Framework deployment guide](./emt-deployment-edge-orchestrator.md).





This section provides an overview of both the operating system and build
pipelines. Once you have decided on the usage scenarios presented below, you can
move on to:

- [Build a new Edge Microvisor Toolkit Image.](./get-started/emt-building-howto.md)
- [Install Edge Microvisor Toolkit from existing image.](./get-started/emt-installation-howto.md)



## Next Steps

- [System Requirements](./get-started/emt-system-requirements)
- [Production Deployment with Edge Manageability Framework](./emt-deployment-edge-orchestrator.md)

:::{toctree}
./get-started/emt-system-requirements.md
./get-started/emt-building-howto.md
./get-started/emt-installation-howto.md
./get-started/emt-sb-howto.md
:::
