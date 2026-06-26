source "https://rubygems.org"

# Jekyll static site generator — modern 4.x line.
gem "jekyll", "~> 4.3"

# Site plugins (loaded automatically in the :jekyll_plugins group).
group :jekyll_plugins do
  gem "jekyll-sitemap"   # generates sitemap.xml for search engines
  gem "jekyll-paginate"  # classic pagination used by this theme
  gem "jekyll-feed"      # generates an Atom/RSS feed at /feed.xml
  gem "jemoji"           # GitHub-style :emoji: support
end

# WEBrick was removed from Ruby's standard library in 3.0+, but
# `jekyll serve` still needs it for the local preview server.
gem "webrick", "~> 1.8"

# Faster, more reliable file-watching on Windows during local development.
gem "wdm", "~> 0.2", platforms: [:mingw, :x64_mingw, :mswin]

# Timezone data — Windows/JRuby don't ship the system tzinfo database.
gem "tzinfo", ">= 1", "< 3"
gem "tzinfo-data", platforms: [:mingw, :x64_mingw, :mswin, :jruby]
