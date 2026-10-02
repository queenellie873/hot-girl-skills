# worked example: explaining a debounce

a full run of the skill, start to finish. // this is the bar: one screen, zero walls of text

## the prompt

```
/code-explainer-but-i-have-adhd src/utils/debounce.js
```

## the code (`src/utils/debounce.js`)

```js
1  export function debounce(fn, wait = 300) {
2    let timeoutId;
3    return function debounced(...args) {
4      clearTimeout(timeoutId);
5      timeoutId = setTimeout(() => {
6        fn.apply(this, args);
7      }, wait);
8    };
9  }
10
11 // usage
12 const search = debounce((query) => fetchResults(query), 300);
13 input.addEventListener('input', (e) => search(e.target.value));
```

## the response

**tl;dr:** `debounce` makes a function wait until you stop calling it for 300ms, so your search box fires one request instead of twelve.

**the path:** `debounce.js:12` you wrap a function -> `debounce.js:13` every keystroke calls the wrapper -> `debounce.js:4-5` each call resets a timer -> `debounce.js:6` the real function runs once things go quiet

### 1. the real-life version
it's an elevator door. every time someone walks in, the door waits a little longer before closing.
- **wrap:** you hand `debounce` a function and get back a new one (`:1`, `:3`)
- **reset:** each call cancels the old timer and starts a fresh one (`:4-5`)
- **fire:** only the last call survives long enough to run (`:6`)

`checkpoint: 1/3 done`

### 2. what happens when you type "cats"

| you type | timer | runs? |
|---|---|---|
| c | start 300ms | no |
| ca | restart | no |
| cat | restart | no |
| cats, then pause | finishes | yes, with "cats" |

- **one request** instead of four. your API (and your rate limit) says thank you

`checkpoint: 2/3 done`

### 3. the two sneaky bits
- **closure:** every call to the wrapper shares one timer, because `timeoutId` (`:2`) lives inside `debounce`. that's a closure: a function remembering variables from where it was made
- **apply:** `fn.apply(this, args)` (`:6`) passes along the original arguments and `this`, so the wrapped function behaves like the original

`checkpoint: 3/3. you've got the whole thing :)`

`// side quest: debounce's sibling is throttle, which runs at most once every N ms instead of waiting for quiet.`

**next:** open `debounce.js`, change `300` to `1000` on line 12, and type in the box. you'll feel the delay.

**go deeper?** debounce vs throttle, adding a "run immediately" option, or why arrow functions matter on line 5

## if they reply "shorter"

**tl;dr:** waits until you stop calling it for 300ms, then runs once.

**the path:** `:12` wrap -> `:4-5` every call resets the timer -> `:6` runs after the quiet

**next:** change `300` to `1000` on line 12 and type. feel the wait.

## if they reply "like i'm 5"

**tl;dr:** it's a patient friend who waits until you're done talking before answering.

- you keep **talking**: the friend keeps waiting
- you **stop**: they count to three
- then they **answer** once, about the last thing you said
