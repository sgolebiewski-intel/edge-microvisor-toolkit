// Copyright (c) 2024, Intel Corporation.
// Licensed under the MIT License.

package ukiUtils

import (
	"fmt"
	"os"
	"path/filepath"
	"strings"

	"github.com/microsoft/azurelinux/toolkit/tools/imagegen/installutils"
	"github.com/microsoft/azurelinux/toolkit/tools/internal/file"
	"github.com/microsoft/azurelinux/toolkit/tools/internal/logger"
	"github.com/microsoft/azurelinux/toolkit/tools/internal/safechroot"
	"github.com/microsoft/azurelinux/toolkit/tools/internal/shell"
)

const (
	// Temporary local file to form boot command parameters for systemd-boot bootloader
	tmpBootParmsCfgFile = "/tmp/baseCmdline.cfg"
)

func InstallUnifiedKernelImage(installChroot *safechroot.Chroot) (err error) {

	err = installChroot.UnsafeRun(func() (err error) {
		const (
			initrdPrefix = "/boot/initramfs-"
			initrdSuffix = ".img"
			linuxPrefix  = "/boot/vmlinuz-"
			ukiImagePath = "/boot/linux.efi"
		)

		//Get initramfs
		initrdPattern := fmt.Sprintf("%v*%v", initrdPrefix, initrdSuffix)
		initrdImageSlice, err := filepath.Glob(initrdPattern)
		if err != nil {
			logger.Log.Warnf("Unable to get initrd image: %v", err)
			return
		}

		// Assume only one initrd image present
		if len(initrdImageSlice) != 1 {
			logger.Log.Warn("Unable to find one initrd image")
			logger.Log.Warnf("Initrd images found: %v", initrdImageSlice)
			err = fmt.Errorf("unable to find one intird image: %v", initrdImageSlice)
			return
		}

		initrdImage := initrdImageSlice[0]

		// Get the kernel version
		kernel := strings.TrimPrefix(initrdImage, initrdPrefix)
		kernel = strings.TrimSuffix(kernel, initrdSuffix)

		//Get vmlinuz
		linuxPattern := fmt.Sprintf("%v%v", linuxPrefix, "*")
		linuxImageSlice, err := filepath.Glob(linuxPattern)
		if err != nil {
			logger.Log.Warnf("Unable to get vmlinuz image: %v", err)
			return
		}

		// Assume only one vmlinuz image present
		if len(linuxImageSlice) != 1 {
			logger.Log.Warn("Unable to find one vmlinuz image")
			logger.Log.Warnf("vmlinuz images found: %v", linuxImageSlice)
			err = fmt.Errorf("unable to find one vmlinuz image: %v", linuxImageSlice)
			return
		}

		linuxImage := linuxImageSlice[0]

		_, err = os.Stat(tmpBootParmsCfgFile)
		if err != nil {
			if os.IsNotExist(err) {
				err = fmt.Errorf("file tmpBootParmsCfgFile does not exists !")
			}
			return
		}

		cmdline, err := file.Read(tmpBootParmsCfgFile)
		if err != nil {
			logger.Log.Warnf("Failed to read cmdline from %s file : %v", tmpBootParmsCfgFile, err)
			return
		}
		logger.Log.Infof("cmdline: %s", cmdline)

		installutils.ReportAction("Building uki image ..")

		// Generate uki image via Ukify
		ukifyArgs := []string{
			"build",
			"--uname", kernel,
			"--linux", linuxImage,
			"--initrd", initrdImage,
			"--cmdline", cmdline,
			"--output", ukiImagePath,
		}
		_, stderr, err := shell.Execute("ukify", ukifyArgs...)

		if err != nil {
			logger.Log.Warnf("Unable to execute ukify: %v", stderr)
			return
		}

		return
	})

	return
}
