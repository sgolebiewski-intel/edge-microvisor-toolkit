# Get Started

Edge Microvisor Toolkit is a lightweight, container-first Linux distribution,
optimized for Intel® architecture. It provides a secure and high-performing
environment for deploying edge workloads across multiple deployment models.

This section provides an overview of both the operating system and build
pipelines. Once you have decided on the usage scenarios presented below, you can
move on to:

- [Build a new Edge Microvisor Toolkit Image.](./get-started/building-howto.md)
- [Install Edge Microvisor Toolkit from existing image.](./get-started/installation-howto.md)

## Usage Scenarios

This section outlines the key usage models intended for the initial release of
Edge Microvisor Toolkit.

It can be used for standalone edge node deployments, or with Edge Manageability
Framework - a complete integrated system providing full lifecycle management for
your edge devices, including remote deployment and management of Kubernetes
applications.

### Edge Microvisor Toolkit Developer

To create a custom developer build of Edge Microvisor Toolkit, follow these steps:

- [Download the mutable host ISO image](https://files-rs.edgeorchestration.intel.com/files-edge-orch/microvisor/iso/EdgeMicrovisorToolkit-3.0.iso) from
  Intel® Edge Software Catalog.
- Install the mutable host via ISO image that includes only essential pre-installed packages,
  providing a ready-to-use base environment.
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

### Edge Microvisor Toolkit Standalone

[Go to Intel® Edge Software Catalog](https://edgesoftwarecatalog.intel.com/package/edge_microvisor_toolkit_standalone_node) and download a standalone Edge Node ISO installer.

The standalone edge node uses the standard immutable build and provides an ISO
image that can be flashed to a USB device and installed on edge nodes. It
installs the microvisor and Kubernetes to the edge node with the essential
functionality to run a single node cluster. The edge node will serve as both the
control and worker node. Additional worker nodes can be added to the cluster
through Kubernetes.

Future releases will enable standalone edge nodes to join an existing Edge
Management Framework backend, deployed on-prem or in the cloud to support scale
out and management of larger infrastructures. The Standalone Edge Node enables
you to quickly get an edge node up and running without deploying backend
services, ready to deploy Kubernetes applicationsthrough `kubectl`, `helm`, or
Kubernetes web dashboard.

:::{admonition} The standalone edge node does not support the real-time version currently.
:class: note

The immutable OS image does not include the Kubernetes software and
extensions. After the OS is installed, they are deployed on a writable section of the
filesystem. Image and orchestration system updates are currently not natively enabled.
:::

### Edge Microvisor Toolkit with Edge Manageability Framework

Edge Microvisor Toolkit supports deployment of its two versions with Edge
Manageability Framework:

- Microvisor Immutable Image
- Microvisor Immutable Image with Real Time

For details on deploying Microvisor with Edge Manageability Framework, refer to
the [Edge Manageability Framework deployment guide](../user-guide/emt-deployment-edge-orchestrator.md).

## Image Support

The toolkit comes pre-configured to produce different images, the table below
outlines the key differences between those.

|  Feature         | Edge Microvisor Toolkit Developer | Edge Microvisor Toolkit Standalone & Orchestrated                                   |
| -----------------| -------------------- | ------------------------------------------------- |
| Capabilities | <ul><li>Easy to install, bootable ISO image with precompiled packages for developer evaluation.</li> <li> Includes installable rpms with TDNF for extending baseline functionality.</li> <li>Complete with toolkit to build image with an opt-in data integrity and security features.</li></ul> | <ul><li>Designed for Open Edge Platforms and can be used to onboard and provision edge nodes at scale.</li><li>Can be used independently on bare-metal and as guest OS.</li><li>Fast atomic updates & rollback support with small image footprint and short boot time.|
| Image Type       | Mutable ISO          | Immutable RAW + VHD                               |
| Update Mechanism | RPM package updates with TDNF | Image based A/B updates + Rollback       |
| Linux Kernel     | Intel® Kernel 6.12   | Intel® Kernel 6.12                                |
| Real time        | No                   | Two images provided one RT kernel and one without |
| OS Bootloader    | GRUB                 | systemd-boot                                      |
| Secure Boot      | Available for opt-in | Enabled                                           |
| Full Disc Encryption | Available for opt-in | Enabled                                       |
| dm-verity        | Available for opt-in | Enabled                                           |
| SELinux          | Permissive           | Permissive                                        |

## Next Steps

- [System Requirements](./introduction)
- [Production Deployment with Edge Manageability Framework](./emt-deployment-edge-orchestrator.md)

:::{toctree}
./get-started/emt-building-howto.md
./get-started/emt-installation-howto.md
./get-started/emt-sb-howto.md
:::
