# Brainhack School

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-2-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
This is the website of the brainhack school, built with [hugo](https://gohugo.io/). 

## Deploying site

The deployment of the website is automated using github actions. 

## Run locally 

To test it locally, you will need to:

1. Create your own fork

2. Clone this GitHub repo or the fork (change the URL if it's a fork): 

   ```bash
   git clone https://github.com/school-brainhack/school-brainhack.github.io.git
   ```

3. Make sure you're inside the `school-brainhack.github.io/` directory, then **clone the submodule for themes:** 

   ```bash
   cd school-brainhack.github.io
   git submodule update --init --recursive --remote
   ```

4. If [Hugo](https://gohugo.io/) is not installed, follow the steps in their documentation to install it on your machine: https://gohugo.io/getting-started/installing/
5. To run the website locally, make sure you are still in `school-brainhack.github.io/` directory and build the website with
   ```bash
   hugo serve -D
   ```
   The `-D` option is to serve the website including the draft .md files.

   Navigate the local version to make sure things are compiled correctly.

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/me-pic"><img src="https://avatars.githubusercontent.com/u/77584086?v=4?s=100" width="100px;" alt="Marie-Eve Picard (she/her)"/><br /><sub><b>Marie-Eve Picard (she/her)</b></sub></a><br /><a href="#translation-me-pic" title="Translation">🌍</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/clarkenj"><img src="https://avatars.githubusercontent.com/u/57987005?v=4?s=100" width="100px;" alt="Natasha Clarke"/><br /><sub><b>Natasha Clarke</b></sub></a><br /><a href="#ideas-clarkenj" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
