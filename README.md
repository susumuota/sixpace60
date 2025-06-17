# Infinite Monkey Sixpace60

<a href="https://github.com/susumuota/sixpace60/blob/main/images/sixpace60_above.png"><img src="https://raw.githubusercontent.com/susumuota/sixpace60/refs/heads/main/images/sixpace60_above.png" alt="Infinite Monkey Sixpace60" width="800" /></a>

<a href="https://github.com/susumuota/sixpace60/blob/main/images/sixpace60_side.png"><img src="https://raw.githubusercontent.com/susumuota/sixpace60/refs/heads/main/images/sixpace60_side.png" alt="Infinite Monkey Sixpace60" width="400" /></a>

<a href="https://github.com/susumuota/sixpace60/blob/main/images/sixpace60_assembly.png"><img src="https://raw.githubusercontent.com/susumuota/sixpace60/refs/heads/main/images/sixpace60_assembly.png" alt="Infinite Monkey Sixpace60" width="800" /></a>

<a href="https://github.com/susumuota/sixpace60/blob/main/images/sixpace60_via.png"><img src="https://raw.githubusercontent.com/susumuota/sixpace60/refs/heads/main/images/sixpace60_via.png" alt="Infinite Monkey Sixpace60" width="800" /></a>

- Based on 60% layout
- Six space keys
- Arrow keys
- No stabilizers
- Supports [VIA](https://caniusevia.com/), [Remap](https://remap-keys.app/) and [VIAL](https://get.vial.today/)


## Installation

- Install [QMK Toolbox](https://qmk.fm/toolbox) to flash the firmware
- Open the QMK Toolbox
- Connect your keyboard
- Press `Open` and select the firmware file [firmware/infinitemonkey_sixpace60_via.hex](firmware/infinitemonkey_sixpace60_via.hex) for VIA or [firmware/infinitemonkey_sixpace60_vial.hex](firmware/infinitemonkey_sixpace60_vial.hex) for VIAL
- Press the reset button on your keyboard **twice quickly** to put it into bootloader mode
- Press `Flash` in the QMK Toolbox

## Setting Up with VIA

- Go to [VIA](https://www.usevia.app/)
- Press `SETTINGS` and turn on `Show Design tab`
- Press `DESIGN`, press `Load`, and select [qmk/keyboards/infinitemonkey/sixpace60/via.json](qmk/keyboards/infinitemonkey/sixpace60/via.json)
- Press `CONFIGURE` press `Authorize device +` and select `Sixpace60`

## Setting Up with VIAL

- Go to [Vial Web](https://vial.rocks/)
- Press `Start Vial`
- Select `Sixpace60`

## Building the Firmware

Install [Docker](https://www.docker.com/get-started) to build the firmware.

### Build for VIA and Remap

```shell
git clone https://github.com/qmk/qmk_firmware.git
git clone https://github.com/susumuota/sixpace60.git
cp -rp sixpace60/qmk/keyboards/infinitemonkey qmk_firmware/keyboards
cd qmk_firmware
RUNTIME="docker" SKIP_FLASHING_SUPPORT=1 util/docker_cmd.sh make infinitemonkey/sixpace60:via
```

### Build for VIAL

```shell
git clone https://github.com/vial-kb/vial-qmk.git
git clone https://github.com/susumuota/sixpace60.git
cp -rp sixpace60/qmk/keyboards/infinitemonkey vial-qmk/keyboards
cd vial-qmk
RUNTIME="docker" SKIP_FLASHING_SUPPORT=1 util/docker_cmd.sh make infinitemonkey/sixpace60:vial
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

- [Susumu OTA](https://github.com/susumuota)
