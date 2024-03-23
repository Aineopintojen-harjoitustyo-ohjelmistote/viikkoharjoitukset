<head>
<title>Slice It Off! - Specification</title>
<meta name="author" content="Viljami Ilola">
</head>

<hr class="PAGE-BREAK">

# Gameplay

## Goal
The goal of the game is ultimately beat the highscores. There should just a
right amount of luck making game interesting while also requiring some the
skill.

## Mechanism
Game consists of play area, enemies moving in that area and player with
slicing tool. Goal here is to make total area where enemies moving small
enough to pass the level. Slicing can be done vertivally or horizontally. If
there is enemies left on both sides after slicing both parts of the play
area will remain. All the cleared areas will be destroyed.

## Scoring
One can get points by passing levels. Still majority of possible points
comes from different bonuses. One can for example get bonus by being fast,
not isolating enemies, picking up collectibles.

<hr class="PAGE-BREAK">

# The Look
In one word game should look "retro". This essentially means blocky fonts,
limited colors and definedly no rounded edges anywhere.

<hr class="PAGE-BREAK">

# Technical

## Used techniques

### Python
Programming will be done by Python. Specifically version 3.8 or newer. No
trick included in Python is ruled out, but external dependencies are tried
to keep at the minimum.

### Pygame
Project makes heavy use of
[pygame](https://www.pygame.org/)
library. Pygame
[sprites](https://www.pygame.org/docs/ref/sprite.html)
are the basic building blocks. Game logic somewhat inbaked to the
game objects for easy handling.

## Developement Environment

### Build System
[Poetry](https://python-poetry.org/)
will be used for develop, build and publich the package. Poetry keeps track
of dependencies. There will be also `./dev.sh`-script to help out firing up
developement tools like
[pytest](https://pytest.org/)
,
[coverage](https://pypi.org/project/coverage/)
and
[pylint](https://pypi.org/project/pylint/)
.

### Testing & Quality
There will be comprehensive unit testing with branch coverage reports. For
that pytest and coverage python packages will be used. Pylint takes care
that code is good in quality and commented properly.

<hr class="PAGE-BREAK">

# Distribution

## Open source
Source code will be licensed as
[GPL-2](https://www.gnu.org/licenses/old-licenses/gpl-2.0.html)
and it's freely available at
[git.hix.fi](https://git.hix.fi/sliceitoff.git/)
.

## Publishing
The ultimate goal is to make game so good that in can be published as
[PyPA](https://www.pypa.io/en/latest/)
package. Then everyone can install it easily as `pip install sliceitoff`. To
be honest I bet there will not be enough time to polish the game that much.
