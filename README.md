<img src="assets/logo.webp" width="100" alt="logo" style="margin:40px auto; display: block">

# MobReaper: Runtime Mobile Application Test Suite

[![Commits](https://img.shields.io/github/commit-activity/w/chichou/grapefruit?label=Commits)](https://github.com/cassio-santos-ptk/mobile-automated-workflow/commits/main/)
[![contributers](https://img.shields.io/github/contributors/chichou/grapefruit)](https://github.com/cassio-santos-ptk/mobile-automated-workflow/graphs/contributors)

![Screenshot](assets/screenshot.png)

## Get Started

## Dependencies

### Python
Grapefruit requires [Python](https://www.python.org/) to be installed.

### Genymotion
Setup genymotion on your device: https://www.genymotion.com/product-desktop/download/

At this moment, the key recommended device definitions are:

- Android Version: 11.0
- Architecture: arm64

### Rooted Device

It is highly recommended to run on a rooted device. Not achieving this can affect the results of the tests

### Local Action Runner

To run in github Actions environment, it is needed to configure a Local Self-hosted runner on youe machine.

To settup, follow the Github [Doc] (https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/about-self-hosted-runners)

At this moment, grapefruit has no authentication. It's possible to use it to inject arbitrary code to your iPhone for anyone that has the access to the web UI. Please limit it to `localhost` as much as possible. Contribution welcomed.

* [Development Setup](https://github.com/ChiChou/grapefruit/wiki/Development-Setup)
* [Troubleshooting](https://github.com/ChiChou/grapefruit/wiki/Trouble-Shooting)
* [Roadmap](https://github.com/ChiChou/Grapefruit/projects/1)

## Discord Group

If you have experienced anything wrong or want to suggest new features, please join my Discord channel! https://discord.gg/pwutZNx