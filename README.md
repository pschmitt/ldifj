# ldifj

This Python script parses LDAP Data Interchange Format (LDIF) files,
allows for the extraction of entries and, optionally, metadata.

## 🛠 Installation

Install the required modules with pip(x):

```shell
pip install ldifj
# the cool kids use pipx nowadays:
pipx install ldifj
```

## 🚀 Usage

```console

usage: ldif [-h] [--metadata] [FILE]

positional arguments:
  FILE         LDIF file to parse, set to '-' to read from stdin

optional arguments:
  -h, --help   show this help message and exit
  --metadata, -m
               Include metadata
```

## 📝 Examples

To parse an LDIF file, run:

```shell
ldif example.ldif
```

`ldif` also accepts input from a pipe:

```shell
cat example.ldif | ldif
```

If you want to include the metadata in the returned JSON object:

```bash
ldif --metadata example.ldif
```

## 📜 License

[GNU General Public License v3 (GPL-3)](./LICENSE).
