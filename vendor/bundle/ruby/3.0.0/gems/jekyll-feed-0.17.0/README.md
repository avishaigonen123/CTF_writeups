---
layout: default
title: README
---

# Jekyll Feed plugin

A Jekyll plugin to generate an Atom (RSS-like) feed of your Jekyll posts

[![Continuous Integration](https://github.com/jekyll/jekyll-feed/actions/workflows/ruby.yml/badge.svg)](https://github.com/jekyll/jekyll-feed/actions/workflows/ruby.yml) [![Gem Version](https://badge.fury.io/rb/jekyll-feed.svg)](https://badge.fury.io/rb/jekyll-feed)

## Installation

Add this line to your site's Gemfile:

```ruby
gem 'jekyll-feed'
```

And then add this line to your site's `_config.yml`:

```yml
plugins:
  - jekyll-feed
```

:warning: If you are using Jekyll < 3.5.0 use the `gems` key instead of `plugins`.

## Usage

The plugin will automatically generate an Atom feed at `/feed.xml`.

### Optional configuration options

The plugin will automatically use any of the following configuration variables, if they are present in your site's `_config.yml` file.

* `title` or `name` - The title of the site, e.g., "My awesome site"
* `description` - A longer description of what your site is about, e.g., "Where I blog about Jekyll and other awesome things"
* `url` - The URL to your site, e.g., `https://example.com`. If none is provided, the plugin will try to use `site.github.url`.
* `author` - Global author information (see below)

### Already have a feed path?

Do you already have an existing feed someplace other than `/feed.xml`, but are on a host like GitHub Pages that doesn't support machine-friendly redirects? If you simply swap out `jekyll-feed` for your existing template, your existing subscribers won't continue to get updates. Instead, you can specify a non-default path via your site's config.

```yml
feed:
  path: /blog/feed.atom
```

To note, you shouldn't have to do this unless you already have a feed you're using, and you can't or wish not to redirect existing subscribers.

### Optional front matter

The plugin will use the following post metadata, automatically generated by Jekyll, which you can override via a post's YAML front matter:

* `date`
* `title`
* `excerpt`
* `id`
* `category`
* `tags`

Additionally, the plugin will use the following values, if present in a post's YAML front matter:

* `image` - URL of an image that is representative of the post (can also be passed as `image.path`)

* `author` - The author of the post, e.g., "Dr. Jekyll". If none is given, feed readers will look to the feed author as defined in `_config.yml`. Like the feed author, this can also be an object or a reference to an author in `_data/authors.yml` (see below).

* `description` - A short description of the post.

### Author information

*TL;DR: In most cases, put `author: [your name]` in the document's front matter, for sites with multiple authors. If you need something more complicated, read on.*

There are several ways to convey author-specific information. Author information is found in the following order of priority:

1. An `author` object, in the documents's front matter, e.g.:

  ```yml
  author:
    twitter: benbalter
  ```

2. An `author` object, in the site's `_config.yml`, e.g.:

  ```yml
  author:
    twitter: benbalter
  ```

3. `site.data.authors[author]`, if an author is specified in the document's front matter, and a corresponding key exists in `site.data.authors`. E.g., you have the following in the document's front matter:

  ```yml
  author: benbalter
  ```

  And you have the following in `_data/authors.yml`:

  ```yml
  benbalter:
    picture: /img/benbalter.png
    twitter: jekyllrb

  potus:
    picture: /img/potus.png
    twitter: whitehouse
  ```

  In the above example, the author `benbalter`'s Twitter handle will be resolved to `@jekyllrb`. This allows you to centralize author information in a single `_data/authors` file for site with many authors that require more than just the author's username.

  *Pro-tip: If `authors` is present in the document's front matter as an array (and `author` is not), the plugin will use the first author listed.*

4. An author in the document's front matter (the simplest way), e.g.:

  ```yml
  author: benbalter
  ```

5. An author in the site's `_config.yml`, e.g.:

  ```yml
  author: benbalter
  ```

### Meta tags

The plugin exposes a helper tag to expose the appropriate meta tags to support automated discovery of your feed. Simply place `{% feed_meta %}` someplace in your template's `<head>` section, to output the necessary metadata.

### SmartyPants

The plugin uses [Jekyll's `smartify` filter](https://jekyllrb.com/docs/templates/) for processing the site title and post titles. This will translate plain ASCII punctuation into "smart" typographic punctuation. This will not render or strip any Markdown you may be using in a title.

Jekyll's `smartify` filter uses [kramdown](https://kramdown.gettalong.org/options.html) as a processor.  Accordingly, if you do not want "smart" typographic punctuation, disabling them in kramdown in your `_config.yml` will disable them in your feed. For example:

   ```yml
   kramdown:
     smart_quotes:               apos,apos,quot,quot
     typographic_symbols:        {hellip: ...}
   ```

### Custom styling

Want to style what your feed looks like in the browser? When a XSLT Styleheet file named `feed.xslt.xml` exists at the root of your repository, a link to this stylesheet is added to the generated feed.

## Why Atom, and not RSS?

Great question. In short, Atom is a better format. Think of it like RSS 3.0. For more information, see [this discussion on why we chose Atom over RSS 2.0](https://github.com/jekyll/jekyll-rss-feed/issues/2).

## Categories

Jekyll Feed can generate feeds for each category. Simply define which categories you'd like feeds for in your config:

```yml
feed:
  categories:
    - news
    - updates
```

## Posts limit

By default the plugin limits the number of posts in the feed to 10. Simply define a new limit in your config:

```yml
feed:
  posts_limit: 20
```

## Collections

Jekyll Feed can generate feeds for collections other than the Posts collection. This works best for chronological collections (e.g., collections with dates in the filenames). Simply define which collections you'd like feeds for in your config:

```yml
feed:
  collections:
    - changes
```

By default, collection feeds will be outputted to `/feed/<COLLECTION>.xml`. If you'd like to customize the output path, specify a collection's custom path as follows:

```yml
feed:
  collections:
    changes:
      path: "/changes.atom"
```

Finally, collections can also have category feeds which are outputted as `/feed/<COLLECTION>/<CATEGORY>.xml`. Specify categories like so:

```yml
feed:
  collections:
    changes:
      path: "/changes.atom"
      categories:
        - news
        - updates
```

## Excerpt Only flag

Optional flag `excerpt_only` allows you to exclude post content from the Atom feed. Default value is `false` for backward compatibility.

When in `config.yml` is `true` than all posts in feed will be without `<content>` tags.

```yml
feed:
  excerpt_only: true
```

The same flag can be used directly in post file. It will be disable `<content>` tag for selected post.
Settings in post file has higher priority than in config file.

## Tags

To automatically generate feeds for each tag you apply to your posts you can add a tags setting to your config:

```yml
feed:
  tags: true
```

If there are tags you don't want included in this auto generation you can exclude them

```yml
feed:
  tags:
    except:
      - tag-to-exclude
      - another-tag
```

If you wish to change the location of these auto generated feeds (`/feed/by_tag/<TAG>.xml` by default) you can provide an alternative folder for them to live in.

```yml
feed:
  tags:
    path: "alternative/path/for/tags/feeds/"
```

If you only want to generate feeds for a few tags you can also set this.

```yml
feed:
  tags:
    only:
      - tag-to-include
      - another-tag
```

Note that if you include a tag that is excluded a feed will not be generated for it.

## Skip development

Use `disable_in_development: true` if you want to turn off feed generation when `jekyll.environment == "development"`,
but don't want to remove the plugin (so you don't accidentally commit the removal). Default value is `false`.

```yml
feed:
  disable_in_development: true
```

## Contributing

1. Fork it (https://github.com/jekyll/jekyll-feed/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
