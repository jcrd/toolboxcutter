# toolboxcutter

toolboxcutter (`tb`) is a script to automate use of
[toolbox](https://github.com/containers/toolbox) using per-project
`Dockerfile`s.

## Packages

* **RPM** package available from [copr][1]. [![Copr build status](https://copr.fedorainfracloud.org/coprs/jcrd/toolboxcutter/package/toolboxcutter/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/jcrd/toolboxcutter/package/toolboxcutter/)

  Install with:
  ```
  dnf copr enable jcrd/toolboxcutter
  dnf install toolboxcutter
  ```

## Usage

```
usage: tb [command]

With no command, enter toolbox.

commands:
  init IMAGE      Initialize Dockerfile based on IMAGE
  create [IMAGE]  Create container (from IMAGE if provided)
  recreate        Remove and recreate container
  build [NAME]    Build image (with NAME if provided)
  rebuild         Remove container and rebuild image
  stop            Stop container
  rm              Remove container
  rmi             Remove image
  rpkg            Build rpm via rpkg
    options:
      -n NAME       rpkg spec template name
      -e EXT        rpkg spec template extension
  rpkg-install    Build and install rpm via rpkg
    options:
      -n NAME       rpkg spec template name
      -e EXT        rpkg spec template extension
      -r NAME       Name of produced rpm to install
  run COMMAND     Run COMMAND in toolbox
  version         Show version
```

`tb` will look for a `Dockerfile` in the working directory. If it exists, the
toolbox image will be automatically created if necessary, then the toolbox
will be entered.

All commands must be run outside of the toolbox.

**Note**: For the rpkg commands to function, `rpkg` must be installed inside the
toolbox.

### Example Dockerfile

An example toolbox `Dockerfile` for shell script development:
```
FROM registry.fedoraproject.org/f33/fedora-toolbox:33

RUN dnf install -y neovim
RUN dnf install -y rpkg
RUN dnf install -y ShellCheck
RUN dnf install -y npm

RUN npm i -g bash-language-server
```

See [jcrd/toolboxes](https://github.com/jcrd/toolboxes) for additional examples.

## License

This project is licensed under the MIT License (see [LICENSE](LICENSE)).

[1]: https://copr.fedorainfracloud.org/coprs/jcrd/toolboxcutter/
