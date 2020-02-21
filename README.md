# Cracking Salts

The following Python script a brute-force for encrypted passwords (using the native built-in module called `Crypt`).

The script makes a comparison between two `txt` files, one of them, the `dictionary.txt` contains a plain-text password of possible user inputs for passwords. On the other side, the `passwords.txt` contains records inspired on the Linux `/etc/passwd` file where we find the user of the system and the encrypted system password split by a `:` symbol.

The `main` function of the program will split the `user` and the `password` element from the` passwords.txt` file and will compare the result of the `encrypted` password with a `dictionary list` of `known-passwords` on the `dictionary.txt` file (`crack` function)

This can be a very handle script for PoC examples.

## Usage

Preferable, use an isolated environment with `virtualenv`, because the `termcolor` package is required.

`salt.py`

Make sure you have the `passwords.txt` and the `dictionary.txt` files in the same directory as the main script.

## Set up

Simple, just.

`virtualenv -p python3 <name_of_the_env>`

## Credits

 - [David E Lares](https://twitter.com/davidlares3)

## License

 - [MIT](https://opensource.org/licenses/MIT)
