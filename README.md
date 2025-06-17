# Infinite Monkey Sixpace60

- Based on 60% HHKB like layout
- Six space keys
- Arrow keys
- No stabilizers
- Supports [QMK](https://qmk.fm/), [VIA](https://caniusevia.com/) and [VIAL](https://get.vial.today/)

# Build for QMK

```shell
RUNTIME="docker" SKIP_FLASHING_SUPPORT=1 util/docker_cmd.sh make infinitemonkey/sixpace60:default
```

# Build for via

```shell
RUNTIME="docker" SKIP_FLASHING_SUPPORT=1 util/docker_cmd.sh make infinitemonkey/sixpace60:via
```

# Build for vial

```shell
RUNTIME="docker" SKIP_FLASHING_SUPPORT=1 util/docker_cmd.sh make infinitemonkey/sixpace60:vial
```

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

# Author

- [Susumu OTA](https://github.com/susumuota)
