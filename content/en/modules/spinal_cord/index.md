---
type: "modules" # DON'T TOUCH THIS ! :)

# Title of your project (we like creative title)
title: "Introduction to spinal cord MRI analysis"

# Your project GitHub repository URL
github_repo:

# If you are working on a project that has website, indicate the full url including "https://" below or leave it empty.
website:

# List +- 4 keywords that best describe your project within []. Note that the project summary also involves a number of key words. Those are listed on top of the [github repository](https://github.com/PSY6983-2021/project_template), click `manage topics`.
# Please only lowercase letters
tags: [spinal cord, spinal cord toolbox]

# Summarize your project in < ~75 words. This description will appear at the top of your page and on the list page with other projects..

summary: "This tutorial introduces basics of spinal cord MRI data analysis using the Spinal Cord Toolbox. 
The tutorial will cover the installation of the Spinal Cord Toolbox, the processing of spinal cord MRI data, and the visualization of the results."

# If you want to add a cover image (listpage and image in the right), add it to your directory and indicate the name
# below with the extension.
image: "spinal_cord_mri.png"
---
<!-- This is an html comment and this won't appear in the rendered page. You are now editing the "content" area, the core of your description. Everything that you can do in markdown is allowed below. We added a couple of comments to guide your through documenting your progress. -->

## Information

The estimated time to complete this training module is 3h.

The prerequisites to take this module are:
 * the [installation](/modules/installation) module.
   - Windows: Ubuntu application (Windows Linux Subsystem)
   - Mac/Linux: Terminal
 * the [introduction to the terminal](/modules/introduction_to_terminal) module.

Contact Jan Valosek if you have questions on this module, or if you want to check that you completed successfully all the exercises.

## Resources

The main resource for this module is the 2023 Spinal Cord Toolbox Course given by Prof. Julien Cohen-Adad and his team at [NeuroPoly lab](https://neuro.polymtl.ca).

The workshop is available on YouTube:

<iframe width="560" height="315" src="https://www.youtube.com/embed/hTbJo8GO5IU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

For the purpose of this module, we will focus on the following chapters of the workshop:

 * 18:39 `2. Installation`
 * 31:37 `3. Segmentation`
 * 47:35 `4. Vertebral labeling`
 * 1:07:30 `5. Shape-based analysis`
 * 1:31:03 `6. Registration to template` (only up to 1:48:00)

The slides are available [here](https://docs.google.com/presentation/d/1t40Fd0fS0SwWR5FU_GWKEvHkB9d96LVddLQW6L3QAx0/edit?usp=sharing).

## Exercise

 * Watch the selected chapters of the Spinal Cord Toolbox Course.
 * Install the Spinal Cord Toolbox on your local machine.
 * Download the sample data as described in the `2. Installation` chapter.
 * Do the segmentation of the spinal cord using two methods (e.g., `sct_deepseg_sc`, `sct_propseg`, `sct_deepseg`) and compare the results. TIP: to visualize the results, you can use viewer of your choice (e.g., `fsleyes`, `itk-snap`) or python (`nibabel` and `matplotlib`).
 * Perform the vertebral labeling.
 * Compute cross-sectional area (CSA) of the spinal cord at the C2-C3 levels.
 * Do the registration of the T2w image to the template.
 * Follow up with your local TA to validate you completed the exercises correctly.
 * 🎉 🎉 🎉 you completed this training module! 🎉 🎉 🎉

## More resources

If you want to learn more about spinal cord MRI data analysis and Spinal Cord Toolbox, please check:
 * the [Spinal Cord Toolbox documentation](https://spinalcordtoolbox.com)
 * the [Spinal Cord Toolbox tutorials](https://spinalcordtoolbox.com/user_section/tutorials.html#)