# Photons RPM Packages

[Photons is an asynchronous Python3.6+ framework](https://photons.delfick.com)
for interacting with [LIFX](https://www.lifx.com.au) devices.

[Packages are avaialble from COPR](https://copr.fedorainfracloud.org/coprs/djelibeybi/photons/)
for Fedora Rawhide, Fedora 33 and EL8-derivatives, e.g. RHEL8, CentOS Stream
and Oracle Linux 8 for both `x86_64` and `aarch64` architectures.

## Installation

1. [Enable the `djelibeybi/photons` COPR repository](https://docs.pagure.org/copr.copr/how_to_enable_repo.html#how-to-enable-repo)
1. Run `dnf install python3-lifx-photons-core` to install the core framework and `lifx` command-line utility.
1. (Optional) run `dnf install python3-lifx-photons-arranger` to install the LIFX Tile arranger tool.
1. (Optional) run `dnf install python3-lifx-photons-interactor` to install Photons Interactor, a
   Photons powered server that provides a JSON API for interacting with LIFX devices on the local network.

## Configuration

To allow discovery of LIFX devices, run:

```shell
# firewall-cmd --permanent --add-service=lifx-discovery
# firewall-cmd --reload
```

To allow incoming connections to Photons Interactor (if installed), run:

```shell
# firewall-cmd --permanent --add-service=photons-interactor
# firewall-cmd --reload
```

To enable and start Photons Interactor after installation, run:

```shell
# systemctl enable --now photons-interactor
```

## License

Each RPM `.spec` file is released under the same license as the upstream package:

* [Apache 2.0 Licence][Apache-2.0]
  * [`python-aiohttp.spec`](python-aiohttp/python-aiohttp.spec)
  * [`python-tornado.spec`](python-tornado/python-tornado.spec)

* [ISC License][ISC]
  * [`python-kdtree.spec`](python-kdtree/python-kdtree.spec)

* [MIT License][MIT]
  * [`python-delfick-project.spec`](python-delfick-project/python-delfick-project.spec)
  * [`python-lifx-photons-arranger.spec`](python-lifx-photons-arranger/python-lifx-photons-arranger.spec)
  * [`python-lifx-photons-core.spec`](python-lifx-photons-core/python-lifx-photons-core.spec)
  * [`python-lifx-photons-interactor.spec`](python-lifx-photons-interactor/python-lifx-photons-interactor.spec)
  * [`python-lru-dict.spec`](python-lru-dict/python-lru-dict.spec)
  * [`python-ruamel-yaml.spec`](python-ruamel-yaml/python-ruamel-yaml.spec)
  * [`python-whirlwind-web.spec`](python-whirlwind-web/python-whirlwind-web.spec)

* [Python Software Foundation License][PSFL]
  * [`python-bitarray.spec`](python-bitarray/python-bitarray.spec)

* [Unlicense][UNLICENSE]
  * [`python-rainbow_logging_handler.spec`](python-rainbow_logging_handler/python-rainbow_logging_handler.spec)

[Apache-2.0]: https://choosealicense.com/licenses/apache-2.0/
[ISC]: https://choosealicense.com/licenses/isc/
[MIT]: https://choosealicense.com/licenses/mit/
[PSFL]: https://github.com/ilanschnell/bitarray/blob/master/LICENSE
[UNLICENSE]: https://choosealicense.com/licenses/unlicense/
