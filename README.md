## fork-webbino-ahmsec
**Most people should use the original Webbino library: https://github.com/SukkoPera/Webbino/.** 

This fork is for experimental purposes.

## Changes made by this fork (thus far)
* Changed the value of the CORS ACAO response header from `*` to `http://localhost:8080`.
* In the 404 error response, no longer reflecting the user-set `pagename` value. Instead, we're returning a static value.
* Removed `PString-Arduino-lib` dependency from `library.properties`.

## License
fork-webbino-ahmsec is free software: you can redistribute it and/or modify it under the terms of version 3 of the GNU General Public License as published by the Free Software Foundation.

fork-webbino-ahmsec is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with Webbino. If not, see <http://www.gnu.org/licenses/>.
