# tcjexl

This is a wrapper of the [pyjexl](https://pypi.org/project/pyjexl/) library, including a set of default transformations  (detailed in [this section](#included-transformations))

Current version of the tcjexl library embeds the pyjexl code (as in [0.3.0 release](https://files.pythonhosted.org/packages/ab/1d/757ac4c9ae2da97cbb2c844fb70395990b5bbacccff5c0297ceefd670c62/pyjexl-0.3.0.tar.gz)) in order to apply some fixes. Ideally, the fix should be applied on the upstream library (in this sense, ve have created [this PR](https://github.com/mozilla/pyjexl/pull/30)) but it hasn't been merged yet at the moment of writing this by pyjexl mantainers. Hopefully, if at some moment the fix is applied on pyjexl we could simplify this (it would be a matter of rollback [this PR](https://github.com/telefonicasc/tcjexl/pull/6) and set the proper pyjexl dependency, e.g. `pyjexl==0.4.0`)

Example:

```python
from tcjexl import JEXL

jexl = JEXL()

context = {"a": 5, "b": 7, "c": "a TEXT String"}

print(jexl.evaluate('a+b', context))
print(jexl.evaluate('c|lowercase', context))
```

Result:

```
12
a text string
```

## Using simulated time

By default, the current time reference used by [date related transformations](#date related transformations) is system current time. However, this can be changed using the positional argument `now` in the `JEXL` constructor to specify a function that returns a `datetime` object to be used as current time.

For instance, if we want to set current time to November 13th, 2020 at 6:24:58am we can use:

```python
from tcjexl import JEXL
import datetime

def simulated_time():
    return datetime.datetime(2020, 11, 13, 6, 24, 58, 000, tzinfo=datetime.timezone.utc)

jexl = JEXL(now=simulated_time)

print(jexl.evaluate('0|currentTimeIso', {}))
```

Result:

```
2020-11-13T06:24:58.000Z
```

## Included transformations

**NOTE:** JEXL pipeline is needed even if the transformation doesn't need an parameter to work (e.g. `currentTime` that provides the current system time and doesn't need and argument). In this case, we use `0|` for these cases (e.g. `0|currentTime`).

### Math related transformations

- `rnd`: returns a random number between two integers. Examples: `0|rnd(10)` returns a random number between 0 (included) and 10 (not included). `12|rnd(99)` returns a random number between 12 (included) and 99 (not included).
- `rndFloat`: returns a random number between two decimal numbers. Examples: `0.2|rndFloat(12.7)` returns a random number between 0.2 and 12.7.
- `round`: rounds a number with a given number of precision digits. Example: `0.12312|round(2)` returns `0.12`, rounding 0.12312 to two decimals.
- `floor`: rounds a number to the lesser integer. Example: `4.9|floor` returns `4`.
- `parseInt`: converts a string to integer
- `parseFloat`: coverts a string to float

### String related transformations

- `uppercase`: converts a given string to uppercase.
- `lowercase`: converts a given string to lowercase.
- `toString`: returns string representation
- `substring`: returns a substring. Examaple: `aGivenString|substring(3,6)` returns `ven`.
- `includes`: returns `True` is string passed as argument is included in the one that comes in the pipe. Example: `"aGivenString"|includes("Given")` return `True` while `"aGivenString"|includes("Text")` returns `False`. 
- `len`: returns the number of items in an array or the length of a string.

### List related transformations

- `next`: returns the next item in an array. Example: `12|next([1,2,3,12,15,18])` returns 15.
- `indexOf`: returns the index corresponding to an item in an array. Example: `[1, 2, 3, 12, 15, 18]|indexOf(15)` returns `4`.
- `rndList`: returns an array of random elements within two limits. Example: `0|rndList(6,8)` is an array with 8 items and each item is a random number between 0 and 6.
- `rndFloatList`: similar to `rndList`, but with decimal numbers.
- `zipStringList`: concat two arrays of the same length with a given separator.
- `concatList`: concat array elements.

### Date related transformations

- `currentTime`: returns current time in UTC format.
- `currentTimeIso`: returns current time in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators) format.
- `toIsoString`: allows to format a date into [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601#Time_zone_designators) format.
- `currentTimeFormat`: allows to format current time with a given format. For instance, if current date is 07/07/2023 and we use `0|currentTimeFormat("%Y")` then `2023` will be returned.
- `timeFormat`: allows to format a given date with a given format. For instance, if current date is 07/07/2023 and we use `0|currentTime|timeFormat("%Y")` then `2023` will be returned.
- `currentHour24`: returns current time in 24 hours format. Example: `0|currentHour24`.
- `currentDay`: returns the current day of the month. Example: `0|currentDay`.

### Interpolation transformations

- `interpolate`: returns number interpolation, given an initial value, a final value and a number of steps. Example: `3|interpolate(0,10,9)`
- `linearInterpolator`: returns linear value interpolation, taking into account an array of values in `[number, value]` format. Example: `number|linearInterpolator([ [0,0], [1,1], [2,1.5], [8,1.8], [10,2.0]])` for number 2 returns `1.5`, for number 5 returns the linear interpolation between 2 and 8, taking into account the associated values 1.5 and 1.8 respectively.
- `linearSelector`: allows to select a given value taking into account ranges defined between two elements in an array. Example: `0|rndFloat(1)|linearSelector([[0.02,'BLACK'], [0.04,'NO FLAG'], [0.06,'RED'], [0.21,'YELLOW'], [1,'GREEN']])`, if input is `0.02 < (0|rndFloat(1)) ≤ 0,04` returns `NO FLAG`.
- `randomLinearInterpolator`: returns linear value interpolation with a random factor, taking into account an array of values in `[number, value]` format. Example: `number|randomLinearInterpolator([0,1],[ [0,0], [1,1], [2,1.5], [8,1.8], [10,2.0]])` for number 2 returns a value close to 1.5 (close due to a random factor is applied), for number 5 returns the lineal interpolation between 2 and 8, taking into account the associated values 1.5 and 1.8 respectively and the random factor. The random factor is specified as a `[min, max]` array and the calculated interpolated value is multiplied by a random number between `min` and `max`. For instance, with `[0.85, 0.99]` the result will be closer to the interpolation but with `[0, 1]` the spread will be wider.
- `alertMaxValue`: returns `True` when input value is greater on equal to a given condition. Example: `0|rnd(5)|alertMaxValue(2)` returns `True` when `0|rnd(5)` is 3, 4 or 5 (for other input values result will be `False`).
- `valueResolver`: given an array `[str, value]` allows to map string with values. Example: `flag|valueResolver([['BLACK', 'stormy'], ['NO FLAG', 'curly'], ['RED', 'stormy'], ['YELLOW', 'curly'], ['GREEN', 'plain']])` is the evaluation of `flag` field is `GREEN` then the returned value would be `plain`.

# Miscelaneous transformations

- `typeOf`: returns type representation of the data (e.g. `str`, `int`, `float`, etc.)
- `strToLocation`: given a string with a comma separated list of decimal numbers, returns an array of such numbers. Example: `"value1, value2"|strToLocation`. Example: `"value1, value2"|strToLocation` returns `[value1, value2]`. It's name (maybe not very good :) is due to it can be useful to generate a [GeoJSON](https://geojson.org/) representing a point which coordinates are provided in a string, eg: `{coordinates:(point|strToLocation),type: "Point"}`

## Packaging

* Check `VERSION` value in `setup.py` file.
* Run

```bash
python3 setup.py sdist bdist_wheel
```

* The file `tcjexl-<version>.tar.gz` is generated in the `dist` directory.

## Uploading package to pypi repository

Once the package has been build as explained in the previous section it can be uploaded to pypi repository.

First, install the twine tool:

```bash
pip install twine
```

Next, run:

```bash
twine upload dist/tcjexl-x.y.z.tar.gz
```

You need to be registered at https://pypi.org with permissions at https://pypi.org/project/tcjexl/, as during the
upload process you will be prompted to provide your user and password.

## Changelog

0.2.0 (March 11th, 2024)

- Add: allow to use context for transformations arguments (using a patched version of pyjexl)

0.1.0 (March 6th, 2024)

- Initial release
