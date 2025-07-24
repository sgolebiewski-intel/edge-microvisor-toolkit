# Build Edge Microvisor Toolkit and Deploy on Edge Nodes

This guide will walk you through the entire process of Edge Microvisor Toolkit deployment.
You will learn how to build the default version of the toolkit, install it on a single
or multiple edge node clusters, and deploy AI solutions.
This guide uses the
[Smart Parking application](https://github.com/open-edge-platform/edge-ai-suites/tree/main/metro-ai-suite/smart-parking)
with AI-driven video analytics to optimize parking management.

1. Build the microvisor.
2. Create a bootable USB installer.
3. Install the toolkit on an edge device.
4. Deploy AI solution.

## Build the microvisor

1. Clone the stable branch of edge-microvisor-toolkit repository:

   ```bash
   git clone https://github.com/open-edge-platform/edge-microvisor-toolkit --branch=3.0.20250718
   ```

2. Clone the edge-microvisor-toolkit-standalone-node repository:

   ```bash
   git clone https://github.com/open-edge-platform/edge-microvisor-toolkit-standalone-node
   ```

3. Navigate to the `edge-microvisor-toolkit` directory:

   ```bash
   cd edge-microvisor-toolkit
   ```

4. Install prerequisites:

   Requirements for building the toolchain were validated on an Ubuntu 22.04 host.

   ```bash
   # Install required dependencies.
   sudo ./toolkit/docs/building/prerequisites-ubuntu.sh

   # Also supported is:
   #    make -C toolkit install-prereqs

   # Fix go 1.21 link
   sudo ln -vsf /usr/lib/go-1.21/bin/go /usr/bin/go
   sudo ln -vsf /usr/lib/go-1.21/bin/gofmt /usr/bin/gofmt

   # Install and configure Docker.
   curl -fsSL https://get.docker.com -o get-docker.sh
   sudo sh get-docker.sh
   sudo usermod -aG docker $USER
   ```

   **You will need to log out and log back in** for user changes to take effect.

5. Navigate to the `toolkit` subdirectory.

   ```bash
   cd ./toolkit
   ```

6. Build the toolchain.

   ```bash
   sudo make toolchain REBUILD_TOOLS=y
   ```

7. Build a selected version of the Edge Microvisor Toolkit:

   All available image configurations are stored in JSON files, located in the `imageconfigs` folder.
   For example, to build a RAW image without real-time extensions, use `edge-image.json` and run
   the following command:

   ```bash
   sudo make image -j8 REBUILD_TOOLS=y REBUILD_PACKAGES=n CONFIG_FILE=./imageconfigs/edge-image.json
   ```

   For more information about specific building parameters, refer to the [article.](https://github.com/open-edge-platform/edge-microvisor-toolkit/blob/3.0/toolkit/docs/building/building.md#local-build-variables).

## Create a bootable USB installer

1. Navigate to the `edge-microvisor-toolkit-standalone-node` directory:

   ```bash
   cd ../../edge-microvisor-toolkit-standalone-node
   ```

2. Create the installer:

   To create the installation tar file with all required files for preparing a bootable USB
   drive, run the following command

   ```bash
   sudo make build
   ```

 > **Note:** This command will generate the `standalone-installation-files.tar.gz` file.
   The file will be located in the `$(pwd)/installation-scripts/out` directory.

3. Prepare the bootable USB drive:

   > **Note:**
   >
   > - Ensure **the correct USB drive is selected** to avoid data loss.
   > - **Replace `/dev/sdX`** with the actual device name of your USB drive.

   - Insert the USB drive into the Developer's System and identify the USB disk:

      ```bash
      lsblk -o NAME,MAJ:MIN,RM,SIZE,RO,FSTYPE,MOUNTPOINT,MODEL
      ```

      > **Note:** Ensure the correct USB drive is selected to avoid data loss.

   - Use the wipefs command to remove any existing filesystem signatures from the USB drive.
     This ensures a clean slate for formatting

      ```bash
      sudo wipefs --all --force /dev/sdX
      ```

   - Format the USB drive with a FAT32 filesystem using the mkfs.vfat command.

      ```bash
      sudo mkfs.vfat /dev/sdX
      ```

   - Unmount the USB drive to ensure the creation of bootable USB.

     - Check what is currently mounted:

       ```bash
       df -hT
       ```

     - Unmount the drive:

       ```bash
       sudo umount /dev/sdX
       ```

   - Copy standalone installation tar file to developer system to prepare the Bootable USB

     Extract the contents of standalone-installation-files.tar.gz

     ```bash
      tar -xzf standalone-installation-files.tar.gz
     ```

   - Extracted files will include

     ```text
     bootable-usb-prepare.sh
     write-image-to-usb.sh
     config-file
     usb-bootable-files.tar.gz
     edgenode-logs-collection.sh
     standalone-vm-setup.sh
     download_images.sh
     user-apps
     ```

   - Download the kubernetes artifacts (container images and manifest files). This step is done by
     executing the ./download_images.sh script. If you are using EMT image with desktop virtualization
     features then use `DV` parameter. For default EMT image which is a non-Real Time kernel use `NON-RT`
     parameter.

      ```bash
      sudo ./download_images.sh DV

      or

      sudo ./download_images.sh NON-RT
      ```

   > **Note:** By default the script will only pull basic kubernetes artifacts to create a single node cluster.

   - Update the `config-file` with your deployment-specific settings.
   This configuration file is used to provision the edge node during
   its initial boot and should include the following parameters:

     - **Proxy settings:** Specify if the edge node requires a proxy to access external networks.
     - **SSH key:** Provide the public SSH key (typically your
     `id_rsa.pub`) from your Linux development system to enable passwordless SSH access to the edge node.
     - **User credentials:** Define the username and password for the primary user account on the edge node.
     - **Cloud-init customization:** Optionally, include user-defined `cloud-init` configurations for advanced setup requirements.
       - For the default EMT Non-Realtime image, a basic
       Kubernetes installation will be performed automatically.
       - For deployments requiring Desktop Virtualization features,
         refer to the [desktop-virtualization-image-guide](desktop-virtualization-image-guide.md) in the
         `user-guide` directory. This document provides reference `cloud-init` configurations that can be
         tailored to your specific deployment needs.
     - **Hugepages configuration:** Set hugepages parameters if your workloads require them.

   - Run the preparation script to create the bootable USB

      ```bash
      sudo ./bootable-usb-prepare.sh </dev/sdX> usb-bootable-files.tar.gz config-file
      ```

   - Required Inputs for the Script:

       ```bash
        - usb: A valid USB device name (e.g., `/dev/sdc`)
        - usb-bootable-files.tar.gz: The tar file containing bootable files
        - config-file: Configuration file with deployment-specific settings
       ```

   > **Note:** Providing proxy settings is optional if the edge node does not require them to access internet services.
   > **Additional Customization:** If you want to add specific configurations,
   helm charts, or packages to your deployment, you can refer to the
   [pre-loading-user-apps guide](pre-loading-user-apps.md) for detailed
   instructions on customizing your EMT image.

4. Select your Edge Microvisor Toolkit image:

   The Edge Microvisor Toolkit Standalone Node supports different EMT images to
   meet specific edge deployment needs. You can choose from:

   - **Edge Microvisor Toolkit Non Realtime image** (default)
   - **Edge Microvisor Toolkit Desktop Virtualization image**
   - **Customized immutable Edge Microvisor Toolkit created using "Edge Microvisor Toolkit Developer Node"**

   ##### Option 1: Using the Default Non Realtime Image

   If you opt for the default Non-Realtime image, which is suggested for the majority of Edge AI applications,
   there's no need for further image setup. The usb-bootable-files.tar.gz installer comes with this image pre-included.

   ##### Option 2: Using Desktop Virtualization or Custom created image

   If you need Desktop Virtualization features, follow these steps to replace the default image:

   1. Desktop Virtualization image: Download from the no Auth file server registry

   > **Note:** Custom created image can be copied locally from your development system to the 5th
   > partition as shown in step 2 below.

   1. Replace the default EMT image with the EMT DV or custom created image. The
   default EMT image is located at the 5th partition of the
   bootable USB drive created in the previous step.
   Follow these steps to replace the image:

     ```bash
     # Create a test directory for mounting
     sudo mkdir -p /mnt/test

     # Mount the 5th partition of the USB drive
     sudo mount /dev/sda5 /mnt/test

     # Navigate to the mounted directory
     cd /mnt/test

     # Remove the older image (backup first if needed)
     sudo rm -f <old-image-file>

     # For Desktop Virtualization image: Download from registry
     sudo wget <your-dv-image-url> -O <new-image-file>

     # For Custom created image: Copy from local directory to 5th partition
     sudo cp /path/to/your/custom-image.raw ./

     # Unmount the partition
     cd /
     sudo umount /mnt/test
     ```

   The DV image is available here [Download DV Image](https://files-rs.edgeorchestration.intel.com/files-edge-orch/repository/microvisor/dv/   edge-readonly-dv-3.0.20250717.0840.raw.gz)

     > **Important:** These steps are manually executed by the user to put the desired image
     > into the 5th partition before standalone deployment mentioned in
     > [Step 2: Deploy Edge Node](#step-2-deploy-edge-node)

### 3. Install the toolkit on an edge device

- Unplug the attached bootable USB from developer system

- Plug the created bootable USB pen drive into the standalone node

- Set the BIOS boot manager to boot from the USB pen drive

- Reboot the Standalone Node
  This will start Microvisor installations.

- Automatic Reboot
  The standalone edge node will automatically reboot into Microvisor.

- First Boot Configuration
  During the first boot, cloud-init will install the k3s Kubernetes cluster.

####Login to the Edge Node After Installation Completes

Refer to the edge node console output for instructions to verify the kubernetes cluster creation.

Use the Linux login credentials which was provided while preparing the bootable USB drive.

**Note:** If you want to run kubectl commands from the edge node you can use the provided alias ``k``
which is defined in the .bashrc of the user defined in your config.

```bash
k get pods -A
```

#### Set up tools on Developer's System

Install and configure [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) and
[helm](https://helm.sh/docs/intro/install/) tools on the Developer's system.

> **Note:** The commands are executed from `Linux` environment, but the same can be achieved from any
environment supporting `kubectl` and `helm` by using equivalent commands.

1. Install `kubectl`:

   ```bash
   sudo apt-get update
   sudo apt-get install -y apt-transport-https ca-certificates curl gnupg
   curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.32/deb/Release.key | \
     sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   sudo chmod 644 /etc/apt/keyrings/kubernetes-apt-keyring.gpg
   echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] \
     https://pkgs.k8s.io/core:/stable:/v1.32/deb/ /' | \
     sudo tee /etc/apt/sources.list.d/kubernetes.list
   sudo chmod 644 /etc/apt/sources.list.d/kubernetes.list
   sudo apt-get update
   sudo apt-get install -y kubectl
   ```

2. Copy the kubeconfig file from the Edge Node:

   ```bash
   mkdir ~/.kube
   export EN_IP=<EN_IP>
   scp user@${EN_IP}:/etc/rancher/k3s/k3s.yaml ~/.kube/config
   ```

3. Update the Edge Node IP in the kubeconfig file and export the path as KUBECONFIG:

   ```bash
   sed -i "s/127\.0\.0\.1/${EN_IP}/g" ~/.kube/config
   export KUBECONFIG=~/.kube/config
   ```

4. Test the connection:

   ```bash
   kubectl get pods -A
   ```

5. Install `helm`:

   ```bash
   curl -fsSL -o get_helm.sh https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3
   chmod 700 get_helm.sh
   ./get_helm.sh
   ```

## 4 Deploy AI solution
