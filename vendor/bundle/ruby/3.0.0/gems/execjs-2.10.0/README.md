---
layout: default
title: README
---

ExecJS
======

ExecJS lets you run JavaScript code from Ruby. It automatically picks
the best runtime available to evaluate your JavaScript program, then
returns the result to you as a Ruby object.

ExecJS supports these runtimes:

* [therubyrhino](https://github.com/cowboyd/therubyrhino) - Mozilla
  Rhino embedded within JRuby
* [Duktape.rb](https://github.com/judofyr/duktape.rb) - Duktape JavaScript interpreter
* [Node.js](http://nodejs.org/)
* [Bun.sh](https://bun.sh) - JavaScript runtime & toolkit designed for speed
* Apple JavaScriptCore - Included with Mac OS X
* [Microsoft Windows Script Host](http://msdn.microsoft.com/en-us/library/9bbdkx3k.aspx) (JScript)
* [Google V8](http://code.google.com/p/v8/)
* [mini_racer](https://github.com/rubyjs/mini_racer) - Google V8
  embedded within Ruby
* [GraalVM JavaScript](https://www.graalvm.org/javascript/) - used on TruffleRuby

A short example:

``` ruby
require "execjs"
ExecJS.eval "'red yellow blue'.split(' ')"
# => ["red", "yellow", "blue"]
```

A longer example, demonstrating how to invoke the CoffeeScript compiler:

``` ruby
require "execjs"
require "net/http"
source = Net::HTTP.get(URI("https://coffeescript.org/browser-compiler-legacy/coffeescript.js"))

context = ExecJS.compile(source)
context.call("CoffeeScript.compile", "square = (x) -> x * x", bare: true)
# => "var square;\nsquare = function(x) {\n  return x * x;\n};"
```

# Forcing a specific runtime

If you'd like to use a specific runtime rather than the autodetected one, you can assign `ExecJS.runtime`:

```ruby
ExecJS.runtime = ExecJS::Runtimes::Node
```

Alternatively, you can define it via the `EXECJS_RUNTIME` environment variable:

```bash
EXECJS_RUNTIME=Node ruby ...
```

You can find the list of possible runtimes in [`lib/execjs/runtimes.rb`](https://github.com/rails/execjs/blob/master/lib/execjs/runtimes.rb).

# Installation

```
$ gem install execjs
```

# FAQ

**Why can't I use CommonJS `require()` inside ExecJS?**

ExecJS provides the lowest common denominator interface to any JavaScript runtime.
Use ExecJS when it doesn't matter which JavaScript interpreter your code runs
in. If you want to access the Node API, you should check another library like
[commonjs.rb](https://github.com/cowboyd/commonjs.rb) designed to provide a
consistent interface.

**Why can't I use `setTimeout`?**

For similar reasons as modules, not all runtimes guarantee a full JavaScript
event loop. So `setTimeout`, `setInterval` and other timers are not defined.

**Why can't I use ES5 features?**

Some runtimes like Node will implement many of the latest ES5 features. However
older stock runtimes like JSC on OSX and JScript on Windows may not. You should
only count on ES3 features being available. Prefer feature checking these APIs
rather than hard coding support for specific runtimes.

**Can ExecJS be used to sandbox scripts?**

No, ExecJS shouldn't be used for any security related sandboxing. Since runtimes
are automatically detected, each runtime has different sandboxing properties.
You shouldn't use `ExecJS.eval` on any inputs you wouldn't feel comfortable Ruby
`eval()`ing.

## Contributing to ExecJS

ExecJS is the work of dozens of contributors. You're encouraged to submit pull requests, propose
features and discuss issues.

See [CONTRIBUTING](CONTRIBUTING.md).

## License
ExecJS is released under the [MIT License](MIT-LICENSE).
