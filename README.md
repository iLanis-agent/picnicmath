# Picnic math

Picnic math plans the outing before the basket comes out: the blanket at a
labeled spot becomes the seating grid, the party at a labeled portion
becomes the boxes to pack, and the cooler at a labeled pack coverage
becomes the ice.

Live site: https://ilanis-agent.github.io/picnicmath/

## The three tools

- **Spot plan** - `floor(width / labeled spot (60 cm)) x floor(depth /
  labeled spot)` sitting spots and the fringe left over, with a date
  blanket / family blanket / full reunion verdict.
- **Basket plan** - `heads x labeled portion (500 g)` of picnic and
  `ceil(total / labeled box (1200 g))` boxes with the room to spare, with
  a quiet picnic / family spread / crowd feast verdict.
- **Ice plan** - `ceil(cooler L / labeled pack coverage (10 L))` ice packs
  and the overlap, with a light chill / working cooler / deep freeze
  verdict.

## Limits

Every default is labeled and illustrative. Real picnics depend on weather,
park rules, appetites and food safety guidance. This is planning
arithmetic, not an outing guarantee: pack for the real day.

## Files

- `index.html` - landing page with the labeled norms
- `app.html` - the three calculators
- `engine.js` - shared calculation and render logic (browser + node)
- `oracle.py` - python mirror of the engine, writes `expected.json`
- `test.js` - runs the engine against `expected.json` (30 cases, 169 checks)

Run the tests: `python3 oracle.py && node test.js`
