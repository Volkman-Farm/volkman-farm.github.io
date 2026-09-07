const isFuture = (data) => new Date(data.page.date) > new Date();

export default {
  layout: 'post',
  tags: ['post'],
  eleventyComputed: {
    // Future-dated posts build no page and stay out of collections until their date passes.
    permalink: (data) => (isFuture(data) ? false : `/blog/${data.page.fileSlug}/`),
    eleventyExcludeFromCollections: (data) => isFuture(data),
  },
};
