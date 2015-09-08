#sbs-git:slp/pkgs/m/mfc-firmware mfc-firmware 0.0.1 f1be446e0f392b26e9caa173af0ed9c3ee1827bd
#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
#

Name:       mfc-firmware
Summary:    Binary mfc firmware common for all samsung targets
Version:    0.0.9
Release:    1
Group:      TO_BE/FILLED_IN
License:    Proprietary
Source0:    %{name}-%{version}.tar.gz
ExclusiveArch: %arm

%if ("%{tizen_target_name}" == "B3")
Excludearch: %arm
%endif

%define debug_package %{nil}

%description
binary mfc firmware common for all samsung targets

%package c110
Summary:    binary mfc firmware specific to samsung c110
Group:      TO_BE/FILLED

%description c110
binary mfc firmware specific to samsung c110.

%package e4412
Summary:    binary mfc firmware specific to e4412
Group:      TO_BE/FILLED

%description e4412
binary mfc firmware specific to e4412.

%package e5410
Summary:    binary mfc firmware specific to e5410
Group:      TO_BE/FILLED

%description e5410
binary mfc firmware specific to e5410.

%package msm8x30
Summary:    binary mfc firmware specific to msm8x30
Group:      TO_BE/FILLED

%description msm8x30
binary mfc firmware specific to msm8x30.

%package e3250
Summary:    binary mfc firmware specific to e3250
Group:      TO_BE/FILLED

%description e3250
binary mfc firmware specific to e3250.

%prep
%setup -q

%build

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/lib/firmware

cp -af mfc-firmware-c110/* %{buildroot}/lib/firmware
cp -af mfc-firmware-e4412/mfc_fw.bin %{buildroot}/lib/firmware/mfc_fw_e4412.bin
cp -af mfc-firmware-e4412/s5p-mfc.fw %{buildroot}/lib/firmware/s5p-mfc.fw
cp -af mfc-firmware-e5410/mfc_fw.bin %{buildroot}/lib/firmware/mfc_fw_e5410.bin
cp -af mfc-firmware-msm8x30/* %{buildroot}/lib/firmware
cp -af mfc-firmware-e3250/mfc_fw_v7.8.bin %{buildroot}/lib/firmware/mfc_fw.bin


%files c110
%manifest mfc-firmware-c110.manifest
%defattr(-,root,root,-)
/lib/firmware/s3c_mfc_fw.bin
/lib/firmware/Readme

%files e4412
%manifest mfc-firmware-e4412.manifest
%defattr(-,root,root,-)
/lib/firmware/mfc_fw_e4412.bin
/lib/firmware/s5p-mfc.fw

%files e5410
%manifest mfc-firmware-e5410.manifest
%defattr(-,root,root,-)
/lib/firmware/mfc_fw_e5410.bin

%files msm8x30
%manifest mfc-firmware-msm8x30.manifest
%defattr(-,root,root,-)
/lib/firmware/vidc_1080p.fw

%files e3250
%manifest mfc-firmware-e3250.manifest
%defattr(-,root,root,-)
/lib/firmware/mfc_fw.bin

%post e4412
mv /lib/firmware/mfc_fw_e4412.bin /lib/firmware/mfc_fw.bin

%post e5410
mv /lib/firmware/mfc_fw_e5410.bin /lib/firmware/mfc_fw.bin

%preun e4412
mv /lib/firmware/mfc_fw.bin /lib/firmware/mfc_fw_e4412.bin

%preun e5410
mv /lib/firmware/mfc_fw.bin /lib/firmware/mfc_fw_e5410.bin
