export default function (eleventyConfig) {
  eleventyConfig.addPassthroughCopy({
    'assets': 'assets',
  });
  eleventyConfig.setIncludesDirectory('_includes');
  eleventyConfig.setLayoutsDirectory('_layouts');
};
