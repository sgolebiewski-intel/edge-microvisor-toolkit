---
orphan: true
---
# Overview

Edge Microvisor Toolkit is an open-source, lightweight, and secure operating system optimized
for the Intel® architecture. It is designed to enhance edge computing workloads by providing
a container-first, immutable OS with a focus on security, efficiency, and streamlined management.

## Secure by Design
- A/B atomic updates prevent configuration drift, corruption and support automatic rollback.
- Read-only root filesystem enhances security and prevents unauthorized modifications.
- Integrated Secure Boot and TPM support for hardware-verified integrity.

## Optimized for Intel® Architecture
- Pre-tuned drivers and acceleration libraries for Intel® CPUs and GPUs.
- Enables Intel® silicon ahead of Operating System vendors (OSVs), unlocking features that may not be accepted upstream.

## Flexible and Modular Deployment
- Integrates with Edge Orchestrator for production deployments with seamless onboarding and provisioning.
- Supports bare metal, VM-based, and containerized deployments.
- Runs on Kubernetes*, Docker*, and OCI-compliant runtimes.

## Open Source and Extensible
- Fully open-source and royalty-free.
- Actively integrates OxM platform features and third-party vendor hardware.

# Usage Mode and Core Components
This release of the Edge Microvisor Toolkit supports one usage mode tailored for scalable and production-ready deployments.

## Production Deployment with Edge Orchestrator

- **Target Use Case:** A pre-configured, immutable OS for scalable, production-ready deployments with Edge Orchestrator.

- **Update Mechanism:** Atomic A/B system updates with rollback support.

- **Bootloader:** systemd-boot for streamlined boot security.

- **Kernel:** Intel® Linux* Kernel 6.6 with optimized security settings.

- **Filesystem:** Immutable filesystem for security and reliability.

- **Security Features:** Fully enforced security policies including secure boot, full disk encryption, and dm-verity.

# Supported Platforms

Edge Microvisor Toolkit has been validated on the following platforms:

- 12th Gen Intel® Core™ Processors
- 13th Gen Intel® Core™ Processors
- Intel® Core™ Ultra Processors (Series 1)
- 3rd Gen Intel® Xeon® Scalable Processors
- 4th Gen Intel® Xeon® Scalable Processors
- Intel® Atom® Processor X Series


# License Information

Edge Microvisor Toolkit is open source under the MIT License.
See the [licence](../../LICENSE) file for details.

# Next Steps
- [Production Deployment with Edge Orchestrator](./deployment-edge-orchestrator.md)
