# Midori

System design and implementation for a web crawler. \
Inspiration from --> https://www.youtube.com/watch?v=0LTXCcVRQi0

<p align="center">
<img src="https://github-production-user-asset-6210df.s3.amazonaws.com/48282663/243183222-2e97f423-5dd6-4cdb-858d-883aa22d1471.png">
<h1 align="center">
   Midori
  </h1>
  
</p>

# System Design

## High Level Design

This will be the high level flow of the data, initally the api will call DB, which will inturn call the crawler which will fetch html pages and parse information. The crawler also needs URLs to fetch html pages which would be in our URL DB, we would initally feed some pages to the URL DB but it will be self sustaining loop where crawler would provide URLs to URL DB after parsing webpages.

![Untitled-2023-03-17-1604(1)](https://github.com/myan-ish/midori/assets/48282663/a1bc1ae5-3c7a-49b5-980c-889628eddd8e)

## Low Level Design
